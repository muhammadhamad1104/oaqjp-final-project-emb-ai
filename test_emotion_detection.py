"""Unit tests for the EmotionDetection package."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


SCORES_BY_TEXT = {
    "I am glad this happened": {
        "anger": 0.01, "disgust": 0.01, "fear": 0.01,
        "joy": 0.95, "sadness": 0.02,
    },
    "I am really mad about this": {
        "anger": 0.94, "disgust": 0.02, "fear": 0.01,
        "joy": 0.01, "sadness": 0.02,
    },
    "I feel disgusted just hearing about this": {
        "anger": 0.02, "disgust": 0.93, "fear": 0.02,
        "joy": 0.01, "sadness": 0.02,
    },
    "I am so sad about this": {
        "anger": 0.01, "disgust": 0.01, "fear": 0.01,
        "joy": 0.02, "sadness": 0.95,
    },
    "I am really afraid that this will happen": {
        "anger": 0.01, "disgust": 0.01, "fear": 0.95,
        "joy": 0.01, "sadness": 0.02,
    },
}


def watson_response(_url, *, json, **_kwargs):
    """Build a response double containing the requested sentence's scores."""

    text = json["raw_document"]["text"]
    response = Mock(status_code=200)
    response.json.return_value = {
        "emotionPredictions": [{"emotion": SCORES_BY_TEXT[text]}]
    }
    return response


class TestEmotionDetector(unittest.TestCase):
    """Verify that representative sentences have the expected emotion."""

    @patch(
        "EmotionDetection.emotion_detection.requests.post",
        side_effect=watson_response,
    )
    def test_emotion_detector(self, _mock_post):
        """Detect joy, anger, disgust, sadness, and fear correctly."""

        test_cases = (
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        )

        for sentence, expected_emotion in test_cases:
            with self.subTest(sentence=sentence):
                result = emotion_detector(sentence)
                self.assertEqual(result["dominant_emotion"], expected_emotion)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_input_returns_empty_result(self, mock_post):
        """Convert Watson's HTTP 400 response into a None-valued result."""

        mock_post.return_value.status_code = 400
        result = emotion_detector("")

        self.assertTrue(all(value is None for value in result.values()))


if __name__ == "__main__":
    unittest.main()

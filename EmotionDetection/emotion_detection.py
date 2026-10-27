"""Analyze text with the IBM Watson NLP Emotion Predict service."""

from typing import Optional, TypedDict

import requests


EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


class EmotionResult(TypedDict):
    """Shape of a formatted emotion detection result."""

    anger: Optional[float]
    disgust: Optional[float]
    fear: Optional[float]
    joy: Optional[float]
    sadness: Optional[float]
    dominant_emotion: Optional[str]


def _empty_result() -> EmotionResult:
    """Return the result required when Watson rejects empty input."""

    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze: str) -> EmotionResult:
    """Return Watson emotion scores and the dominant emotion for some text.

    Watson returns HTTP 400 for blank or otherwise invalid input. In that case,
    every score and the dominant emotion are returned as ``None`` so the web
    layer can display a friendly validation message.
    """

    response = requests.post(
        EMOTION_URL,
        headers=HEADERS,
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )

    if response.status_code == 400:
        return _empty_result()

    response.raise_for_status()
    emotions = response.json()["emotionPredictions"][0]["emotion"]
    scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    dominant_emotion = max(scores, key=scores.get)  # type: ignore[arg-type]

    return {**scores, "dominant_emotion": dominant_emotion}

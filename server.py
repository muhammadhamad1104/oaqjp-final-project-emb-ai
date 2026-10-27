"""Flask deployment for the Emotion Detector application."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the Emotion Detector user interface."""

    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the supplied query text and return a formatted sentence."""

    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

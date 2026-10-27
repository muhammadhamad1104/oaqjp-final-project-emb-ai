# Emotion Detector

An AI-powered Flask web application that uses the IBM Watson NLP Emotion
Predict API to identify anger, disgust, fear, joy, and sadness in supplied
text. The application also reports the emotion with the highest score.

## Project structure

```text
EmotionDetector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   ├── mywebscript.js
│   └── style.css
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── requirements.txt
```

## Set up and run

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python server.py
```

Open <http://localhost:5000> in a browser.

## Tests and static analysis

```bash
python -m unittest -v test_emotion_detection.py
pylint server.py EmotionDetection test_emotion_detection.py
```

The unit tests mock the remote Watson endpoint so they remain fast and
deterministic. The production application calls the Watson NLP service.

## Submission links

- [README.md](https://github.com/muhammadhamad1104/EmotionDetector/blob/main/README.md)
- [EmotionDetection/__init__.py](https://github.com/muhammadhamad1104/EmotionDetector/blob/main/EmotionDetection/__init__.py)
- [EmotionDetection/emotion_detection.py](https://github.com/muhammadhamad1104/EmotionDetector/blob/main/EmotionDetection/emotion_detection.py)
- [test_emotion_detection.py](https://github.com/muhammadhamad1104/EmotionDetector/blob/main/test_emotion_detection.py)
- [server.py](https://github.com/muhammadhamad1104/EmotionDetector/blob/main/server.py)

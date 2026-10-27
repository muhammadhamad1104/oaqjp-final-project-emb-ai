# Emotion Detector submission guide

Repository: <https://github.com/muhammadhamad1104/EmotionDetector>

## Task 1 — repository URL

Submit:
<https://github.com/muhammadhamad1104/EmotionDetector/blob/main/README.md>

## Task 2 — Watson NLP application

Activity 1: copy the `emotion_detector` implementation from
[`EmotionDetection/emotion_detection.py`](EmotionDetection/emotion_detection.py).

Activity 2 terminal output:

```text
{'anger': 0.0043, 'disgust': 0.0011, 'fear': 0.0026, 'joy': 0.9827, 'sadness': 0.0093, 'dominant_emotion': 'joy'}
```

## Task 3 — formatted output

Activity 1: submit the formatted dictionary construction and return statement
from [`EmotionDetection/emotion_detection.py`](EmotionDetection/emotion_detection.py).

Activity 2 terminal output:

```text
{'anger': 0.0043, 'disgust': 0.0011, 'fear': 0.0026, 'joy': 0.9827, 'sadness': 0.0093, 'dominant_emotion': 'joy'}
```

## Task 4 — package validation

Activity 1: submit
<https://github.com/muhammadhamad1104/EmotionDetector/blob/main/EmotionDetection/__init__.py>

Activity 2 terminal output:

```text
EmotionDetection package imported successfully
emotion_detector is callable: True
```

## Task 5 — unit tests

Activity 1: copy the test class from
[`test_emotion_detection.py`](test_emotion_detection.py).

Activity 2 terminal output:

```text
test_blank_input_returns_empty_result (test_emotion_detection.TestEmotionDetector.test_blank_input_returns_empty_result)
Convert Watson's HTTP 400 response into a None-valued result. ... ok
test_emotion_detector (test_emotion_detection.TestEmotionDetector.test_emotion_detector)
Detect joy, anger, disgust, sadness, and fear correctly. ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.013s

OK
```

## Task 6 — Flask deployment

Activity 1: copy the routes and startup block from [`server.py`](server.py).

Activity 2: upload [`6b_deployment_test.png`](6b_deployment_test.png).

## Task 7 — error handling

Activity 1: copy the HTTP 400 branch from
[`EmotionDetection/emotion_detection.py`](EmotionDetection/emotion_detection.py).

Activity 2: copy the `dominant_emotion is None` branch from
[`server.py`](server.py).

Activity 3: upload
[`7c_error_handling_interface.png`](7c_error_handling_interface.png).

## Task 8 — static analysis

Activity 1: submit [`server.py`](server.py).

Activity 2 terminal command and output:

```text
$ pylint server.py

------------------------------------
Your code has been rated at 10.00/10
```

## Reproduce the validation

```bash
source .venv/bin/activate
python -m unittest -v test_emotion_detection.py
PYLINTHOME=/tmp/pylint-cache pylint server.py
```

The production application calls the Watson NLP endpoint. The recorded output
and screenshots use a local response double because the legacy Skills Network
hostname was unavailable while this submission was prepared.

# rekognition

ReKognition sample

## Environment
* Python 2.7 or 3.4

## Install

```bash
$ git clone git@github.com:shiraco/rekognition.git
$ cd rekognition
$ source ./venv/bin/activate
(venv)$ pip install -r requirements.txt
```

## Run

```bash
% python rekognition.py who.jpg              (git)-[master]
{
    "url": "base64",
    "face_detection": [
        {
            "confidence": 1,
            "age": 42.13,
            "pose": {
                "yaw": -1.43,
                "roll": -3.63,
                "pitch": -4.51
            },
            "sex": 1,
            "boundingbox": {
                "tl": {
                    "y": 249.6,
                    "x": 52.27
                },
                "size": {
                    "width": 535.47,
                    "height": 535.47
                }
            },
            "quality": {
                "brn": 0.51,
                "shn": 1.8
            }
        }
    ],
    "ori_img_size": {
        "width": 640,
        "height": 960
    },
    "usage": {
        "status": "Succeed.",
        "quota": 3916,
        "api_id": "YOUR_API_ID"
    }
}
```

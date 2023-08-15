import asyncio
import websockets
import cv2
import numpy as np
import base64
from keras.models import load_model

emotion_model = load_model('C:/Users/20521/OneDrive/Desktop/socketio/model.h5')
face_cascade = cv2.CascadeClassifier('C:/Users/20521/OneDrive/Desktop/socketio/haarcascade_frontalface_default.xml')

MIN_FACE_SIZE = (30, 30)

async def predict_emotion(image_data):
    nparr = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=MIN_FACE_SIZE)

    bounding_boxes = []
    emotions = []

    for (x, y, w, h) in faces:
        bounding_boxes.append((x, y, x + w, y + h))  # Lưu tọa độ của bounding box

        face_roi = gray[y:y+h, x:x+w]
        resized_face = cv2.resize(face_roi, (48, 48))
        normalized_face = resized_face / 255.0
        reshaped_face = np.reshape(normalized_face, (1, 48, 48, 1))

        emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
        emotion_prediction = emotion_model.predict(reshaped_face)
        max_index = np.argmax(emotion_prediction[0])
        emotion = emotion_labels[max_index]
        emotions.append(emotion)

    return bounding_boxes, emotions

async def handle_client(websocket, path):
    try:
        async for message in websocket:
            bounding_boxes, emotions = await predict_emotion(base64.b64decode(message))

            bounding_box_str = ';'.join([f"{x1},{y1},{x2},{y2}" for (x1, y1, x2, y2) in bounding_boxes])
            emotions_str = ','.join(emotions)
            response = f"{emotions_str}|{bounding_box_str}"
            await websocket.send(response)

            await asyncio.sleep(0)
    except websockets.exceptions.ConnectionClosed:
        pass

start_server = websockets.serve(handle_client, "192.168.0.206", 5500)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

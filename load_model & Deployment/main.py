from fastapi import FastAPI, UploadFile, File
from PIL import Image
import numpy as np
import io
import tensorflow as tf

app = FastAPI()

# Load your pre-trained model
model = tf.keras.models.load_model('model.h5')

labels = ['air mineral', 'alat penerangan', 'jaket', 'jas hujan', 'kompas',
       'matras', 'p3k', 'sepatu', 'sleeping bag', 'tas', 'tenda',
       'trash bag']

@app.get("/")
async def welcome():
    return {"message" : "Selamat Datang di API ML"}


async def load_and_resize_image(file: UploadFile, size):

    # Load image
    image = Image.open(io.BytesIO(await file.read()))

    # Resize image
    image = tf.image.resize(image, [size, size])

    # Scale the tensor
    image = image / 255

    return np.array(image)

@app.post("/predict")
async def predict(file: UploadFile):
    image = await load_and_resize_image(file, 224)
    pred = model.predict(tf.expand_dims(image, axis=0))
    label_prediction = labels[pred[0].argmax()]
    return {"prediction" : label_prediction}
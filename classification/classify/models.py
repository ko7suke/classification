import base64
import os
import io
import numpy as np

import tensorflow.compat.v1 as tf
from PIL import Image
from django.db import models
from tensorflow.keras.models import load_model

graph = tf.get_default_graph()
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'


class Classify(models.Model):
    image = models.ImageField(upload_to='images')

    def classify(self):
        IMAGE_SIZE = 224
        MODEL_FILE_PATH = './classify/classification_models/vgg16_transfer_gender.h5'
        labels = ["man", "woman"]
        global graph

        with graph.as_default():
            model = load_model(MODEL_FILE_PATH)
            img_data = self.image.read()
            img_bin = io.BytesIO(img_data)

            image = Image.open(img_bin)
            image = image.convert("RGB")
            image = image.resize((IMAGE_SIZE, IMAGE_SIZE))

            data = np.asarray(image) / 255.0
            X = [data]
            X = np.asarray(X)

            result = model.classify([X])[0]
            classified = result.argmax()
            percentage = int(result[classified] * 100)

            return labels[classified], percentage

    def image_src(self):
        with self.image.open() as img:
            base64_img = base64.b64encode(img.read()).decode()
            return 'data:' + img.file.content_type + ';base64,' + base64_img


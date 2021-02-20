import numpy as np
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.python.keras.utils import np_utils
from tensorflow.python.keras.applications import VGG16

MODEL_NAME = "your_model"
CLASSES = ["man", "woman"]
NUM_CLASSES = len(CLASSES)
IMAGE_SIZE = 224
DATA_PATH = '../data_generator/data/output/image_files/imagefiles_224.npy'

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = np.load(DATA_PATH, allow_pickle=True)
    y_train = np_utils.to_categorical(y_train, NUM_CLASSES)
    y_test = np_utils.to_categorical(y_test, NUM_CLASSES)
    X_train = X_train.astype("float") / 255.0
    X_test = X_test.astype("float") / 255.0

    # モデルの定義
    model = VGG16(weights='imagenet', include_top=False, input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3))
    top_model = Sequential()
    top_model.add(Flatten(input_shape=model.output_shape[1:]))
    top_model.add(Dense(256, activation='relu'))
    top_model.add(Dropout(0.5))
    top_model.add(Dense(NUM_CLASSES, activation='softmax'))

    model = Model(inputs=model.input, outputs=top_model(model.output))
    model.summary()

    for layer in model.layers[:15]:
        layer.trainable = False

    opt = Adam(lr=0.0001)
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    model.fit(X_train, y_train, batch_size=32, epochs=17)

    score = model.evaluate(X_test, y_test, batch_size=32)

    model.save(f"./models/{MODEL_NAME}.h5")

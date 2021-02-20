from PIL import Image
import glob
import numpy as np
from sklearn import model_selection

IMAGE_FILE_NAME = "your_image _file_name"
CLASSES = ["man", "woman"]
IMAGE_SIZE = 224
X = []
Y = []

if __name__ == '__main__':
    for index, class_label in enumerate(CLASSES):
        photos_dir = "./data/input/" + class_label
        files = glob.glob(photos_dir + "/*.jpg")
        for i, file in enumerate(files):
            image = Image.open(file)
            image = image.convert("RGB")
            image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
            data = np.asarray(image)
            X.append(data)
            Y.append(index)

    X = np.array(X)
    Y = np.array(Y)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
    xy = (X_train, X_test, y_train, y_test)
    np.save(f"./data/output/image_files/{IMAGE_FILE_NAME}.npy", xy)

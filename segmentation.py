import cv2
import numpy as np
from Model import Model, DecoderType
from preprocess import preprocess, Batch 

def read_model():
    return Model(open('./model/charList.txt').read(), mustRestore=True)

def read_image(path):
    return cv2.imread('/home/' + path)

def to_lines (image):
    linesList = []

    # grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # binary
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # dilation
    kernel = np.ones((5, 900), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)

    # find contours
    ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

    for i, ctr in enumerate(sorted_ctrs):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)

        # Getting ROI
        roi = image[y:y + h, x:x + w]

        # show ROI
        linesList.append(roi)

    return reversed(linesList)

def to_words (image):

    wordList = []

    # grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # binary
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # dilation
    kernel = np.ones((5, 35), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)

    # find contours
    ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

    for i, ctr in enumerate(sorted_ctrs):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)

        # Getting ROI
        roi = image[y:y + h, x:x + w]

        # show ROI
        roi= cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        if roi.shape > (50,50) :
            wordList.append(roi)

    return wordList


def result (fnImg, model):

	"recognize text in image provided by app"
	img = preprocess(fnImg, Model.imgSize)

	batch = Batch(None, [img])
	(recognized, probability) = model.inferBatch(batch, True)

	return recognized[0], probability[0]


# reference - https://machinelearningmastery.com/use-pre-trained-vgg-model-classify-objects-photographs/
import os
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from natsort import natsorted, ns

# load the VGG16 model
model = VGG16()

# # load the image
# image = load_img('modified5.jpg', target_size=(224,224))
#
# # covert the images pixels to numpy array
# image = img_to_array(image)
#
# #reshape the image data -- [ not sure why we are doing this????]
# image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
#
# #prepare image for the VGG16 model
# image = preprocess_input(image)
#
# #make a prediction
# yhat = model.predict(image)
#
# #print the prediction
# label = decode_predictions(yhat)
# label = label[0][0]
# print('%s (%.2f%%)' % (label[1], label[2]*100))

def predict(img):
    # load the image
    image = load_img(img, target_size=(224, 224))

    # covert the images pixels to numpy array
    image = img_to_array(image)

    # reshape the image data -- [ not sure why we are doing this????]
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

    # prepare image for the VGG16 model
    image = preprocess_input(image)

    # make a prediction
    yhat = model.predict(image)

    # print the prediction
    label = decode_predictions(yhat)
    label = label[0][0]
    print('%s (%.2f%%)' % (label[1], label[2] * 100))

image_path ='/Users/Jagan/PycharmProjects/XAI/VGG16'

for root, sub_dirs, files in os.walk(image_path):
    for f in files:
        if '.jpg' in f or '.png' in f:
            print('------Now Predicting for -----', f)
            predict(f)

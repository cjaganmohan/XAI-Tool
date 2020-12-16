# reference - https://machinelearningmastery.com/use-pre-trained-vgg-model-classify-objects-photographs/
import argparse
import os
import os
import pdb
import shutil
import sys
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from natsort import natsorted, ns

reload(sys)
sys.setdefaultencoding('ISO-8859-1')

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
    #print('%s (%.2f%%)' % (label[1], label[2] * 100))
    #prediction = str(label[1]) + ', '+str(round(label[2]*100,2))
    prediction = str('%s,(%.2f%%)' % (label[1], label[2] * 100))
    return prediction

def start_prediction(image_path, original_prediction):
    test_images = []
    for root, sub_dirs, files in os.walk(image_path):
        for f in files:
            if '.jpg' in f or '.png' in f or '.JPEG' in f:
                test_images.append(os.path.join(root, f))

    test_images = natsorted(test_images)
    for image in test_images:
        predicted_label = predict(image).split(',')[0].strip()  # spliting the prediction output
        if predicted_label == original_prediction:
            print str(image.rsplit('/', 1)[1]) + ' --> ' + predict(image),',fail'
        else:
            print str(image.rsplit('/', 1)[1]) + ' --> ' + predict(image),',pass'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_location', type=str)
    parser.add_argument('--original_prediction', type=str)
    #parser.add_argument('--file_type', type=str)  # {'Baseline', 'Individual_transformation','2-way'}
    #parser.add_argument('--output_path', type=str)

    args, unknown = parser.parse_known_args()
    #print 'Calling the VGG16 model now '
    #print args.image_location, #args.group, args.file_type, args.output_path
    start_prediction(args.image_location, args.original_prediction) #, args.group, args.file_type, args.output_path)
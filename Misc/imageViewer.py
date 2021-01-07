import argparse
import glob
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
from natsort import natsorted


def displayImage(imageDirectory):
    images = []
    targetLocation = imageDirectory + '/*.jpg'
    print targetLocation
    for img_path in glob.glob(targetLocation):
        images.append(mpimg.imread(img_path))


    plt.figure(figsize=(20, 10))
    columns = 5
    for i, image in enumerate(images):
        plt.subplot(len(images) / columns + 1, columns, i + 1)
        plt.imshow(image)
        plt.title('Test case: '+ str(i))
    #plt.show()
    plt.savefig('/Users/Jagan/Desktop/image3104_initial_test_cases.jpg', dpi=300)



    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_directory', type=str)
    
    args, unknown = parser.parse_known_args()
    displayImage(args.image_directory)
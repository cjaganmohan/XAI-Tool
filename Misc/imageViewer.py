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
        print img_path
        images.append(mpimg.imread(img_path))

    
    plt.figure(figsize=(20, 20))
    #columns = 5
    columns = 3
    for i, image in enumerate(images):
        #print image
        plt.subplot(len(images) / columns + 1, columns, i + 1)
        plt.imshow(image)
        #plt.title('Test case: '+ str(i))
    #plt.show()
    #plt.savefig('/Users/Jagan/Desktop/explanations2.jpg', dpi=300)
    plt.savefig('/Users/Jagan/Desktop/explanations2.jpg', dpi=300)
    # new logic b
    # plt.gca().set_axis_off()
    # plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
    #         hspace = 0, wspace = 0)
    # plt.margins(0,0)
    # plt.gca().xaxis.set_major_locator(plt.NullLocator())
    # plt.gca().yaxis.set_major_locator(plt.NullLocator())
    # plt.savefig("/Users/Jagan/Desktop/explanations2.jpg", bbox_inches = 'tight',
    # pad_inches = 0)
    # new logic e


    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_directory', type=str)

    args, unknown = parser.parse_known_args()
    displayImage(args.image_directory)
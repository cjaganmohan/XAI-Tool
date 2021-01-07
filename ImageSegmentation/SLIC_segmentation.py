# reference: https://www.pyimagesearch.com/author/adrian/
import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.segmentation import mark_boundaries
from skimage.segmentation import slic
from skimage.util import img_as_float



def generate_segments(imageLocation):
    image = cv2.imread(imageLocation)
    segments = slic(img_as_float(image), n_segments=25, sigma=5)

    fig = plt.figure("Superpixels")
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), segments))
    plt.axis("off")
    plt.show()

    print(np.unique(segments))

    # To mask
    #mask = np.zeros(image.shape[:2], dtype='uint8')
    #
    # mask[segments == 0] = 255
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Applied", cv2.bitwise_and(image, image, mask = mask))
    # cv2.waitKey(0)
    #
    #
    # mask[segments == 7] = 255
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Applied", cv2.bitwise_and(image, image, mask = mask))
    # cv2.waitKey(0)

    # for (i, segVal) in enumerate(np.unique(segments)):
    #     print('[x] inspecting segment %d' % (i))
    #     mask = np.zeros(image.shape[:2], dtype='uint8')
    #     mask[segments == segVal] = 255
    #     # mask[segments == segVal] = 0
    #
    #     cv2.imshow("Mask", mask)
    #     cv2.imshow("Applied", cv2.bitwise_and(image, image, mask=mask))
    #     cv2.waitKey(0)

    mask = np.zeros(image.shape[:2], dtype='uint8')
    #masked_segments = [0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,21]
    masked_segments = [1,4,5,6,7,8,9,10,11,12,13,17,18,21]
    #masked_segments = [9,14]
    output_file_destination = '/Users/Jagan/Desktop/Image4837_failure_inducing_combination_explainer_new'+str(masked_segments)+'.jpg'
    for i in np.unique(segments):
        print i
        if i not in masked_segments:
            print i
            mask[segments == i] = 255
            cv2.imshow('Modified_Image', cv2.bitwise_and(image, image, mask=mask))
            cv2.waitKey(0)
    cv2.imwrite(output_file_destination, cv2.bitwise_and(image, image, mask=mask))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str)

    args, unknown = parser.parse_known_args()
    generate_segments(args.image)
#https://stackoverflow.com/questions/51249781/using-regionprops-in-python
from skimage.io import imread, imshow
from skimage.filters import gaussian, threshold_otsu
from skimage import measure, data, io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import cv2
from skimage.color import label2rgb
from PIL import Image
import numpy as np
import shutil
import os
import glob
from skimage.exposure import rescale_intensity
from skimage.morphology import reconstruction
import numpy as np
import rotate_image

def grain_extract(img):

    shutil.rmtree('extracted_grains')
    os.mkdir('extracted_grains')
    shutil.rmtree('extracted_grains_rgb')
    os.mkdir('extracted_grains_rgb')

    original = imread(img)

    gray_image = rgb2gray(original)

    thresh = threshold_otsu(gray_image)
    o = gray_image > thresh

    blurred = gaussian(o, sigma=.8)
    binary = blurred > threshold_otsu(blurred)

    seed = np.copy(binary)
    seed[1:-1, 1:-1] = binary.max()
    mask = binary
    filled = reconstruction(seed, mask, method='erosion')

    labels = measure.label(filled)
    props = measure.regionprops(labels)

    i = 1

    for prop in props:
        if prop.area < 200 :
            continue
        #print('grain',i,': Size -> ',prop.area)
        a, b, c, d = prop.bbox
        #io.imshow(original[a:c, b:d])
        #plt.show()
        plt.imsave('extracted_grains/' + str(i) + '.jpg', prop.image, cmap=plt.cm.gray)
        plt.imsave('extracted_grains_rgb/' + str(i) + '.jpg', original[a:c, b:d], cmap=plt.cm.gray)
        i += 1

    fd = rotate_image.rotate_img()
    return fd

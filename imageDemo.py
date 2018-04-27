import numpy as np


class LinearNonLinearOperation:
    def __init__(self):
        print("Image Operation class called")

    def srgb2lin(self, img, gpower):
        """
        :param img: the image passed by the user
        :param gpower: the power passed by the main function
        :return: the linear image (backward gamma)
        """
        # constants
        t = 0.04045
        a = 0.055

        # image normalized and converted to floating point
        img = img.astype(np.float32)/255.0

        # placeholder linear image
        img_lin = np.zeros(img.shape)

        # srgb non-linearity to linear conversion and back to uint8
        img_lin[img < t] = np.divide(img[img < t], 12.92)
        img_lin[img > t] = np.power(np.divide((img[img > t] + a), (1 + a)), gpower)

        img_lin = np.multiply(img_lin, 255.0)
        img_lin = img_lin.astype(np.uint8)

        return img_lin

    def lin2srgb(self, img, gpower):
        """
        :param img: the image passed by the user
        :param gpower: the power passed by the main function
        :return: the sRGB non-linear image (backward gamma)
        """
        # constants
        t = 0.0031308
        a = 0.055

        # image normalized and converted to floating point
        img = img.astype(np.float32) / 255.0

        # placeholder srgb non-linear image
        img_srgb = np.zeros(img.shape)

        # linear to srgb non-linearity and back to uint8
        img_srgb[img < t] = np.multiply(img[img < t], 12.92)
        img_srgb[img > t] = np.power(np.multiply(img[img > t], (1+a)), (1/gpower)) - a

        img_srgb = np.multiply(img_srgb, 255.0)
        img_srgb = img_srgb.astype(np.uint8)

        return img_srgb

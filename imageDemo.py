"""
Copyright © 2018, Ratnajit Mukherjee.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors
   may be used to endorse or promote products derived from this software without
   specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import numpy as np


class LinearNonLinearOperation(object):

    @staticmethod
    def srgb2lin(img, gpower):
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

    @staticmethod
    def lin2srgb(img, gpower):
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

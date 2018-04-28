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

from imageDemo import LinearNonLinearOperation as imgop
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import numpy as np
import argparse
import imageio


class GammaCurveDemo:
    def __init__(self):
        print("THIS IS A GAMMA CURVE DEMO USING NUMPY AND MATPLOTLIB")

    def drawGammaCurve(self):
        """
        Function to plot standard Gamma curves (forward and backward) for g = 2.2, 2.4 and 2.6 respectively
         2.2 = bright light
         2.4 = ambient lighting temp
         2.6 = dark lighting conditions
        :return: <none>
        """
        x_space = np.linspace(0.0, 1.0, 4096)

        plt.figure(1)
        for gpower, gcolor in zip([2.2, 2.4, 2.6], ['red', 'green', 'blue']):
            fwd_gamma_space = np.power(x_space, (1/gpower))
            bwd_gamma_space = np.power(x_space, gpower)

            plt.plot(x_space, fwd_gamma_space, label="Gamma = 1/"+str(gpower), color=gcolor)
            plt.plot(x_space, bwd_gamma_space, label="Gamma = "+str(gpower), linestyle='-.', color=gcolor)

        plt.plot(x_space, x_space, label="linear", color="black")
        plt.legend()
        plt.xlabel("Input Linear Space")
        plt.ylabel("Output non-linear Space")
        plt.title("Power Curve Comparison")
        plt.grid()
        plt.show()
        return

    def drawImagePlot(self, fwdGammaArr, bwdGammaArr, input_image):
        fig = plt.figure(2)
        rows = 2
        columns = 4

        gs = GridSpec(rows, columns)

        """
        *************************************************************************
        This the most ridiculous way of plotting images as subplots
        Have to figure out a way to do this custom grid and yet run it in a loop
        *************************************************************************
        """

        ax1 = plt.subplot(gs.new_subplotspec((0, 0), rowspan=2, colspan=1))
        ax1.imshow(input_image)
        ax1.set_xlabel("Input Image")
        ax1.set_xticks([])
        ax1.set_yticks([])

        ax2 = plt.subplot(gs.new_subplotspec((0, 1), colspan=1))
        ax2.imshow(fwdGammaArr[:, :, :, 0])
        ax2.set_xlabel("Gamma = "+str(1/2.2))
        ax2.set_xticks([])
        ax2.set_yticks([])

        ax3 = plt.subplot(gs.new_subplotspec((0, 2), colspan=1))
        ax3.imshow(fwdGammaArr[:, :, :, 1])
        ax3.set_xlabel("Gamma = " + str(1 / 2.4))
        ax3.set_xticks([])
        ax3.set_yticks([])

        ax4 = plt.subplot(gs.new_subplotspec((0, 3), colspan=1))
        ax4.imshow(fwdGammaArr[:, :, :, 2])
        ax4.set_xlabel("Gamma = " + str(1 / 2.6))
        ax4.set_xticks([])
        ax4.set_yticks([])

        ax5 = plt.subplot(gs.new_subplotspec((1, 1), colspan=1))
        ax5.imshow(bwdGammaArr[:, :, :, 0])
        ax5.set_xlabel("Gamma = " + str(2.2))
        ax5.set_xticks([])
        ax5.set_yticks([])

        ax6 = plt.subplot(gs.new_subplotspec((1, 2), colspan=1))
        ax6.imshow(bwdGammaArr[:, :, :, 1])
        ax6.set_xlabel("Gamma = " + str(2.4))
        ax6.set_xticks([])
        ax6.set_yticks([])

        ax7 = plt.subplot(gs.new_subplotspec((1, 3), colspan=1))
        ax7.imshow(bwdGammaArr[:, :, :, 2])
        ax7.set_xlabel("Gamma = " + str(2.6))
        ax7.set_xticks([])
        ax7.set_yticks([])

        """
        ***********************************************
            Set plot title and show the images
        ***********************************************
        """

        fig.suptitle("Gamma Curve - Image Demo")
        plt.show()

    def gammaCurveImageDemo(self, img_path):
        """
        Function to demonstrate the effects of 3 gamma curves with both forward and backward gamma correction
        :param img_path: the path of the image to be processed
        :return: the final subplots showing the original and gamma corrected images for comparison

        NOTE: We demonstrate the use static methods imported from the class LinearNonLinearOperation allowing
        function call without instantiating the class
        """
        img = imageio.imread(img_path)

        # First convert the image into a standard linear image
        img_lin_base = imgop.srgb2lin(img, gpower=2.4)

        # Create 2 4D arrays for the gamma-corrected images
        fwdGammaImg = np.zeros((img.shape[0], img.shape[1], img.shape[2], 3), dtype=np.uint8)
        bwdGammaImg = np.zeros((img.shape[0], img.shape[1], img.shape[2], 3), dtype=np.uint8)

        # Gamma power list
        gpower_list = [2.2, 2.4, 2.6]

        # using the indexing we serve two purposes (1: iterate over the list and 2: iterate over the list)
        for idx in range(0, len(gpower_list)):
            fwdGammaImg[:, :, :, idx] = imgop.lin2srgb(img=img_lin_base, gpower=gpower_list[idx])
            bwdGammaImg[:, :, :, idx] = imgop.srgb2lin(img=img, gpower=gpower_list[idx])

        # draw the final plot
        self.drawImagePlot(fwdGammaArr=fwdGammaImg, bwdGammaArr=bwdGammaImg, input_image=img)
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="The absolute system path of the input image", type=str)
    args = parser.parse_args()

    if args.input:
        input_path = args.input
    else:
        print("No input image argument has been passed. Reverting to demo image.")
        input_path = 'mountain.jpg'

    gDemo = GammaCurveDemo()
    gDemo.drawGammaCurve()
    gDemo.gammaCurveImageDemo(input_path)

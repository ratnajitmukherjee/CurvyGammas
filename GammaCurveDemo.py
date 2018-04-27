from imageDemo import LinearNonLinearOperation
from matplotlib.gridspec import GridSpec
import numpy as np
import matplotlib.pyplot as plt
import imageio


class GammaCurveDemo:
    def __init__(self):
        print("THIS IS A GAMMA CURVE DEMO USING NUMPY AND MATPLOTLIB")

    def drawGammaCurve(self):
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

        fig.suptitle("Gamma Curve - Image Demo")

        plt.show()

    def gammaCurveImageDemo(self, img_path):
        img = imageio.imread(img_path)

        # Call the image operation class
        imgop = LinearNonLinearOperation()

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
    gDemo = GammaCurveDemo()
    gDemo.drawGammaCurve()
    gDemo.gammaCurveImageDemo('mountain.jpg')
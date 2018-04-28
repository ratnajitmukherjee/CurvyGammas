![PowerCurve](PowerCurve.jpeg)

# CurvyGammas
This is a demo project showing the effect of Gamma Curves on Images

At first the typical gamma=2.2, 2.4 and 2.6 and their inverses i.e. gamma = (1/2.2), (1/2.4) and (1/2.6), respectively are plotted to show the sRGB non-linearity of the spaces.

# Libraries used in this program
1) numpy
2) matplotlib
3) imageio
4) argparse

# Installation
1) pip install numpy OR pip3 install numpy
2) pip install matplotlib OR pip3 install matplotlib
3) pip install imageio OR pip3 install imageio

# Additional notes:
Image read-write operation conducted via imageio library instead of OpenCV since handling RGB instead of BGR (as in OpenCV) is easier

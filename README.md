# Material Recommender
A Blender 2.80 add-on that helps you generate materials.

This is a Blender extension that appears as a panel in the Properties editor, under the Materials section.
It is able to generate the preview of a material using neural rendering.
It is based on the paper here: https://users.cg.tuwien.ac.at/zsolnai/gfx/gaussian-material-synthesis/
Each material is an animation in which the light source moves for better assessment of the material.

Features*:
- view materials animations in VSE
- export the materials for usage in the scene
- generates a list of preferences that the user can score
- learn the preferences of the user in a one-round or multi-round fashion.
- recommend materials similar to the ones rated
- discover new materials in the preferences space based on high scoring materials

* a material is a structure that simulates a material in the context of the extension; to generate a true blender material one can export the extension material


Installation guide:
Minimul Python version: 3.70
The extension uses the following packages:
- numpy
- scipy
- matplotlib
- climin
- GPy
- keras

Consider using Anaconda for managing packages.
The keras back-end user for developing this extension is tensorflow-gpu.
Notes and errors when installing:
1) At the moment of writing, GPy is not available for Python 3.7. Details on how to make it work here (vmarkovtsev's response): https://github.com/SheffieldML/GPy/issues/649
2) In order to link the anaconda environment to Blender, see here: https://blender.stackexchange.com/a/51800
3) (After note 2) Error when importing numpy, see here: https://stackoverflow.com/a/56009839
4) (After note 2) Error when importing keras/GPy, I modified the regex checker in platform\[s\].py in order to be compatible; see here: https://stackoverflow.com/a/19105436

# OMNI-P2x

OMNI-P2x is a universal neural network potential for excited-state simulations. It approaches TD-DFT quality predictions, e.g., for UV/vis absorption spectra at a fraction of cost. OMNI-P2x is faster and more accurate than semiempirical QM methods such as TD-DFTB.

# Usage
You can use OMNI-P2x in [MLatom](https://github.com/dralgroup/mlatom) via [Aitomic](http://mlatom.com/aitomic) add-on, either online via a web browser or locally on your computer. Below are the details.

## Online via a web browser
It is convenient to do calculations with OMNI-P2x via a web browser, where two options are available:

- [Aitomistic Hub](https://aitomistic.xyz) - provides a convenient web interface for performing simulations, with limited free resources mainly for demo purposes (recommended).
- [XACS cloud](https://XACScloud.com) - a less convenient but a time-proven solution with generous free computational resources for academic users.

## Locally
The model weights are available in this repository under the folder `model_weights`. You can adjust MLatom's source code as described in the preprint (see citation below) to load the weights and use them. Alternatively, you can request a ready-to-use implementation in the Aitomic package (which builds upon MLatom by providing add-ons for unpublished features like this one), it is free for academic users subject to a license agreement. The source code is planned to be openly released in MLatom under the MIT license upon the acceptance of the manuscript in the journal of our choice.

## Tutorial
Here we describe how to use OMNI-P2x, either online or locally.

# Citation
- Mikolaj Martyka, Xin-Yu Tong, Joanna Jankowska, and Pavlo O. Dral. *OMNI-P2x: A Universal Neural Network Potential for Excited-State Simulations*. **2025**, *to be submitted*.

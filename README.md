# DLHub Publication Example: Black Holes Mergers

Publication code for a model to infer properties of black holes from gravitational waves

## Installation

Our environment is defined using Anaconda. Install it by calling:

`conda env create --file environment.yml`

Then activate the environment following the instructions from Anaconda.
It will be similar to: `conda activate plb`d

## Publishing the Model

Call `python publish_model.py` after installing and activating the environment to publish the model.

It will send in a publication request to DLHub and prints the task ID to screen. 

**Note**: Contact us to get access to the Keras H5 file to be published.

## Performing Inference Requests

Run the published model by calling `python run_model.py`. 
This script contains options to change how many waveform samples are generated
and which version of the model on DLHub is used to perform the inference.

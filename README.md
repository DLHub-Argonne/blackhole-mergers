# DLHub Publication Example: Black Holes Mergers

Publication code for a model to infer properties of black holes from gravitational waves. Based on 
[work by Khan, Huerta, and Das from UIUC](https://arxiv.org/abs/2004.09524).

## Installation

Our environment is defined using Anaconda. Install it by calling:

`conda env create --file environment.yml`

Then activate the environment following the instructions from Anaconda.
It will be similar to: `conda activate plb`

## Publishing the Model

Call `python publish_model.py` after installing and activating the environment to publish the model.

It will send in a publication request to DLHub and prints the task ID to screen. 

**Note**: Contact us to get access to the Keras H5 file to be published.

## Performing Inference Requests

Run the published model by calling `python run_model.py`. 
This script contains options to change how many waveform samples are generated
and which version of the model on DLHub is used to perform the inference.

## Repository Structure

The repository is structured for easy publication to DLHub, where each file serves a specific purpose:

- `dlhub_app.py` defines an interface to the machine learning model that follows a common pattern in DLHub: a single function, `inference`, that provides an interface to the model. That function loads the model into a global variable so that it stays in memory between calls then executes the model. It also includes a main function so one can test the function without publishing it to DLHub.
  - There is a [pre-built Keras interfence function](https://dlhub-sdk.readthedocs.io/en/latest/servable-types.html#keras-models) for DLHub, but we opted to write our own to return specially-formated data (i.e., the inference results in a dictionary with their names).
- `environment.yml` specifies how to re-create the computational environment using [Anaconda's environment specification format](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file). DLHub understands this format and will use it when creating the model's container.
- `inference.ipynb` explains how to use the model in an interactive way that complements the API access provided by DLHub.
- `publish_model.py` builds a description for the model that fits DLHub's metadata format. We use the [DLHub SDK's utility functions](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) to reference the paper that describes this model, and give human-friendly labels to the model inputs and outputs.
- `run_model.py` illustrates how to run the model from DLHub. 

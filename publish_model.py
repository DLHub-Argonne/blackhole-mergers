"""Publish the script to DLHub"""

from dlhub_sdk.models.servables.python import PythonStaticMethodModel
from dlhub_sdk.utils.types import compose_argument_block
from dlhub_sdk.client import DLHubClient
from dlhub_app import inference
from argparse import ArgumentParser
from tensorflow.keras.models import load_model
import logging
import json
import os

# Make a logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Parse the user input
parser = ArgumentParser(description='''Publish model to DLHub''')
parser.add_argument('--test', help='Just test out the submission and print the metadata', action='store_true')
args = parser.parse_args()
logging.info(f'Starting publication')

# Load in the model
tf_model = load_model('model_19-0.00.h5')

# Write out the model description
model = PythonStaticMethodModel.from_function_pointer(inference)

#   Descriptions of the model interface
model.set_inputs('ndarray', 'Gravity waveform measurement', shape=tf_model.input_shape)
model.set_outputs('dict', 'Estimated of properties of merging black holes',
    properties={
        'q': compose_argument_block('list', 'Mass ratio', item_type='float'),
        's1': compose_argument_block('list', 'Spin of primary', item_type='float'),
        's2': compose_argument_block('list', 'Spin of primary', item_type='float'),
        'S_eff': compose_argument_block('list', 'Effective spin', item_type='float'),
        'chi': compose_argument_block('list', 'Effective spin parameter', item_type='float'),
    }
)

# Provenance information for the model
model.add_related_identifier("2004.09524", "arXiv", "IsDescribedBy")

#   DLHub searchable
model['datacite']['subjects'] = [{'subject': 'cosmology'}]
logging.info('Initialized model with generic metadata')

# Add the needed files
model.add_file('dlhub_app.py')
model.add_file('model_19-0.00.h5')
model.parse_repo2docker_configuration()

# Model name
model.set_name(f'binary_black_hole_mergers')
model.set_title(f'A deep learning model to characterize the signal manifold of quasi-circular, spinning, non-precessing binary black hole mergers')
logging.info(f'Defined model name: {model.name}')

#   Model provenance information
model.set_authors(['Khan, Asad', 'Huerta, E. A.', 'Das, Arnav'], [['University of Illinois at Urbana-Champaign']]*3)
logging.info('Added model-specific metadata')

# If desired, print out the metadata
if args.test:
    logging.info(f'Metadata:\n{json.dumps(model.to_dict(), indent=2)}')
    exit()

    
# Publish servable to DLHub

#   Make the client and submit task
client = DLHubClient(http_timeout=-1)
task_id = client.publish_servable(model)
logging.info(f'Started publication. Task ID: {task_id}')


from dlhub_sdk.client import DLHubClient
from argparse import ArgumentParser
import numpy as np
import logging

# Make a logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Make the client
client = DLHubClient()

# Parse CLI arguments
parser = ArgumentParser(description='Run the model')
parser.add_argument('--model', help='Name of the DLHub servable', type=str,
        default='loganw_globusid/binary_black_hole_mergers')
parser.add_argument('--test-size', help='Number of waveforms to test', type=int, default=1)
args = parser.parse_args()

# Make some test data
test_data = np.zeros((args.test_size, 101300, 1), dtype=int)
logging.info(f'Made {test_data.shape[0]} test samples')

# Run it through dlhub
logging.info(f'Made invokation to DLHub servable: {args.model}')
result = client.run(args.model, test_data.tolist())

print(result)

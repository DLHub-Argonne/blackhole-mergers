from dlhub_sdk.client import DLHubClient
from argparse import ArgumentParser
import numpy as np

# Make the client
client = DLHubClient()

# TODO (wardlt): Increase default size, make it easier to access
client._fx_client.DEFAULT_MAX_REQUEST_SIZE = 50 * 1024 ** 3

# Parse CLI arguments
parser = ArgumentParser(description='Run the model')
parser.add_argument('--model', help='Name of the DLHub servable', type=str,
        default='loganw_globusid/binary_black_hole_mergers')
parser.add_argument('--test-size', help='Number of waveforms to test', type=int, default=1)
args = parser.parse_args()

# Make some test data
test_data = np.random.uniform(size=(args.test_size, 101300, 1))

# Run it through dlhub
result = client.run(args.model, test_data)

print(result)

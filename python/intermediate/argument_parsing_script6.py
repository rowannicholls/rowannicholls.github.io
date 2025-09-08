import argparse

# Create command line argument parser
parser = argparse.ArgumentParser()
# Add positional arguments
parser.add_argument('message',)
parser.add_argument('number', type=int)
# Add optional arguments
parser.add_argument('--recipient', '-r')
# Parse arguments from terminal
args = parser.parse_args()
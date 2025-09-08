import argparse

# Create command line argument parser
parser = argparse.ArgumentParser(
    # Add a helpful description that will be displayed at the start of the help message
    description="A script that takes a text message and sends it to a recipient's phone.",
    # Add a helpful description that will be displayed at the end of the help message
    epilog='Written by rowannicholls.github.io'
)
# Add positional arguments
parser.add_argument(
    'message',
    help='The message that you want to be sent.'
)
parser.add_argument(
    'number', type=int,
    help='The phone number of the recipient'
)
# Add optional arguments
parser.add_argument(
    '--recipient', '-r',
    help='The name of the recipient.'
)
# Parse arguments from terminal
args = parser.parse_args()
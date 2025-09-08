import argparse

# Create command line argument parser
parser = argparse.ArgumentParser()
# Add optional arguments
parser.add_argument('--message', '-m')
parser.add_argument('--recipient', '-r')
# Parse arguments from terminal
args = parser.parse_args()

# Access the arguments
message = args.message
print(message)
recipient = args.recipient
print(recipient)
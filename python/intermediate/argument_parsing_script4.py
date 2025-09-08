import argparse

# Create command line argument parser
parser = argparse.ArgumentParser()
# Add positional argument
parser.add_argument('message')
# Parse arguments from terminal
args = parser.parse_args()

# Access the arguments
message = args.message
print(message)

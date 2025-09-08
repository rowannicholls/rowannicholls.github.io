import sys

if len(sys.argv) > 1:
    print('Data was received from the terminal')
    for argument in sys.argv[1:]:
        if argument == 'Option 1':
            print('Running the script as per Option 1')
        else:
            print('Running the script as per a different option')
else:
    print('Nothing was received from the terminal')

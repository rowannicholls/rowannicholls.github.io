"""Get the Isis flag status."""
import requests
from pathlib import Path
import pandas as pd

# Import the master data frame, or initialise it if it does not exist
path = Path('master.csv')
if path.exists():
    df = pd.read_csv(path)
else:
    df = pd.DataFrame()

# Make the API call
response = requests.get('https://ourcs.co.uk/api/flags/status/isis/')
# Isis Flag Page
# https://ourcs.co.uk/information/flags/isis/

# Check the status code
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
if response.status_code == 200:
    # 200 OK
    pass
else:
    # If the request was unsuccessful, print an error message
    raise ValueError(f'Error: {response.status_code} - {response.reason}')

# Check if the status has changed since the last check
this_call_date = response.json()['set_date']
if len(df) == 0:
    # The master data frame has just been initialised
    pass
else:
    # A previous entry exists
    most_recent_date = df.loc[len(df) - 1, 'set_date']
    if this_call_date == most_recent_date:
        # This data is not new
        raise SystemExit

# Add the received data as a row in the data frame if it is new
row = pd.DataFrame([response.json()])
df = pd.concat([df, row], ignore_index=True)
print(df)
df.to_csv('master.csv', index=False)

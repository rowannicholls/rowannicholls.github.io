"""Plot the Isis flag status."""
from datetime import datetime, timezone, timedelta
from pathlib import Path
import argparse
import os

import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd

# Change working directory to the folder containing the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Register Computer Modern fonts
font_dir = Path('../../fonts/cm-unicode-0.7.0')
for font in font_dir.glob('*.ttf'):
    fm.fontManager.addfont(str(font))

# Matplotlib font parameters
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['CMU Serif'],
    'mathtext.fontset': 'cm',
})


def cardinal_to_ordinal(cardinal):
    """Convert a cordinal number to an ordinal number."""
    if cardinal % 10 == 1:
        return f'{cardinal}st'
    elif cardinal % 10 == 2:
        return f'{cardinal}nd'
    elif cardinal % 10 == 3:
        return f'{cardinal}rd'
    else:
        return f'{cardinal}th'


# Create command-line argument parser
parser = argparse.ArgumentParser()
# Add optional arguments
parser.add_argument('--latest_only', '-l', action='store_true')
parser.add_argument('--path', '-p', default='master.csv')
# Parse arguments from terminal
args = parser.parse_args()

# Import data
df = pd.read_csv(args.path)
# Trim
cols = ['status_text', 'set_date']
df = df[cols]

# Convert 'set_date' column to datetime objects
df['set_date'] = pd.to_datetime(df['set_date'], format='ISO8601')

# Duplicate the colour column
df['colour'] = df['status_text']
# Convert colours to Matplotlib colours
df['colour'] = df['colour'].replace('Black', '#212121')
df['colour'] = df['colour'].replace('Red', '#E74C3C')
df['colour'] = df['colour'].replace('Amber', '#F0B23E')
df['colour'] = df['colour'].replace('Dark Blue', '#1C71A6')
df['colour'] = df['colour'].replace('Light Blue', 'lightblue')
df['colour'] = df['colour'].replace('Green', '#70A35E')
df['colour'] = df['colour'].replace('Grey', 'grey')

terms = [
    # (year, term, start of 0th Week, end of Peak Term)
    # ('2023', 'Hilary', '2023-01-08T00:00:00Z', '2023-02-25T23:00:00Z'),
    # ('2023', 'Trinity', '2023-04-16T00:00:00Z', '2023-05-27T23:00:00Z'),
    # ('2023', 'Michaelmas', '2023-10-01T00:00:00Z', '2023-11-25T23:00:00Z'),
    # ('2024', 'Hilary', '2024-01-07T00:00:00Z', '2024-03-02T23:00:00Z'),
    # ('2024', 'Trinity', '2024-04-14T00:00:00Z', '2024-05-25T23:00:00Z'),
    # ('2024', 'Michaelmas', '2024-10-06T00:00:00Z', '2024-11-30T23:00:00Z'),
    # ('2025', 'Hilary', '2025-01-12T00:00:00Z', '2025-03-01T23:00:00Z'),
    # ('2025', 'Trinity', '2025-04-20T00:00:00Z', '2025-05-31T23:00:00Z'),
    # ('2025', 'Michaelmas', '2025-10-05T00:00:00Z', '2025-11-29T23:00:00Z'),
    ('2026', 'Hilary', '2026-01-11T00:00:00Z', '2026-03-07T23:00:00Z'),
]

# Forward fill to either today or the next 9th week
latest_term = terms[-1]
# First day of 0th week
noughth_start = datetime.fromisoformat(latest_term[2])
# End of 9th week
ninth_end = noughth_start + timedelta(weeks=10) - timedelta(hours=1)
# Current datetime
now = datetime.now(timezone.utc)
# Append a new row with today's date or the end of 9th Week, whichever is
# later
if now > ninth_end:
    # If it is currently vacation time (ie after the end of the latest term)
    new_row_1 = {'set_date': ninth_end + timedelta(hours=1), 'colour': 'white'}
    new_row_2 = {'set_date': now, 'colour': 'white'}
else:
    # If it is currently term time (ie before the end of the latest term)
    new_row_1 = {'set_date': now, 'colour': 'white'}
    new_row_2 = {'set_date': ninth_end, 'colour': 'white'}
new_row_1 = pd.DataFrame(new_row_1, index=[0])
df = pd.concat([df, new_row_1], ignore_index=True)
new_row_2 = pd.DataFrame(new_row_2, index=[0])
df = pd.concat([df, new_row_2], ignore_index=True)

# Forward-fill the gaps in the data
df = df.rename(columns={'set_date': 'datetime'})
df = df.set_index('datetime')
df = df.resample('1h').ffill()
df.reset_index(inplace=True)

# Decide which terms to analyse
if args.latest_only:
    terms_to_analyse = terms[-1:]
else:
    terms_to_analyse = terms

# Iterate through the terms
for term in terms_to_analyse:
    year = term[0]
    term_name = term[1]
    # First day of 0th week
    noughth_start = datetime.fromisoformat(term[2])
    # End of Peak Term
    peak_term_end = datetime.fromisoformat(term[3])

    # End of 9th week
    ninth_end = noughth_start + timedelta(weeks=10) - timedelta(hours=1)
    # Start of Peak Term
    peak_term_start = noughth_start + timedelta(days=4)
    # Current datetime
    now = datetime.now(timezone.utc)

    # Extract Full Term
    bl = (df['datetime'] >= noughth_start) & (df['datetime'] <= ninth_end)
    full_term = df[bl].copy()

    # Extract Peak Term
    bl = (df['datetime'] >= peak_term_start) & \
        (df['datetime'] <= peak_term_end)
    peak_term = df[bl]
    # Remove the placeholder flag (the "white" flag")
    peak_term = peak_term[peak_term['colour'] != 'white']
    # Get the percentage of hours under each colour flag
    colour_counts = peak_term['status_text'].value_counts()
    colour_percentage = (colour_counts / len(peak_term)) * 100
    colour_percentage = colour_percentage.round(1)

    # Define the flag colours
    colours = [
        'Black', 'Red', 'Amber', 'Dark Blue', 'Light Blue', 'Green', 'Grey'
    ]
    # Export to external file
    with open(f'{year}_{term_name.lower()}_term.txt', 'w') as file:
        start = peak_term_start.date()
        end = peak_term_end.date()
        if now > peak_term_end:
            file.write(f'Percentage of Peak Term ({start} to {end} ')
            file.write('inclusive) under each flag:\n')
        else:
            file.write(f'Percentage of Peak Term ({start} to today) ')
            file.write('under each flag:\n')
        file.write('\n')
        file.write('| | % |\n')
        file.write('|---|:---:|\n')
        for colour in colours:
            if colour in colour_percentage.index:
                file.write(f'| {colour} | {colour_percentage[colour]} |\n')
            else:
                file.write(f'| {colour} | 0 |\n')
        file.write('\n')

    # Get the number of weeks since the start of 0th week
    ser = (full_term.loc[:, 'datetime'] - noughth_start).dt.days
    full_term.loc[:, 'oxford_week_number'] = ser // 7

    # Get ISO week number
    full_term['iso_week_number'] = full_term['datetime'].dt.isocalendar().week

    # Define the figure and axis
    fig, ax = plt.subplots(figsize=(6, 4), dpi=141)
    # Create a flag to indicate if we need to add the month in the first block
    month_in_first_block = True
    # Loop through each week
    for week_number, week_data in full_term.groupby('oxford_week_number'):
        # Plot rectangles for each hour
        for index, row in week_data.iterrows():
            # Convert datetime to days-since-epoch
            x = mdates.date2num(row['datetime'])
            # 1970-01-01 was a Thursday, so subtract 3 days to pretend it was a
            # Monday (which we will label as "Sunday")
            x = x - 3
            # Get only the fractions of the week
            x = x % 7
            # Plot the week number on the y-axis
            y = week_number
            # Plot with an offset so as to align with the centre of the labels
            x = x - 0.5
            y = y - 0.5

            width = 1 / 24  # each hour
            height = 1

            # Plot the rectangle
            rect = plt.Rectangle((x, y), width, height, color=row['colour'])
            ax.add_patch(rect)

            # Add the date as text in every 24th rectangle
            if index % 24 == 8:
                date_text = row['datetime'].strftime('%d').lstrip('0')
                ax.text(
                    # Align text horizontally in the rectangle
                    x + width / 2,
                    # Align text vertically in the rectangle
                    y + height / 1.3,
                    # The date as text
                    date_text,
                    # Horizontal alignment
                    ha='center',
                    # Vertical alignment
                    va='center',
                    # Font size
                    fontsize=6,
                    # Text color
                    color='w'
                )

            # Add the month name as text in the relevant rectangles
            if (row['datetime'].day == 1 or month_in_first_block):
                if row['datetime'].hour == 1:
                    month_text = row['datetime'].strftime('%B')
                    ax.text(
                        # Align text horizontally in the rectangle
                        x + width / 2,
                        # Align text vertically in the rectangle
                        y + height / 3.5,
                        # The date as text
                        month_text,
                        # Vertical alignment
                        va='center',
                        # Font size
                        fontsize=6,
                        # Text color
                        color='w',
                    )
                    month_in_first_block = False

            # Add "Peak Term Starts" text"
            if row['datetime'] == peak_term_start + timedelta(hours=1):
                ax.text(
                    x + width / 2, y + height * 0.60, 'Peak Term',
                    fontsize=5, color='w', fontstyle='italic',
                )
                ax.text(
                    x + width / 2, y + height * 0.85, 'Starts',
                    fontsize=5, color='w', fontstyle='italic',
                )

            # Add "Peak Term Ends" text"
            if row['datetime'] == peak_term_end + timedelta(hours=2):
                ax.text(
                    x + width / 2, y + height * 0.60, 'Peak Term',
                    fontsize=5, color='w', fontstyle='italic'
                )
                ax.text(
                    x + width / 2, y + height * 0.85, 'Ends',
                    fontsize=5, color='w', fontstyle='italic'
                )

    # Construct the x-axis so as to represent days of the week
    ax.set_xticks(range(7))
    labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_xlim(-0.5, 6.5)
    # Remove black lines on the major x-axis ticks
    ax.tick_params(axis='x', which='major', length=0)
    # Add minor ticks on the x-axis without labels
    ax.set_xticks([i + 0.5 for i in range(7)], minor=True)
    # Add grid lines
    ax.grid(axis='x', which='minor', linestyle='-')

    # Construct the y-axis so as to represent weeks
    start_week = int(full_term['oxford_week_number'].min())
    end_week = int(full_term['oxford_week_number'].max())
    num_weeks = end_week - start_week + 1
    ax.set_ylim(end_week + 0.5, start_week - 0.5)
    ax.set_yticks(range(start_week, end_week + 1))
    # Construct the week names
    week_names = [f'{cardinal_to_ordinal(i)} Week' for i in range(num_weeks)]
    ax.set_yticklabels(week_names, fontsize=8)
    # Remove black lines on the major y-axis ticks
    ax.tick_params(axis='y', which='major', length=0)
    # Add minor ticks on y-axis without labels
    ax.set_yticks([i + 0.5 for i in range(num_weeks)], minor=True)
    # Add grid lines
    ax.grid(axis='y', which='minor', linestyle='-')

    # Set title and labels
    st = f'OURCs Isis Flag\n{term_name} Term {year}'
    plt.title(st, fontsize=12)
    plt.savefig(f'{year}_{term_name.lower()}_term.png')

"""Plot the Isis flag status."""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.dates as mdates
from datetime import datetime, timezone, timedelta
import platform
import argparse

if platform.system() == 'Linux':
    # Set the Matplotlib backend to one that is compatible with Wayland
    plt.switch_backend('Agg')

# Use LaTeX for graphs' text
plt.rc('text', usetex=True)
# Use the serif font
plt.rc('font', family='serif')
# Be able to use Greek symbols in text mode
plt.rc('text.latex', preamble=r'\usepackage{textgreek}')


def cardinal_to_ordinal(cardinal):
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
    ('2023', 'Hilary', '2023-01-08T00:00:00Z', '2023-02-25T23:00:00Z'),
    ('2023', 'Trinity', '2023-04-16T00:00:00Z', '2023-05-27T23:00:00Z'),
    ('2023', 'Michaelmas', '2023-10-01T00:00:00Z', '2023-11-25T23:00:00Z'),
    ('2024', 'Hilary', '2024-01-07T00:00:00Z', '2024-03-02T23:00:00Z'),
    ('2024', 'Trinity', '2024-04-14T00:00:00Z', '2024-05-25T23:00:00Z'),
    ('2024', 'Michaelmas', '2024-10-06T00:00:00Z', '2024-11-30T23:00:00Z'),
    ('2025', 'Hilary', '2025-01-12T00:00:00Z', '2025-03-01T23:00:00Z'),
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
    bl = (df['datetime'] >= peak_term_start) & (df['datetime'] <= peak_term_end)
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
        if now > peak_term_end:
            file.write('Percentage of Peak Term* under each flag:\n')
        else:
            file.write('Percentage of Peak Term* - so far - under each flag:')
            file.write('\n')
        file.write('\n')
        file.write('| | % |\n')
        file.write('|---|:---:|\n')
        for colour in colours:
            if colour in colour_percentage.index:
                file.write(f'| {colour} | {colour_percentage[colour]} |\n')
            else:
                file.write(f'| {colour} | 0 |\n')
        file.write('\n')
        start = peak_term_start.date()
        end = peak_term_end.date()
        file.write(f'*{start} to {end} inclusive')

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
                    # first_day = (index == week_data.index[0] + 12) and (week_number == 0)
                    # print(row['datetime'], row['datetime'].strftime('%H'))
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
    st = f"""OURCs Isis Flag
    {term_name} Term {year}"""
    plt.title(st, fontsize=12)
    plt.savefig(f'{year}_{term_name.lower()}_term.png')

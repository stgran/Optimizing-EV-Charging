import pandas as pd
import sqlite3
import logging

'''
METHODS:
- load_dataset(csv_path): imports the csv data.
- clean_dataset(dataset, column_names=None): cleans the dataset. For more info, see README.md.
- adjust_datetime(datetime_str): adjusts the datetime format.
- init_db(db_path, table_name): initializes an SQLite database.
- insert_data(db_path, dataset, table_name, column_name): inserts data into an SQLite database.
'''

def load_dataset(csv_path):
    # Load the data using Pandas
    dataset = pd.read_csv(csv_path)
    return dataset

def clean_dataset(dataset, column_names=None):
    '''
    During cleaning, weremove columns that are full of n/e and check for n/a presence.
    
    DROP N/E COLUMNS
    We remove columns that are full of 'n/e' because this type of production does
    not occur in the Eastern Denmark bidding zone.
    These columns are easily identifiable because they have only one unique value: 'n/e'

    CHECK FOR N/A PRESENCE
    'n/a' means that that type of electricity production should be occurring but for some reason,
    the data is missing. For now, we flag columns that have a higher 'n/a' density than 10%.

    ADJUST MTU FORMAT
    The imported MTU data is set up as 'dd-mm-yyyy HH:MM - dd-mm-yyyy HH:MM'.
    We change this format to 'yyyy-mm-dd HH:MM:SS.SSS', which is recognizable as a datetime
    by SQLite.

    FUTURE IMPROVEMENTS
    With more time and in a situation where we are using real-time data, not just historical,
    I would set up a system to check if currently 'n/e' production types start getting
    produced or vice versa.
    '''
    
    # DROP N/E COLUMNS and CHECK FOR N/A
    drop_columns = ['Area'] # List of columns to drop
    for column in dataset: # Iterate over the columns
        unique_vals = dataset[column].unique()
        unique_vals = [unique_val for unique_val in unique_vals if pd.isna(unique_val) == False]

        # Identifying 'n/e' columns
        if len(unique_vals) == 1 and unique_vals[0] == 'n/e': # Check if the column only contains 'n/e'
            drop_columns.append(column) # Track these columns for dropping

        # Flagging columns with a high density of 'n/a'
        if 'n/a' in unique_vals:
            value_counts = dataset[column].value_counts()
            if value_counts.loc['n/a'] > (dataset[column].size * .1):
                na_density = value_counts.loc['n/a']/dataset[column].size
                logging.info(f'n/a density: {na_density}')
    dataset.drop(drop_columns, axis=1, inplace=True) # Drop those target columns

    # Adjust datetime format to be read as datetime by SQLite
    dataset['MTU'] = dataset['MTU'].apply(lambda datetime: adjust_datetime(datetime))

    if column_names:
        dataset.rename(columns=column_names, inplace=True)
    return dataset

def adjust_datetime(datetime_str):
    '''
    Function to adjust the original datetime format to be readable as a datetime
    by SQLite.
    Switches from hour-hour+1 format to hour timestamp.
    Loses timezone. In the future, this strategy could be confusing when being
    used on multiple timezones and would need to be adjusted.
    '''
    YYYY = datetime_str[6:10] # Select the year
    MM = datetime_str[3:5] # Select the month
    DD = datetime_str[:2] # Select the day
    HH = datetime_str[11:13] # Select the hour
    min_sec = '00:00.000'
    adjusted_datetime = f'{YYYY}-{MM}-{DD} {HH}:{min_sec}' # Put them together in a new format
    return adjusted_datetime

def init_db(db_path, table_name):
    # Query to create a table
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        Area TEXT NOT NULL,
        MTU TEXT NOT NULL PRIMARY KEY,
        Biomass REAL,
        FossilGas REAL,
        FossilHardCoal REAL,
        FossilOil REAL,
        Solar REAL,
        Waste REAL,
        WindOffshore REAL,
        WindOnshore REAL
        );
    '''

    # Initiate SQLite database connection object
    db_conn = sqlite3.connect(db_path)
    # If this db does not yet exist, initiating the connection object
    # actually creates it as a new database.

    # Establish cursor object so we can execute SQL code on the db.
    c = db_conn.cursor()

    # Execute the query
    c.execute(create_table_query)

def insert_data(db_path, dataset, table_name, column_name):
    # Query to add a column
    add_column_query = f'''
    ALTER TABLE {table_name} ADD COLUMN
        {column_name} REAL GENERATED ALWAYS AS (Biomass + FossilGas + FossilHardCoal + FossilOil + Solar + Waste + WindOffshore + WindOnshore);
    '''
    
    # Initiate SQLite database connection object
    db_conn = sqlite3.connect(db_path)

    # Write the dataset into the chosen SQLite table
    dataset.to_sql(table_name, db_conn, if_exists='replace', index=False)

    # Establish cursor object so we can execute SQL code on the db.
    c = db_conn.cursor()

    # Execute the query, adding a generated column that calculates total production
    c.execute(add_column_query)
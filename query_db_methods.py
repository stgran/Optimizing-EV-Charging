import pandas as pd
import sqlite3
from SQLiteStDev import StdevFunc

def query_db(production_type, db_path, table_name):
    '''
    This function queries an SQLite database.
    This function creates four subqueries for the four seasons
    and then queries from the results of those subqueries.

    The table returned by this query contains an hours column, production results
    by season, and standard deviation of those production results by season.
    '''

    query = f'''
    WITH spring AS
            (SELECT strftime ('%H', MTU) hour, AVG({production_type}) AS {production_type}_spring, stdev({production_type}) AS stdev{production_type}_spring
            FROM {table_name}
            WHERE strftime ('%m', MTU) IN ('02', '03', '04')
            GROUP BY strftime ('%H', MTU)),
        summer AS
            (SELECT strftime ('%H', MTU) hour, AVG({production_type}) AS {production_type}_summer, stdev({production_type}) AS stdev{production_type}_summer
            FROM {table_name}
            WHERE strftime ('%m', MTU) IN ('05', '06', '07')
            GROUP BY strftime ('%H', MTU)),
        fall AS
            (SELECT strftime ('%H', MTU) hour, AVG({production_type}) AS {production_type}_fall, stdev({production_type}) AS stdev{production_type}_fall
            FROM {table_name}
            WHERE strftime ('%m', MTU) IN ('08', '09', '10')
            GROUP BY strftime ('%H', MTU)),
        winter AS
            (SELECT strftime ('%H', MTU) hour, AVG({production_type}) AS {production_type}_winter, stdev({production_type}) AS stdev{production_type}_winter
            FROM {table_name}
            WHERE strftime ('%m', MTU) IN ('11', '12', '01')
            GROUP BY strftime ('%H', MTU))
    SELECT spring.hour, spring.{production_type}_spring AS Spring, spring.stdev{production_type}_spring AS spring_stdev, summer.{production_type}_summer AS Summer, summer.stdev{production_type}_summer AS summer_stdev, fall.{production_type}_fall AS Fall, fall.stdev{production_type}_fall AS fall_stdev, winter.{production_type}_winter AS Winter, winter.stdev{production_type}_winter AS winter_stdev
    FROM spring
        LEFT JOIN summer
            ON spring.hour = summer.hour
        LEFT JOIN fall
            ON spring.hour = fall.hour
        LEFT JOIN winter
            ON spring.hour = winter.hour
    ORDER BY spring.hour;
    '''

    # Initiate SQLite database connection object
    db_conn = sqlite3.connect(db_path)

    # Add a function to calculate standard deviation
    db_conn.create_aggregate("stdev", 1, StdevFunc)

    # Execute the query
    results = pd.read_sql_query(query, db_conn)

    return results
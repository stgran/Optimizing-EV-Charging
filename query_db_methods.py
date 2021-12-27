import pandas as pd
import sqlite3
from SQLiteStDev import StdevFunc

def query_db(production_type, db_path, table_name):
    # db_path = 'data/entsoe_2020_data.db'
    
    # table_name = 'entsoe'

    production_type_clause = f'AVG({production_type}) AS {production_type}, stdev({production_type}) AS stdev{production_type}'
    # if isinstance(production_types, list):
    #     # production_type_clause = f'AVG({production_types[0]}) AS {production_types[0]}, stdev({production_types[0]}) AS {production_types[0]}StDev'
    #     # for production_type in production_types[1:]:
    #     #     production_type_clause = production_type_clause + f', AVG({production_type}) AS {production_type}, stdev({production_type}) AS {production_type}StDev'
    #     production_type_clause = f'AVG({production_types[0]}) AS {production_types[0]}_{season}, stdev({production_types[0]}) AS stdev{production_types[0]}_{season}'
    #     for production_type in production_types[1:]:
    #         production_type_clause = production_type_clause + f', AVG({production_type}) AS {production_type}_{season}, stdev({production_type}) AS stdev{production_type}_{season}'
    # elif isinstance(production_types, str):
    #     production_type_clause = f'AVG({production_types}) AS {production_types}_{season}, stdev({production_types}) AS stdev{production_types}_{season}'

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
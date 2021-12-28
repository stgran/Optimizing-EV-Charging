from create_db_methods import load_dataset, clean_dataset, init_db, insert_data
import logging
import pandas as pd
import json

'''
During this step, two databases are created: a production database and an emissions database.

The only difference between these two databases is that for the emissions data,
the production data has been weighted by the respective emissions factor.
'''

def create_production_db():
    # Sets up logging
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    csv_path = 'data/actual_generation_per_production_type_2020.csv'

    db_path = 'data/entsoe_2020_data.db'

    production_table_name = 'entsoe_production'

    # Key for changing column names
    column_names = {
        'Biomass  - Actual Aggregated [MW]': 'Biomass',
        'Fossil Gas  - Actual Aggregated [MW]': 'FossilGas',
        'Fossil Hard coal  - Actual Aggregated [MW]': 'FossilHardCoal',
        'Fossil Oil  - Actual Aggregated [MW]': 'FossilOil',
        'Solar  - Actual Aggregated [MW]': 'Solar',
        'Waste  - Actual Aggregated [MW]': 'Waste',
        'Wind Offshore  - Actual Aggregated [MW]': 'WindOffshore',
        'Wind Onshore  - Actual Aggregated [MW]': 'WindOnshore'}

    # LOAD DATASET
    dataset = load_dataset(csv_path)

    # CLEAN DATASET
    cleaned_dataset = clean_dataset(dataset, column_names)
    cleaned_dataset.to_csv('data/cleaned_data.csv')

    # CREATE PRODUCTION DB
    init_db(db_path, production_table_name)

    # INSERT PRODUCTION DATA INTO PRODUCTION DB
    insert_data(db_path, cleaned_dataset, production_table_name, 'TotalProduction')

def create_emissions_db():
    db_path = 'data/entsoe_2020_emissions_data.db'

    emissions_table_name = 'entsoe_emissions'

    with open('data/emissionFactors.json') as f:
        emission_factors_dict = json.load(f) # Load in the emission factor data from a json file

    # When getting the emission factors from the json file, I need to make sure I'm
    # getting the right factor for each production type. I made this key to ensure
    # this is done correctly.
    emission_types_key = {
        'Biomass': 'biomass',
        'FossilGas': 'gas',
        'FossilHardCoal': 'coal',
        'FossilOil': 'oil',
        'Solar': 'solar',
        'Waste': 'biomass',
        'WindOffshore': 'wind',
        'WindOnshore': 'wind',
    }

    emissions_dataset = pd.read_csv('data/cleaned_data.csv')

    for production_type in emission_types_key:
        emission_factor = emission_factor = emission_factors_dict['defaults'][emission_types_key[production_type]]['value']
        emissions_dataset[production_type] = emissions_dataset[production_type].apply(lambda prod: prod * emission_factor)

    emissions_dataset.to_csv('data/emissions_data.csv')

    # CREATE EMISSIONS DB
    init_db(db_path, emissions_table_name)

    # INSERT EMISSIONS DATA INTO EMISSIONS DB
    insert_data(db_path, emissions_dataset, emissions_table_name, 'TotalEmission')
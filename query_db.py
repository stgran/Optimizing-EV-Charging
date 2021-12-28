import pandas as pd
import json
from query_db_methods import query_db

'''
During this step, the two SQLite databases are queried to generate seven datasets.
'''

def prepare_datasets():
    # These are the production types used in East Denmark
    production_types = ['Biomass', 'FossilGas', 'FossilHardCoal', 'FossilOil', 'Solar', 'Waste', 'WindOffshore', 'WindOnshore']

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
        
    # We will break our data down seasonally
    seasons = {'spring': (2, 3, 4), 'summer': (5, 6, 7), 'fall': (8, 9, 10), 'winter': (11, 12, 1)}

    # Here we will outline the datasets we want so we can add to them as we
    # cycle through the seasons
    hours = {'hour': range(24)}

    TotalProductionHourly = query_db('TotalProduction', 'data/entsoe_2020_data.db', 'entsoe_production')

    TotalProductionHourly.to_csv('data/TotalProductionHourly.csv')

    TotalEmissionsHourly = query_db('TotalEmission', 'data/entsoe_2020_emissions_data.db', 'entsoe_emissions')

    TotalEmissionsHourly.to_csv('data/TotalEmissionsHourly.csv')

    EfficiencyHourly = TotalProductionHourly['hour'].copy().to_frame()
    for season in ['Spring', 'Summer', 'Fall', 'Winter']:
        EfficiencyHourly[f'{season}'] = TotalProductionHourly[f'{season}'] / TotalEmissionsHourly[f'{season}']

    EfficiencyHourly.to_csv('data/EfficiencyHourly.csv')

    SolarHourly = query_db('Solar', 'data/entsoe_2020_data.db', 'entsoe_production')

    SolarHourly.to_csv('data/SolarHourly.csv')

    WindOffshoreHourly = query_db('WindOffshore', 'data/entsoe_2020_data.db', 'entsoe_production')

    WindOffshoreHourly.to_csv('data/WindOffshoreHourly.csv')

    WindOnshoreHourly = query_db('WindOnshore', 'data/entsoe_2020_data.db', 'entsoe_production')

    WindOnshoreHourly.to_csv('data/WindOnshoreHourly.csv')

    FossilCoalHourly = query_db('FossilHardCoal', 'data/entsoe_2020_data.db', 'entsoe_production')

    FossilCoalHourly.to_csv('data/FossilCoalHourly.csv')

    return TotalProductionHourly, TotalEmissionsHourly, EfficiencyHourly, SolarHourly, WindOffshoreHourly, WindOnshoreHourly, FossilCoalHourly
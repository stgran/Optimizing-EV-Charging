import pandas as pd
import json
from query_db_methods import query_db

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

    # ProductionHourlyByType = pd.DataFrame(data=hours)

    # HourlyEmissions = pd.DataFrame(data=hours)

    # TotalEmissions = pd.DataFrame(data=hours)

    # Efficiency = pd.DataFrame(data=hours)

    # EmissionFactors = pd.DataFrame()

    # DailyProductionByType = pd.DataFrame()

    # for season in seasons:
    #     # The first dataset we need is average total electricity production over for a day
    #     dataset_1 = query_db('TotalProduction', seasons[season], season)
    #     destination = f'data/{season}TotalProductionHourly.csv'

    #     dataset_1.to_csv(destination)

    #     # The second dataset we need is average electricity production by production type
    #     # for a day, which we will then scale by emission factors and sum to get
    #     # total emissions for a day.
    #     dataset_2 = query_db(production_types, seasons[season])
    #     destination = f'data/{season}ProductionHourlyByType.csv'
    #     dataset_2.to_csv(destination)

    #     dataset_3 = dataset_2.copy()
    #     emission_factors = {'ProductionType': [], 'EmissionFactor': []}
    #     daily_production = {'ProductionType': [], 'DailyProduction': []}
    #     for production_type in emission_types_key:
    #         daily_production['ProductionType'].append(production_type)
    #         daily_production['DailyProduction'].append(dataset_3[production_type].sum())
            
    #         emission_factor = emission_factors_dict['defaults'][emission_types_key[production_type]]['value']
    #         dataset_3[production_type] = dataset_3[production_type].apply(lambda production: scaleByEF(production, emission_factor))

    #         emission_factors['ProductionType'].append(production_type)
    #         emission_factors['EmissionFactor'].append(emission_factor)
    #     dataset_3['TotalEmissions'] = dataset_3.apply(lambda row: row.Biomass + row.FossilGas + row.FossilHardCoal + row.FossilOil + row.Solar + row.Waste + row.WindOffshore + row.WindOnshore, axis=1)
    #     dataset_3.to_csv('data/HourlyEmissions.csv')

    #     dataset_4 = dataset_1.copy()
    #     dataset_4['TotalEmissions'] = dataset_3['TotalEmissions']
    #     dataset_4['Efficiency'] = dataset_4.apply(lambda row: row.TotalProduction / row.TotalEmissions, axis=1)

    #     dataset_5 = pd.DataFrame.from_dict(emission_factors)

    #     dataset_6 = pd.DataFrame.from_dict(daily_production)

    #     return dataset_1, dataset_2, dataset_3, dataset_4, dataset_5, dataset_6
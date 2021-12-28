from create_db import create_production_db, create_emissions_db
from query_db import prepare_datasets
from visualize_analyses import visualize
from summary_stats import get_summary_stats

'''
This script executes the entire process, including:
- Importing data as a .csv
- Cleaning the data
- Creating SQL databases and inserting the data into the dbs
- Querying the dbs
- Analyzing the queried data
- Visualizing the data and analyses
'''

def main():
    create_production_db()
    create_emissions_db()
    prepare_datasets()
    TotalProductionHourly, TotalEmissionsHourly, EfficiencyHourly, SolarHourly, WindOffshoreHourly, WindOnshoreHourly, FossilCoalHourly = prepare_datasets()
    visualize(TotalProductionHourly, TotalEmissionsHourly, EfficiencyHourly, SolarHourly, WindOffshoreHourly, WindOnshoreHourly, FossilCoalHourly)
    get_summary_stats(TotalEmissionsHourly)

if __name__ == '__main__':
    main()
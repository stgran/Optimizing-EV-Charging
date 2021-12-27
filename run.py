from create_db import create_production_db, create_emissions_db
from query_db import prepare_datasets
from visualize_analyses import visualize
from summary_stats import get_summary_stats

def main():
    create_production_db()
    create_emissions_db()
    prepare_datasets()
    TotalProductionHourly, TotalEmissionsHourly, EfficiencyHourly, SolarHourly, WindOffshoreHourly, WindOnshoreHourly, FossilCoalHourly = prepare_datasets()
    visualize(TotalProductionHourly, TotalEmissionsHourly, EfficiencyHourly, SolarHourly, WindOffshoreHourly, WindOnshoreHourly, FossilCoalHourly)
    get_summary_stats(TotalEmissionsHourly)
    # dataset_1, dataset_2, dataset_3, dataset_4, dataset_5, dataset_6 = prepare_datasets()
    # visualize(dataset_1, dataset_2, dataset_3, dataset_4, dataset_5, dataset_6)

if __name__ == '__main__':
    main()
from matplotlib.pyplot import plot
from visualize_analyses_methods import seasonal_bars

def visualize(TotalProductionHourly, TotalEmissionsHourly, EfficiencyHourly, SolarHourly, WindOffshoreHourly, WindOnshoreHourly, FossilCoalHourly):
    seasonal_bars(
        dataset=TotalProductionHourly,
        bars_cols=['Spring', 'Summer', 'Fall', 'Winter'],
        labels_col='hour',
        y_label='Avg Electricity Production (MWH)',
        x_label='Hour',
        title='Seasonal Average Production over 24 Hrs',
        destination='figures/SeasonalProductionOver24Hrs.png'
    )

    seasonal_bars(
        dataset=TotalEmissionsHourly,
        bars_cols=['Spring', 'Summer', 'Fall', 'Winter'],
        labels_col='hour',
        y_label='Avg Emissions (kgCO2e)',
        x_label='Hour',
        title='Seasonal Average Emissions over 24 Hrs',
        destination='figures/SeasonalEmissionsOver24Hrs.png'
    )

    seasonal_bars(
        dataset=EfficiencyHourly,
        bars_cols=['Spring', 'Summer', 'Fall', 'Winter'],
        labels_col='hour',
        y_label='Average Efficiency (MWH/kgCO2e)',
        x_label='Hour',
        title='Seasonal Average Efficiency over 24 Hrs',
        destination='figures/SeasonalEfficiencyOver24Hrs.png'
    )

    seasonal_bars(
        dataset=SolarHourly,
        bars_cols=['Spring', 'Summer', 'Fall', 'Winter'],
        labels_col='hour',
        y_label='Avg Electricity Production (MWH)',
        x_label='Hour',
        title='Seasonal Solar Production over 24 Hrs',
        destination='figures/SeasonalSolarOver24Hrs.png'
    )

    seasonal_bars(
        dataset=WindOffshoreHourly,
        bars_cols=['Spring', 'Summer', 'Fall', 'Winter'],
        labels_col='hour',
        y_label='Avg Electricity Production (MWH)',
        x_label='Hour',
        title='Seasonal Offshore Wind Production over 24 Hrs',
        destination='figures/SeasonalWindOffshoreOver24Hrs.png'
    )

    seasonal_bars(
        dataset=WindOnshoreHourly,
        bars_cols=['Spring', 'Summer', 'Fall', 'Winter'],
        labels_col='hour',
        y_label='Avg Electricity Production (MWH)',
        x_label='Hour',
        title='Seasonal Onshore Wind Production over 24 Hrs',
        destination='figures/SeasonalWindOnshoreOver24Hrs.png'
    )

    seasonal_bars(
        dataset=FossilCoalHourly,
        bars_cols=['Spring', 'Summer', 'Fall', 'Winter'],
        labels_col='hour',
        y_label='Avg Electricity Production (MWH)',
        x_label='Hour',
        title='Seasonal Coal Production over 24 Hrs',
        destination='figures/SeasonalFossilCoalOver24Hrs.png'
    )

    # plot_bars(
    #     dataset=dataset_1,
    #     bars_col='TotalProduction',
    #     labels_col='hour',
    #     y_label='Avg Electricity Production (MWH)',
    #     x_label='Hour',
    #     title='Total Average Production over 24 Hrs',
    #     destination='figures/ProductionOver24Hrs.png'
    # )
    
    # plot_bars(
    #     dataset=dataset_3,
    #     bars_col='TotalEmissions',
    #     labels_col='hour',
    #     y_label='Avg Emissions (kg CO2 equivalent)',
    #     x_label='Hour',
    #     title='Total Average Emissions over 24 Hrs',
    #     destination='figures/EmissionsOver24Hrs.png'
    # )

    # plot_bars(
    #     dataset=dataset_4,
    #     bars_col='Efficiency',
    #     labels_col='hour',
    #     y_label='Avg Efficiency of Electricity Production (MWH/kgCO2e)',
    #     x_label='Hour',
    #     title='Production Efficiency over 24 HRs',
    #     destination='figures/EfficiencyOver24Hrs.png'
    # )

    # subplot_bars(
    #     dataset=dataset_2,
    #     bars_cols=['Biomass', 'FossilGas', 'FossilHardCoal', 'FossilOil', 'Solar', 'Waste', 'WindOffshore', 'WindOnshore'],
    #     labels_col='hour',
    #     y_label='Avg Elec Prod (MWH)',
    #     x_label='Hour',
    #     title='Average Production by Production Type over 24 Hrs',
    #     destination='figures/ProductionByTypeOver24Hrs.png'
    # )

    # plot_bars(
    #     dataset=dataset_5,
    #     bars_col='EmissionFactor',
    #     labels_col='ProductionType',
    #     y_label='kgCO2eq/MWh',
    #     x_label='Production Type',
    #     title='Emission Factor by Production Type',
    #     destination='figures/EmissionFactorsByType.png'
    # )

    # plot_bars(
    #     dataset=dataset_6,
    #     bars_col='DailyProduction',
    #     labels_col='ProductionType',
    #     y_label='MWh',
    #     x_label='Production Type',
    #     title='Average Daily Production by Production Type',
    #     destination='figures/DailyProductionByType.png'
    # )
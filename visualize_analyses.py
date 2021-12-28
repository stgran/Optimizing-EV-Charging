from visualize_analyses_methods import seasonal_bars

def visualize(TotalProductionHourly, TotalEmissionsHourly, EfficiencyHourly, SolarHourly, WindOffshoreHourly, WindOnshoreHourly, FossilCoalHourly):
    '''
    During this step, data visualizations are created for seven datasets.
    '''
    
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
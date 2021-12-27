import pandas as pd

def daily_stats(dataset):
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    results = {'Season': seasons, 'StDev': [], 'NormStDev': [], 'Range': [], 'NormRange': []}
    for season in seasons:
        stdev = dataset[season].std()
        results['StDev'].append(stdev)

        normalized_stdev = stdev / dataset[season].mean()
        results['NormStDev'].append(normalized_stdev)

        rang = dataset[season].max() - dataset[season].min()
        results['Range'].append(rang)

        normalized_range = rang / dataset[season].mean()
        results['NormRange'].append(normalized_range)
    return results

def get_summary_stats(TotalEmissionsHourly):
    TotalEmissionsResultsDict = daily_stats(TotalEmissionsHourly)
    TotalEmissionsResults = pd.DataFrame.from_dict(TotalEmissionsResultsDict)
    TotalEmissionsResults.to_csv('Tables/TotalEmissionsStats.csv')


## Input Dataset
The data regarding electricity production by production type for East Denmark (bidding zone DK2) was sourced from ENTSO-E. It can be found [here](https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show?name=&defaultValue=true&viewType=TABLE&areaType=BZN&atch=false&datepicker-day-offset-select-dv-date-from_input=D&dateTime.dateTime=21.12.2021+00:00|CET|DAYTIMERANGE&dateTime.endDateTime=21.12.2021+00:00|CET|DAYTIMERANGE&area.values=CTY|10Y1001A1001A65H!BZN|10YDK-2--------M&productionType.values=B01&productionType.values=B02&productionType.values=B03&productionType.values=B04&productionType.values=B05&productionType.values=B06&productionType.values=B07&productionType.values=B08&productionType.values=B09&productionType.values=B10&productionType.values=B11&productionType.values=B12&productionType.values=B13&productionType.values=B14&productionType.values=B20&productionType.values=B15&productionType.values=B16&productionType.values=B17&productionType.values=B18&productionType.values=B19&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)).

In this dataset, MTU stands for "market time unit". Times in data/actual_generation_per_production_type_2020.csv are shown in CET.

All columns in this dataset other than "Area" and "MTU" use Megawatts as their unit. Because each row of data in these columns represents an hour of electricity production, Megawatts is equivalent to Megawatt Hours.

Many of the columns regarding types of electricity production are filled with 'n/e' ('not expected'). This means that that type of electricity production does not occur within the bidding zone. These columns could also contain 'n/a' ('not available'), meaning that that type of electricity production is expected but the data is missing.

## Emission Factors
Emission factors for each production type of electricity are contained in emissionFactors.json.  

The "value" argument of each type of production type represents the emission factors for that production type. The unit of these values is grams of carbon dioxide equivalent per kilowatt hour of generation (gCO<sub>2</sub>eq/kWh).  

More information about these emission factors is available in the Parliamentary Office of Science and Technology's "Carbon Footprint of Electricity Generation" article published in October 2006, which can be found [here](https://researchbriefings.files.parliament.uk/documents/POST-PN-268/POST-PN-268.pdf).

## Steps
The first four steps occur in create_db.py: importing the data, cleaning the data, creating the SQLite database, and inserting the cleaned dataset into the database.

### Importing the Data
Data is imported using pandas' read_csv.

### Cleaning
Four steps were taken during cleaning:  
1. Columns that were entirely 'n/e' were dropped from the dataset because that type of electricity production did not occur in the DK2 bidding zone during 2020. This resulted in dropping thirteen columns.
2. Columns that were over 10% 'n/a' (missing data) were flagged. No columns were flagged.
3. The format of the MTU (datetime) column was changed so that SQLite could recognized the column as containing datetimes.
4. Column names were adjusted.

### Creating the SQLite Database
This step was completed using the sqlite3 package. The database was initialized with all the columns remaining after the cleaning step, plus a generated column TotalProduction that is calculated by adding up the electricity production from across all production types.

### Inserting Data into the Database.
This step was completed using the sqlite3 and pandas package.

### Querying Data from the Database
We will create the datasets we need for visualization during this step by querying from our database and making some adjustments.

#### Dataset 1: Total Average Production over a Day

#### Dataset 2: Average Emissions over a Day by Production Type
For this dataset, we will query the a day's worth of average hourly production for each production type. We will then multiply this production data by the respective emission factors to determine the average hourly emissions for each production types. The unit of the emission factor is grams carbon dioxide equivalent per kilowatt hour, which is equivalent to kilograms carbon dioxide equivalent per megawatt hour. We multiply production (megawatt hours) by the emission factor (kilograms carbon dioxide equivalent per megawatt hour), giving us a unit of kilograms carbon dioxide equivalent (kgCO<sub>2</sub>eq) for Dataset 2.
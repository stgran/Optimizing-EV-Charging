# Materials and Relevant Info
The materials that are most relevant to a reviewer are:
- `REPORT.md`: Contains the report for the Copenhagen-based Danish EV charging app client.
- `README.md`: Standard README for the code files.
- Python files:
    - `create_db.py`
    - `create_db_methods.py`
    - `query_db.py`
    - `query_db_methods.py`
    - `run.py`
    - `summary_stats.py`
    - `visualize_analyses.py`
    - `visualize_analyses_methods.py`

All other files support these main files.
- The `data` folder contains the original dataset, emission factors data, the SQLite databases, and all other datasets created for visualization purposes.
- The `figures` folder contains all data visualizations created for the report.
- The `tables` folder contains a data table regarding emissions variations relevant to the report.
- `NordicBiddingZones.png` is used to explain Denmark's two electricity grids in the report. `THEMA-report-2013-27-Nordic_Bidding_Zones_FINAL.pdf` is the source of this map.
- `SQLiteStDev.py` contains a standard deviation aggregate function for SQLite.
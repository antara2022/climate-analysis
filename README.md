## Climate Analysis
Analyzes Climate Data using Python, SQLAlchemy Queries and a Flask API

## Objective #1: Analyze and Explore the Climate Data
### Step 1 - Create Database
- Use the SQLAlchemy create_engine() function to connect to the SQLite database
- Use the SQLAlchemy automap_base() function to reflect the tables into classes, and then save references to the classes named station and measurement
- Link Python to the database by creating a SQLAlchemy session
### Step 2 - Precipitation Analysis
- Find the most recent date in the dataset
- Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data
- Select only the "date" and "prcp" values
- Load the query results into a Pandas DataFrame, set the index to the "date" column and sort the DataFrame values by "date".
![image](https://github.com/antara2022/climate-analysis/assets/112270155/44f097ab-8277-4a73-b35b-dbd94738016b)

- Plot the results by using the DataFrame plot method
![image](https://github.com/antara2022/climate-analysis/assets/112270155/afcb80d1-c447-48b0-9484-d18567906cee)

- Use Pandas to print the summary statistics for the precipitation data
![image](https://github.com/antara2022/climate-analysis/assets/112270155/c3affa96-6798-4c84-a2a2-b6a25b6a0051)

### Step 3 - Station Analysis
- Design a query to calculate the total number of stations in the dataset
- Design a query to find the most-active stations
  - List the stations and observation counts in descending order.
- Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query
- Design a query to get the previous 12 months of temperature observation (TOBS) data
  - Plot the results as a histogram
![image](https://github.com/antara2022/climate-analysis/assets/112270155/22359c6f-91ce-4519-aca6-49b8ec231236)

## Objective #2: Design A Climate App
### Step 4 - Flask API
- Design a Flask API based on the queries that were just developed
- Create the routes for each page
  - /
    - Start at the homepage
    - List all the available routes
  - /api/v1.0/precipitation
    - Convert the query results from the precipitation analysis to a dictionary using date as the key and prcp as the value
    - Return the JSON representation of your dictionary
  - /api/v1.0/stations
    - Return a JSON list of stations from the dataset
  - /api/v1.0/tobs
    - Query the dates and temperature observations of the most-active station for the previous year of data
    - Return a JSON list of temperature observations for the previous year
  - /api/v1.0/ and /api/v1.0//
    - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range
    - For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date
    - For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive

Contact: antara.choudhury3000@gmail.com

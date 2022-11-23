# Part 2: Designing Climate App
# Designing a Flask API based on the queries that have been developed in part 1

#########################################################################################
# Import dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import numpy as np
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the database into a new model
Base = automap_base()

# Reflect tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# creating a home route
@app.route("/")
def welcome():
    """Listing all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"Precipitation: /api/v1.0/precipitation<br/>"
        f"List of Weather Stations: /api/v1.0/stations<br/>"
        f"Temperature for Previous Year for Most Active Station: /api/v1.0/tobs<br/>"
        f"Mininum Temperature, Average Temperature, and the Maximum Temperature from the start date(yyyy-mm-dd): /api/v1.0/yyyy-mm-dd<br/>"
        f"Mininum Temperature, Average Temperature, and the Maximum Temperature from start to end dates(yyyy-mm-dd,yyyy-mm-dd)): /api/v1.0/yyyy-mm-dd,yyyy-mm-dd"
    )

@app.route('/api/v1.0/<start>')
def start_date(start):
    session = Session(engine)
    queryresult = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    session.close()

    tobs_data = []
    for min,avg,max in queryresult:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobs_data.append(tobs_dict)

    return jsonify(tobs_data)

@app.route('/api/v1.0/<start>/<stop>')
def start_stop_date(start,stop):
    session = Session(engine)
    queryresult = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= stop).all()
    session.close()

    tobs_data = []
    for min,avg,max in queryresult:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        tobs_data.append(tobs_dict)

    return jsonify(tobs)

@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    lateststr = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    lastdate = dt.datetime.strptime(lateststr, '%Y-%m-%d')
    querydate = dt.date(lastdate.year -1, lastdate.month, lastdate.day)
    sel = [Measurement.date,Measurement.tobs]
    queryresult = session.query(*sel).filter(Measurement.date >= querydate).all()
    session.close()

    tobs_data = []
    for date, tobs in queryresult:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs
        tobs_data.append(tobs_dict)

    return jsonify(tobs_data)

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    sel = [Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation]
    queryresult = session.query(*sel).all()
    session.close()

    stations_dataset = []
    for station,name,lat,lon,el in queryresult:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Lat"] = lat
        station_dict["Lon"] = lon
        station_dict["Elevation"] = el
        stations_dataset.append(station_dict)

    return jsonify(stations_dataset)

@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    lateststr2 = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    lastdate2 = dt.datetime.strptime(lateststr2, '%Y-%m-%d')
    querydate = dt.date(lastdate2.year -1, lastdate2.month, lastdate2.day)
    sel = [Measurement.date,Measurement.prcp]
    queryresult = session.query(*sel).filter(Measurement.date >= querydate).all()
    session.close()

    precip = []
    for date, prcp in queryresult:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precip.append(prcp_dict)

    return jsonify(precip)

if __name__ == '__main__':
    app.run(debug=True)
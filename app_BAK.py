################################################### 
# Import Dependencies  
###################################################

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

################################################### 
# SQL Database Setup  
###################################################

# Create query engine
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect db (schema) into new model
Base = automap_base()

# Reflect db tables (create class instances)
Base.prepare(engine,reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

################################################### 
# Flask Database Setup  
###################################################

app = Flask(__name__)

# Welcome route (http://127.0.0.1:5000/)
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end<br/>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
 
################################################### 
# Create Precipitation Route 
# http://127.0.0.1:5000/api/v1.0/precipitation 
###################################################

# Return precipitation data for last year
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

################################################### 
# Create Stations Route  
# http://127.0.0.1:5000/api/v1.0/stations 
###################################################   

# Return list of stations in db
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

################################################### 
# Create Monthly Temperature (TOBS) Route 
# http://127.0.0.1:5000/api/v1.0/tobs  
###################################################   

# Return temperature observations for the previous year
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    
    #unravel results into 1D list & convert to python (numpy) list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

################################################### 
# Create Statistics (temp/start/end) Route  
# http://127.0.0.1:5000/api/v1.0/temp/2017-06-01/2017-06-30 
###################################################   

# Return stats (min, avg, and max temp)
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

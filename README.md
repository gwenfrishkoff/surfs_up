# "Surfs Up" (Weather Data Analysis using Python & SQlite)

## Project Overview
The target audience for this project is a potential investor, who is considering whether to fund a brick-and-mortar ice-cream shop, to be located in Oahu, Hawaii. The investor has requested an analysis of local weather data, which will be used to project earnings throughout the year.

For the current project, we have been asked to use Python, together with SQlite, to summarize and describe the weather data. The client has requested two main deliverables:
	<ol>
	<li> Deliverable 1: Summary Statistics for June;
	<li> Deliverable 2: Summary Statistics for December.
	</ol>

Based on these summary statistics, the client has asked us to provide a high-level summary of the results and to suggest additional queries to gather more weather data for June and December.

## Data & Resources
For this project, we used the following source data and resources:
	<ol>
	<li> SQlite Database: 'hawaii.sqlite'; and
	<li> Python 3, using Jupyter Notebooks web interface, together with the following methods and modules:
        <li> Pandas (to covert data to DataFrames);
        <li> NumPy (for statistical analysis); and
		<li> SqlAlchemy (to load SQL data and create Object Relational Mappings)
	</ol>

## Results Summary
The python code that generates the weather data analysis has been saved to the file 'SurfsUp_Challenge.ipynb'. Results suggest the following conclusions:
	<ol>
	<li> Temperatures in Oahu, HI are relatively stable throughout the year (mean & standard deviation in temperatures for June and December are 75±3 and 71±3 degrees, respectively); 
    <li> There is slightly more variation in warmer temperatures in June, as compared with December (i.e., temps are slightly positively skewed in June); and
	<li> Temperatures rarely drop below 60 degrees, even in December (lower quartile = 64).
	</ol>

## Recommendations & Future Analyses
Variations in rain (precipitation) can also affect business throughout the year. We therefore wrote additional queries (Queries #3-4 in 'SurfsUp_Challenge.ipynb') to retrieve these data for June and December and a dynamic query (Query #5) to retrieve minimum, maximimum, and average rain for user-specified start and end dates.
#HW6_jmv423
Jordan Vani (10/16/2016)

###Assignment 1: NYC Buildig Energy Usage

1. Energy data is accessed directly from NYC open data and read into a DataFrame. Unnecessary columns and rows with NaN are dropped.
2. Building data is curled into PUIDATA, unzipped, and the shapefile is loaded into a DataFrame. Unnecessary columns and rows with NaN are dropped.
3. Energy and building data are merged based on BBL. SiteEUI is converted to numeric value.
4. Scatter matrix of merged data is plotted.
5. Energy consumption vs. number of units is plotted.
6. Log number of units vs. log total energy is plotted.
7. Linear models are created for both log energy vs. log units and log units vs. log energy using the statsmodels.formula.api module.
8. NEED TO EXPLAIN THE CHI SQUARE EVALUATION.
9. A 2nd order polynomial is fitted to log energy vs. log units. 
10. NEED TO EXPLAIN THE LIKELIHOOD EVALUATION.

####Work Breakdown
Ben Miller explained curl-ing data to PUIDATA. Reviewed assignment with Tashay Green.

###Assignment 2: Citibike mini-project
[See Jupyter Notebook](https://github.com/jvani/PUI2016_jmv423/blob/master/HW6_jmv423/Assignment2_jmv423.ipynb)

1. Data was loaded from the CitiBike System Data portal.
2. Unnecessary columns were dropped, and the date was reformated.
3. A T-test was utilized via scipy.

The resulting Authorea article can be seen [here](https://www.authorea.com/users/106017/articles/133419/_show_article).

####Work Breakdown
Work done with Tashay Green.

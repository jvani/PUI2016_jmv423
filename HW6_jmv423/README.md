#HW6_jmv423
Jordan Vani (10/16/2016)

###Assignment 1: NYC Buildig Energy Usage

1. Energy data is accessed directly from NYC open data and read into a DataFrame. Unnecessary columns and rows with NaN are dropped.
2. Building data is curled into PUIDATA, unzipped, and the shapefile is loaded into a DataFrame. Unnecessary columns and rows with NaN are dropped.
3. Energy and building data are merged based on BBL. SiteEUI is converted to numeric value.
4. Scatter matrix of merged data is plotted.
5. Energy consumption vs. number of units is plotted.
6. I dropped all rows where the # of units or energy usage was less than 1. 
7. I added columns to my dataframe where I calculated the log values of the unit tota and energy use total.
8. I then dropped all rows where the log of the units total was less than 1.
9. Log number of units vs. log total energy is plotted.
10. Linear models are created for both log energy vs. log units and log units vs. log energy using the statsmodels.formula.api module.
11. The chi-square values were calculated for both linear models and compared to assess, which model was a better fit to the data. The units vs. energy model returned a lower chi square value indicating a better fit. 
12. A 2nd order polynomial is fitted to log energy vs. log units using the statsmodels.formula.api module. 
13. The likelihood ratio was calculate to test if the polynomial model was a better fit than the linear model. Since the comparison returned a p-value of ~ 0 we could reject the null hypothesis and accept the alternative hypothesis: the second order polynomial fits the data significantly better than the linear model.

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

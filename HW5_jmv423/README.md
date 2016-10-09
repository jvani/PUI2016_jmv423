#HW5_jmv423
Jordan Vani (10/09/2016)

###Assignment 1:  Compare Tests for Goodness of fit 
1. Citibike data was accessed, unzipped, and loaded into a dataframe.
2. Data frame was modified: dropped unnecessary columns, renamed columns, calculated age, and dropped Nan).
3. Generated normal and chi square distributions with size and shape similar to the citibike data.
4. Graphed the distribution of citibike data, and the normal and chi square data.
5. Ran KS test for citibike data against both the normal distribution and chi square distribution. Rejected the null hypothesis for both tests.
6. Ran chi square test for citibike data against both the normal distribution and chi square distribution. Rejected the null hypothesis for both tests.

####Work Breakdown
All work done by Jordan Vani

###Assignment 2: Line Fitting and Data Munging with Income Gender Bias
1. Load all data as pandas dataframes to two dictionaries.
2. For all columns in each dataframe except the characteristic column, coerce the datatype to numeric.
3. Show data and plot scatter matrix for the all male dataframe and the all female dataframe.
4. Plot the male vs. female median income for each racial group. 
5. Run ols regression and analytical regression. Plot both.
6. Plot male vs. female for all income types and run an ols regression. Plot all.
7. Predicted the expected income of a woman compared to a man at $30,000, when considering all income types. 
8. Described the results in terms of race.

####Work Breakdown
All work done by Jordan Vani

##Assignment 3:
####Do diets help lose more fat than excercise?
Ho: Diets help lose an equal or less amount (lbs) of fat than does excercise (p = 0.05). Diets <= Excercise

Ha: Diets help lose more fat (lbs) than excercise (p = 0.05). Diets > Excercise
####Do Americans trust the president?
Ho: Americans do not trust or are ambivalent towards the president (p = 0.05). P(yes) <= 0.5.

Ha: Americans do trust the president (p = 0.05). P(yes) > 0.5.

####Effectiveness of nicotine patches to quit smoking.
Ho: Nicotine patches cause cessation rates to be equal or less than control patches (p = 0.05). P(Cessation|Patch) <= P(Cessation|Control).

Ha: Nicotine patches cause cessation rates to be larger than with the control patches (p = 0.05). P(Cessation|Patch) > P(Cessation|Control).

####Quantify the danger of smoking for pregnant women.
Ho: The IQ of children with mothers who smoked during their pregnancy is equal or greater than children whose mothers did not smoke. IQs >= IQn.

Ha: The IQ of children with mothers who smoked during their pregnancy is less than children whose mothers did not smoke. IQs < IQn.

#HW4_jmv423
Jordan Vani (10/02/2016)

###Assignment 1:  Review Citibike Proposal
See markdown file here: https://github.com/jvani/PUI2016_nm2773/blob/master/HW3_nm2773/CitibikeReview_jmv423.md

Pull request submitted 10/01/2016.

####Work Breakdown
All work done by Jordan Vani

###Assignment 2: Literature choices of statistical tests.
For the multiple regression paper the case-1 regression was examined.

 Analyses           | IV(s)                                                                                                                   | IV type(s)  | DV(s)         | DV type(s) | Control Var | Control Var Type | Question to be answered                                                                                                               | _H0_                                                                                                                                               | alpha         | link to paper 
--------------------|-------------------------------------------------------------------------------------------------------------------------|-------------|---------------|------------|-------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------
T-test              | (1) Fighting Stance                                                                                                     | Dichotomous | (1) Winning % | Continuous | 0           | NA               | Is there a winning % advantage for left handed MMA fighters?                                                                          | Ho: Left handed fighters have a disadvantage or no difference in winning % compared to right handed fighters.                                      | alpha = 0.025 | [The Southpaw Advantage? - Lateral Preference in Mixed Martial Arts](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0079793)              
Multiple Regression | (1) Commercial Sex Workers % of Pop, (2) GINI Measure of Income Inequality, (3) % Pop Muslim, (4) Female Illiteracy Rate| Continuous  | (1) HIV rate  | Continuous | 0           | NA               | Is there a relationship the % of commercial sex workers in a pop, inequality, the % of Muslims, and female illiteracy with HIV rates? | Ho: There is no relationship between the % of commercial sex workers in a pop, inequality, the % of Muslims, and female illiteracy with HIV rates? | alpha = 0.05  | [Size Matters: The Number of Prostitutes and the Global HIV/AIDS Pandemic](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0000543) 

####Work Breakdown
Papers selected and reviewed with Ian Stuart.

###Assignment 3: Reproduce the analysis of the Hard to Employ program in NY
1. Hypotheses were formulated and statistical significance levels set.
2. Z-test was performed, null hypothesis was not rejected.
2. Chi square test was performed, null hypothesis was not rejected.

####Work Breakdown
Work was done with Tashay Green.

###Assignment 4: Tests of correlation using the scipy package with citibike data
1. Data was accessed (directly from citibike), unzipped, and loaded into a pandas dataframe. 
2. KS test was completed on the  male and female distributions (null was rejected).
3. KS test was completed on a subsample (every 200th row) of the male and female distributions (null was rejected).
4. A subsample of male citibike users was selected to be equal len() as the female sample.  The two distributions were sorted by age and a Pearson's test was completed (null was rejected).
5. Using the same subsample of male citibike users, with both male and female ages sorted a  Spearman's test was completed (null was rejected).
6. Time of day was classified as day or night. A KS test was completed on the distribution of ages  of both night and day time users (null was rejected).

####Work Breakdown
All work was done by Jordan Vani. Some  code borrowed from  Prof. Bianca (https://github.com/fedhere/PUI2016_fb55/blob/master/HW4_fb55/citibikes_compare_distributions.ipynb)

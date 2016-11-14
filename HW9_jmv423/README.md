#HW9_jmv423
Jordan Vani (14/11/2016)

## Assignment 1

###Data Formatting
1. Curl data to PUIDATA from Github.
2. Load data using numpy.
3. Create empty ndarry with dtype float.
4. Convert mta_data to float array and store in empty ndarry.
5. Replace all -1 values with nan.

###Task 1: Event Detection
1. Sum over card type and stations to get total ridership by week.
2. Find index with minimum ridership.
3. Calculate date by adding index+1 weeks to the start date.
4. Plotted figure to show event.

###Task 2: Ridership Type Changes
1. Sum over stations to get total ridership by card type for each week.
2. Create pandas dataframe, calculate fields for first & last 10 weeks, ratio, and label.

###Task 3: Periodicity 
1. Use data of total ridership by week for each station.
2. Append fourier transform of each column to list.
3. Append annual values (week 52) to list.
4. Enumerate annual values from list.
5. Sort enumerated list by second value in tuple.
6. Extract top 4 values for annual periodicity.
7. Plotted figure to show periodicity.

###Extra Credit: Clustering
1. Calculate silhouette score for cluster size 2:6.
2. Perform PCA reduction using 2 eigenvectors.
3. Label subway stops by KMean cluster of PCA results.
4. Plot PCA transformed data labelled by cluster.

####Work Breakdown
All work done by Jordan Vani, reviewed with Tashay Green.

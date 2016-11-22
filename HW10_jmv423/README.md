#HW10_jmv423
Jordan Vani (20/11/2016)

### Assignment 1: Finish Lab
I ran and uploaded SIna Kashuk's notebook we went through in class.

###Assignment 2: Spatial Autocorrelation
Using Sina Kashuk's provided notebook I split the citibike data into two subsets where winter included November to April and summer included May to October. This decision was informed by visually inspecting the seasonal periodicity seen in Figure 1. The spatial distribution of rides between summer and winter show a similar pattern as seen in Figures 3 & 4. By subsequently plotting Moran's Scatterplot in Figure 6, we can clearly see the presence of positive spatial autocorrelation. The calculated Moran's I for summer was 0.626 and the I for winter was 0.641, the statistical significance of these values is visually presented in Figure 7.  Ultimately, the calculated I values suggest a stronger positive spatial autocorrelation in the winter than in summer, which is seen in Figure 8. Ultimately, the spatial autocorrelation is presented in Figure 9, wherein areas with each low & high ridership is clustered together.

The slight differences in autocorrelation strength may be a result of fewer people using citibike outside of existing hotspots. As such, the ridership is slightly more concentrated in the winter in the summer. Together these two insights make sense, given how people are less likely to ride to distant areas in the winter as a result of the weather.

Steps:

1. Download and load all data.
2. Examine seasonality of data by plotting boxplots for monthly ridership.
3. Visualize seasonal trends using the sm.tsa.seasonal_decompose function.
4. Intersect Citibike station geometry with census tract.
5. Break down resulting dataset into 'winter' & 'summer' average the rides accordingly.
6. Plot ridership heatmap.
7. Edit shapefile, and re plot ridership heatmap.
8. Calculate spatial lag & quantiles for neighbors in each winter and summer subsets.
9. Plot spatial lag.
10. Plot the Moran's scatterplot & KDE plot of Morans I for both winter and summer.
11. Ultimately, plot the hot and cold spots based on the local spatial autocorrelation.

###Work Breakdown
All work and interpretation done by Jordan Vani.

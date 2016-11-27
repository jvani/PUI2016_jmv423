#HW11_jmv423
Jordan Vani (26/11/2016)

### Assignment 1: Plot CUSP & Census Tracts

1. Download & unzip data, load into GeoDataFrame. Query to only show Brooklyn, set to WGS 84.
2. Create point shape of CUSP in GeoDataFrame.
3. Intersect tract with CUSP. 
4. Plot all data.

###Work Breakdown
All work and interpretation done by Jordan Vani.

###Assignment 2: Clustering Businesses

1. Download and load census data, concatenate all data to one dataframe and set index to zipcode.
2. Download and load zipcode data, fill zipcodes with leading 0s and set to index.
3. Whiten establishment counts by zipcode.
4. Perform PCA reduction to two dimensions, and do kmean clustering in 2 clusters.
5. Do DBSCAN clustering.
6. Plot kmeans and DBSCAN clutsering on NYC shapefile. Both show similar results, 18 zipcodes flip cluster group between the two algorithms.
7. To interpret the results I plotted the normalized establishment value for each cluster. Accordingly, the first Kmeans cluster generally shows a trend of increasing number of establishments. The second kmeans cluster generally shows a decrease in the number of establishments or no change.

###Work Breakdown
All work and interpretation done by Jordan Vani.

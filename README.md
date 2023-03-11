This is a repository which implements simple visualization of K-means and KNN ML algorithms.

It uses pygame python library for visualization.

It uses python language for implementation of algorithms.

Overview : It first takes number of points as input and then classifies input points into 
3 (fixed) clusters. After that it takes a new point and k-value as input to classify new point
into a cluster based on K-nearest neighbours.

Working steps : 

1. Run the kmeans_knn.py python file.
2. A user console will open.
3. Enter the number of inputs (say n) asked as user input in the console and press enter.
4. A pygame window will open.
5. Click with mouse in the pygame window to locate the n points.
6. Enter one extra point (say p) which will be classified into a cluster based on KNN.
7. On entering point p, n points will be classified into 3 clusters.
8. Now, user console will ask for value of k in KNN (K-nearest neighbor).
9. Enter k value and press enter.
10. Go to pygame window, you will see that point p will be colored to either red, blue or 
    green accordingly. Quit the pygame window.
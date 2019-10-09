"""
    HIGH LEVEL EXPLANATION:

    K-MEANS is a static custering algorithm that is used on machine learning to cluster
    information together. The way that it works is that you are chosing K points that will
    be put on random positions. After each repetition each point is assigned to each clustering
    point depending on which cluster is closest to the point. After that the new position of each
    cluster is chosen by finding the average position of all points that were assigned to that cluster.
"""

import random
import math

# Create a point class functioning more like a data structure
class Point:

    x = 0
    y = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y

k = int(input("Select how many centroids you need"))
n = int(input("Select how many random points do you want"))

centroids = []
points = []

# Creating a multidimensional array here with our point structure
#
# [ [Point*n]*k ]

centroid_points = [ [ Point(0,0) for i in range(n)] for j in range(k)]
amount_of_centroids_on_each_point = []

# randomization of points
for i in range(k):
    point = Point(random.uniform(10,100),random.uniform(10,100))
    centroids.append(point)

for i in range(n):
    point = Point(random.uniform(10,100),random.uniform(10,100))
    points.append(point)



failSafeCounter = 0
flag = 0

# Main functionallity
while flag == 0 and failSafeCounter < 1000:

    flag = 0

    #Reseting this array
    for i in range(n):
        amount_of_centroids_on_each_point.append(0)

    for i in range(n):

        # Looping through the points array to find the
        # cluster with the minimum ditance from the point
        # and assigning it to that
        minimum = 99999999
        lower_centroid = -1

        for j in range(k):

            # Finding the cluster here with the miminum distance from the point
            distance = math.sqrt( (centroids[j].x-points[i].x)*(centroids[j].x-points[i].x) + (centroids[j].y-points[i].y)*(centroids[j].y-points[i].y ))
            if (distance < minimum):
                minimum = distance
                lower_centroid = j

        # Assigning point to the cluster
        centroid_points[lower_centroid][amount_of_centroids_on_each_point[lower_centroid]].x = points[i].x
        centroid_points[lower_centroid][amount_of_centroids_on_each_point[lower_centroid]].y = points[i].y
        amount_of_centroids_on_each_point[lower_centroid] += 1

    failSafeCounter+=1

    for i in range(k):
        avgx = 0
        avgy = 0
        counter = 0

        for j in range(n):
            if (not(centroid_points[i][j].x == 0 and centroid_points[i][j].y == 0)):
                avgx+=centroid_points[i][j].x
                avgy+=centroid_points[i][j].y
                counter+=1

        if counter!=0:
            
            if centroids[i].x != (avgx/counter) or centroids[i].y != (avgy/counter):
                flag = 1
                
            centroids[i].x = (avgx/counter)
            centroids[i].y = (avgy/counter)


# Loop through the points list to show the results
for i in range(k):
    print('Cluster {} has the following points:\n'.format(i))
    for j in range(n):
        if (not(centroid_points[i][j].x == 0 and centroid_points[i][j].y == 0)):
            print('x:{},y:{}'.format(centroid_points[i][j].x,centroid_points[i][j].y))

    print('\n')

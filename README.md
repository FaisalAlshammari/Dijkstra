# Dijkstra
## Finding the shortest path between two vertices using Dijkstra's algorithm

### Overview of the program:

This program finds the shortest path between two nodes entered by the user, the information of a 
weighted undirected graph G = (V,E) including the number of vertices and the x-y coordinates for the 
vertices and the edges information are all given in a text file. the method I used to implement this is 
Dijkstra algorithm which is an algorithm for finding the shortest paths between nodes in a graph. And 
this program has many useful uses in real life like choosing the shortest path for a trip where the weight 
is the time needed to reach the desired destination like in google maps. Or even in networking it can 
find the shortest path to optimize and enhance the network performance it can also be used in 
automated robots or drones to choose the shortest path to deliver a package to a certain location. 
Weights does not need to represent distance all the time it can represent trip time or fuel cost in
transportation for examples. As for time complexity heappush() and heappop() have a time complexity 
of O(logn) separately but the time complexity for Dijkstra's algorithm implementation is O(n^2logn).

 ////////////////////////////////////////////////////

### Here are the requirements the program is following:
- Your program should read the information of a weighted undirected graph G = (V,E) using a text file in the following format:
(a) The first line has an integer specifying the number of vertices in the graph (i.e.,|V |).
(b) Lines from line number 2 to line number |V | +1 give the x− and y− coordinates
of all vertices starting from v0. These lines are in the format of two integers
separated by a comma.
(c) Lines from line number |V |+2 to the last line give information about the edges of
the graph in the format of three integers separated by commas. A line containingi, j, k
tells you that there is an edge between vi and vj and its weight is k.
Vertices are numbered from 0 to |V | − 1, where |V | is given to you in the first line of the text file.
- Your program should draw the Graph described in the text file.
- Your program should find and highlight the shortest path between two vertices entered
by the user. Note that the user will enter two integers representing the vertices he/she
is asking about and your program will highlight (with a different color) the shortest path between them.


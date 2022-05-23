import matplotlib.pyplot as plt  # for plotting the graph
import matplotlib.lines as mlines
import networkx as nx  # for visualization of graph
from collections import defaultdict
from heapq import *

with open("Vertices.txt") as f:
    lines = f.readlines()

    numOfVertices = lines[0]

    vertices = []
    vertices = list(range(int(numOfVertices)))

    rawedges = lines[int(numOfVertices) + 1:]

    my_edges_w = []
    weights = []
    my_edges = []
    myedgeslist = []
    for line in rawedges:
        node1, node2, weight = (line.strip().split(','))
        my_edges_w.append((node1, node2, int(weight)))
        my_edges.append((node1, node2))
        myedgeslist.append((int(node1), int(node2)))
        weights.append(int(weight))

x_edges = []
y_edges = []
x_edges = [x[0] for x in myedgeslist]
y_edges = [x[1] for x in myedgeslist]

rawcor = lines[1:int(numOfVertices) + 1]
my_cor = []
x_cor = []
y_cor = []
for line in rawcor:
    x, y, = (line.strip().split(','))
    my_cor.append((x, y))
    x_cor.append(int(x))
    y_cor.append(int(y))

while True:
    print('Enter two vertices from the list :', vertices)
    start_node = input("Enter start node: ")
    end_node = input("Enter end node: ")
    userinput = []
    userinput.append(int(start_node))
    userinput.append(int(end_node))

    if any(num not in vertices for num in
           userinput):  # if userinput[0] not in vertices or userinput[1] not in vertices:

        print('invalid input, please enter vertices from the given list only:')
        msg = False
        continue
    else:
        msg = True
        break


def dijkstra(edges, f, t):
    g = defaultdict(set)
    for i, j, k in edges:
        g[i].add((k, j))
        g[j].add((k, i))

    q, seen = [(0, f, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path += (v1,)
            if v1 == t:
                return cost, path

            for k, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost + k, v2, path))

    return float("infinity")


path_and_weights = dijkstra(my_edges_w, start_node, end_node)

Sb_weights = path_and_weights[0]
shortest_path = (path_and_weights[1])
path_weight = (path_and_weights[0])
shortest_path_int = []
shortest_path_int = [int(x) for x, in shortest_path]
sp_Lt = []
sp_Lt = tuple(shortest_path_int)

if msg:
    print('shortest path is => ', shortest_path_int)
    print('path weight is:', path_weight)

G = nx.Graph()
z = 0
while z < len(vertices):
    G.add_node(vertices[z], pos=(int(x_cor[z]), int(y_cor[z])))
    z = z + 1

d = 0
while d < len(my_edges):
    G.add_edge(x_edges[d], y_edges[d], weight=weights[d], edge_color='red')
    d = d + 1

fi = []
for i in range(len(shortest_path_int) - 1):  # get the edges of the shortest path
    fi.append(
        (min(shortest_path_int[i], shortest_path_int[i + 1]),
         max(shortest_path_int[i], shortest_path_int[i + 1])))  # sp.append((shortestpath[i],shortestpath[i+1]))

c_list = []
for i in G.edges():
    if i in fi:  # if edges is in shortest path tuples then color it red
        c_list.append("red")
    else:  # color the rest with green
        c_list.append("Green")

weight = nx.get_edge_attributes(G, 'weight')
pos = nx.get_node_attributes(G, 'pos')

nx.draw_networkx_edge_labels(G, pos, edge_labels=weight)
nx.draw(G, pos, with_labels=weight)
nx.draw_networkx_edges(G, pos, edge_color=c_list)

Sp_Red = mlines.Line2D([], [], color='red', markersize=2, label='shortest path')
plt.legend(handles=[Sp_Red], )
plt.axis(True)
plt.show()

f.close()

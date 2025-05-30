---
title: Minimum Spanning Tree using Kruskal's Algorithm
date: May 06, 2017
tags:
    - algorithm
    - graph
    - python
---

Hey there!! Now we are heading off to finding a minimal spanning tree for an
undirected graph. It is recommended to go through my previous post on [Disjoint
Set Data Structure](/posts/disjoint-set-data-structure.html)

It is assumed that the reader knows about Graph, a very important data
structure in computer science with lots of applications(social networks,
computer networks, digital circuits, and many more).

An undirected graph has no sense of directions in edges. For example, if we
have an edge connecting two vertices A and B, that edge can be called as
connecting A to B or B to A. The adjacency matrix for the graph is symmetric.
graph

Above is a simple small graph(hand made by me, no wonder why the graph edges
are zig-zagged). The adjacency matrix for the graph is thus,

```python
# the infinity
INF = 99999999
# our adjacency matrix
adjacency = \
[[INF,7,2,5],
[7,INF,4,1],
[2,4,INF,4],
[5,1,4,INF]]
```

I have chosen adjacency matrix for graph representation here. And as mentioned
earlier, the adjacency matrix is symmetric because it is an undirected graph.
INF means infinity and is the weight of the vertices that are not connected.
Ignore the blue edges for now.

Kruskal's algorithm goes like this:

* List out the edges of the graph.
* For each edge, make a set containing only the edge. If there are n edges then, there will be n sets(partitions) at this step.
* Take an edge with smallest weight value and check if the vertices connected by it are in same set. If not, union them, else continue with the next smallest edge.
* Repeat till all vertices are contained in a single set.

### Code

Lets directly go into the code for the implementation is very very easy.

```python
# number of vertices
v = len(adjacency)

# now get the edges
# an edge is a tuple (vertex 1, vertex 2, weight)
edges = [(i, j, adjacency[i][j]) for i in range(v) for j in range(i, v) if adjacency[i][j]!=INF]

# sort edges
# because we need to take out smallest edges first.
edges.sort(key=lambda x: x[2])

# CREATE a disjoint set datastructure
# The constructor will automaticall create separate set for each vertex
disset = DisjointSet(v) # v is number of vertices

c = 0 # counter
wts = 0 # total weight of the final spanning treee
final_edges = []
while c < len(edges):
    edge = edges[c]
    i,j, w = edge[0], edge[1], edge[2]
    if disset.find(i) != disset.find(j):
        wts+=w
        disset.union(i, j)
        final_edges.append(edge)
    c+=1

print(final_edges)
```

Running the above code for the graph shown above, we get the output: `[(1, 3, 1), (0, 2, 2), (1, 2, 4)]` which are the blue edges in the figure.
That's all about the Kruskal's Algorithm. Easy, ain't it??

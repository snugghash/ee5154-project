import numpy
import networkx as nx
import os, pickle

def readGraph(path, delimiter=" ", directed=False, weighted=False, skip=0):
    fileHandle = open(path, 'r');
    for i in range(1,skip+1):
        fileHandle.readline()
    ##lines = fileHandle.readlines();
    G = nx.DiGraph();
    if(directed==False):
        G = G.to_undirected()
    for line in fileHandle.readlines():
        a = [int(i) for i in line[:-1].split(delimiter)]
        if(weighted==True):
            G.add_edge(a[0],a[1],weight=a[2])
        else:
            G.add_edge(a[0],a[1])
    return G

"""
Returns number of triangles in an undirected unweighted graph.
"""
def findTriangles(G):
    adjMat = nx.adjacency_matrix(G).toarray()
    return numpy.matrix.trace(numpy.linalg.matrix_power(adjMat,3))/6


"""
Reads network graph from Arnetminer dataset
"""
def readArnetminerGraph(path, delimiter=" ", directed=True, weighted=False, skip=0):
    x=0
    fileHandle = open(path, 'r');
    for i in range(1,skip+1):
        fileHandle.readline()
    G = nx.DiGraph();
    # TODO using dictionary for lineType
    for line in fileHandle.readlines():
        lineType = line[1]
        print(lineType)
        if lineType=='*':
            title = line[2:-1]
            x+=1
            print(x)
            print(title)
        elif lineType=='@':
            authors = line[2:-1]
        elif lineType=='t':
            year = line[2:-1]
        elif lineType=='c':
            journal = line[2:-1]
        elif lineType=='i':
            index = line[6:-1]
            G.add_node(index, journal=journal, year=year, authors=authors, title=title)
        elif lineType=='%':
            if line[2] != ' ':
                G.add_edge(index, line[2:-1])
        elif lineType=='!':
            if line[2] != '\n':
                G.node[index]['abstract'] = line[2:-1]
    return G

def storeNxGraph(G, path):
    nx.readwrite.gpickle.write_gpickle(G, path)

def readNxGraph(path):
    return nx.readwrite.gpickle.read_gpickle(path)

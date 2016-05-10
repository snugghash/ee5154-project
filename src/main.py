import networkx as nx

# Check loading of graph into nx on Artificial Intelligence dataset
from BasicGraphOperations import readArnetminerGraph, storeNxGraph
G = readArnetminerGraph("../DBLP_citation_2014_May/DBLP_Citation_2014_May/domains/Artificial intelligence.txt")
print(G.node["3003478"], G.node["3655495"])


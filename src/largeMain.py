# Load and store entire Aretminer dataset given
G = readArnetminerGraph("../DBLP_citation_2014_May/DBLP_Citation_2014_May/publications.txt")
print(G.node["3003478"], G.node["3655495"])
storeNxGraph(G,"nxGraphFull")

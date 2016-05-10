import networkx as nx
from BasicGraphOperations import readGraph

G1 = readGraph("../Q1weighted.txt",directed=False)
G2 = readGraph("../Q1unweighted.txt",directed=False)

def maxValKey(dictionary):
    values=list(dictionary.values())
    keys=list(dictionary.keys())
    return keys[values.index(max(values))]
node1 = maxValKey(nx.degree(G1))
node2 = maxValKey(nx.degree(G2))
print(node1,G1.degree(node1))
print(node2,G2.degree(node2))

import networkx as nx
from BasicGraphOperations import readGraph
import numpy

G1 = readGraph("Q2edgelist.txt",directed=True)

adjMat = nx.adjacency_matrix(G1)
print(adjMat.toarray())

"""
TODO Faster with just ccm = adj*adj.T
"""
def getCoCitationMatrix(G1):
    ccm = numpy.zeros([len(G1.nodes()),len(G1.nodes())])
    for i in range(1,len(G1.nodes())):
        ccm[i][i] = G1.in_degree(i)
        for j in range(i+1,len(G1.nodes())):
            ccm[i][j] = len(list(set(G1.predecessors(i)).intersection(set(G1.predecessors(j)))))
    ccm = ccm + ccm.T - numpy.diag(ccm.diagonal())
    return ccm

"""
TODO Faster with just bcm = adj.T*adj
"""
def getBibliographicCoupling(G1):
    bcm = numpy.zeros([len(G1.nodes()),len(G1.nodes())])
    for i in range(1,len(G1.nodes())):
        bcm[i][i] = G1.out_degree(i)
        for j in range(i+1,len(G1.nodes())):
            bcm[i][j] = len(list(set(G1.successors(i)).intersection(set(G1.successors(j)))))
    bcm = bcm + bcm.T - numpy.diag(bcm.diagonal())
    return bcm

print(getCoCitationMatrix(G1))
print(getBibliographicCoupling(G1))

import networkx as nx
from BasicGraphOperations import readGraph
import numpy
import operator
import matplotlib.pyplot as plt

G1 = readGraph("../citation.txt", directed=True, skip=1, delimiter='\t')

print(len(G1.nodes()))
print(len(G1.edges()))

degseq = list(G1.in_degree().values())
dmax = max(degseq)+1
freq = [ 0 for d in range(dmax) ]
for d in degseq:
    freq[d] += 1

plt.loglog(freq)
plt.show()
#plt.hist(freq)
#plt.show()

citations = G1.in_degree()
citations = sorted(citations.items(), key=operator.itemgetter(1),reverse=True)
print(citations[0])
print(citations[1])
print(citations[2])


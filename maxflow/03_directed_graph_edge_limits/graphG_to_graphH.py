# *really silly* algorthim trying to convert the problem of maximum flow with lower bound to another graph
# verify the correctness of doing so in test3.py in directed graph


class EdgeWithLimit(object):
    def __init__(self, u, v, w, l):
        self.source = u
        self.sink = v
        self.capacity = w
        self.lowerbound = l

    def __repr__(self):
        return "%s -> %s : %s with lower bound %s" %(self.source, self.sink, self.capacity, self.lowerbound)

class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w

    def __repr__(self):
        return '%-2s -> %-2s : %-2s ' %(self.source, self.sink, self.capacity)

def graphG_to_graphH(nodes, edges):
    """
    H_nodes lists
    H_edges EdgeWithLimit object
    """
    H_nodes = nodes + ['X', 'Y']
    H_edges = []
    for e1 in G_Edges:
        H_edges.append(Edge(e1.source, e1.sink, e1.capacity - e1.lowerbound))
        if e1.lowerbound != 0:
            H_edges.append(Edge('X', e1.sink, e1.lowerbound))
            H_edges.append(Edge(e1.source, 'Y', e1.lowerbound))
    return H_nodes, H_edges


G_nodes = ['S','A','B','C','D','T']
G_Edges = [ EdgeWithLimit('S','A',20,7), EdgeWithLimit('S','B',10,4),
            EdgeWithLimit('A','B',10,5), EdgeWithLimit('A','C',5, 0),
            EdgeWithLimit('C','B',15,1), EdgeWithLimit('B','D',10,3),
            EdgeWithLimit('D','C',10,4), EdgeWithLimit('D','T',20,4),
            EdgeWithLimit('C','T',15,2)]



H_nodes, H_edges =  graphG_to_graphH(G_nodes, G_Edges)
H_edges.sort(key = lambda edge: [ edge.source, edge.sink])

def compress_edges(edges):
    H_f_edges = [ ]

    for edge in edges:
        lastEdge = H_f_edges[-1] if H_f_edges != [] else None
        if lastEdge == None:
            H_f_edges.append(edge)
        else: # lastEdge is not None
            if edge.source == lastEdge.source and edge.sink == lastEdge.sink:
                cur_capacity = lastEdge.capacity
                H_f_edges[-1] = Edge(edge.source, edge.sink, cur_capacity + edge.capacity)
            else:
                H_f_edges.append(edge)

    return H_f_edges

H_f_edges = compress_edges(H_edges)
print 'nodes', H_nodes
print 'edges:'
for e in H_f_edges:
    print 'g.add_edge(' + '\'' + e.source + '\',\'' + e.sink +'\',' + str(e.capacity) + ')'

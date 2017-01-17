import FlowNetwork
g = FlowNetwork.FlowNetwork()

[g.add_vertex(v) for v in 'ABCD']

g.add_edge('A','B',1000)
g.add_edge('A','C',1000)
g.add_edge('B','C',1)
g.add_edge('B','D',1000)
g.add_edge('C','D',1000)


print g.max_flow('A','D')

import FlowNetwork
g = FlowNetwork.FlowNetwork()

[g.add_vertex(v) for v in 'XSABCDTY']

g.add_edge('A','B',5)
g.add_edge('A','C',5)
g.add_edge('A','Y',5)
g.add_edge('B','D',7)
g.add_edge('B','Y',3)
g.add_edge('C','B',14)
g.add_edge('C','T',13)
g.add_edge('C','Y',3)
g.add_edge('D','C',6)
g.add_edge('D','T',16)
g.add_edge('D','Y',8)
g.add_edge('S','A',13)
g.add_edge('S','B',6)
g.add_edge('S','Y',11)
g.add_edge('X','A',7)
g.add_edge('X','B',10)
g.add_edge('X','C',4)
g.add_edge('X','D',3)
g.add_edge('X','T',6)

print g.max_flow('X','Y')

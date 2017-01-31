import UndirectedFlowNetwork

g = UndirectedFlowNetwork.UndirectedFlowNetwork()

[g.add_vertex(v) for v in 'abcdeftghsjkmnpq']

g.add_edge('a','b',12)
g.add_edge('a','e',10)
g.add_edge('a','f',6)

g.add_edge('b','c',16)
g.add_edge('b','f',1)
g.add_edge('b','t',4)

g.add_edge('c','d',4)
g.add_edge('c','t',1)

g.add_edge('d','g',1)
g.add_edge('d','t',12)

g.add_edge('e','f',6)
g.add_edge('e','h',4)

g.add_edge('f','t',4)
g.add_edge('f','s',4)
g.add_edge('f','h',12)

g.add_edge('t','g',8)
g.add_edge('t','s',10)
g.add_edge('t','j',4)
g.add_edge('t','k',12)


g.add_edge('g','k',20)

g.add_edge('h','s',15)
g.add_edge('h','m',10)
g.add_edge('h','n',8)

g.add_edge('s','j',12)
g.add_edge('s','n',12)
g.add_edge('s','p',20)

g.add_edge('j','p',6)
g.add_edge('j','k',14)

g.add_edge('k','q',10)
g.add_edge('k','p',16)

g.add_edge('m','n',16)
g.add_edge('n','p',18)
g.add_edge('p','q',16)


print g.flow

# print g.get_edges('s')
# print g.find_path('s','t', [])


print g.max_flow('s','t')

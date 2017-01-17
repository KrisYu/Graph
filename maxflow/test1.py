import FlowNetwork

g = FlowNetwork.FlowNetwork()

[g.add_vertex(v) for v in 'sopqrt']

g.add_edge('s','o',3)
g.add_edge('s','p',3)
g.add_edge('o','p',2)
g.add_edge('o','q',3)
g.add_edge('p','r',2)
g.add_edge('r','t',3)
g.add_edge('q','r',4)
g.add_edge('q','t',2)

# print g.flow

# print g.get_edges('s')
# print g.find_path('s','t', [])


print g.max_flow('s','t')

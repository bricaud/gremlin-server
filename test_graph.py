#!/usr/bin/python
# -*- coding: utf-8 -*-

from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import Cardinality

statics.load_statics(globals())
# Initialize the graph and the traversal
graph = Graph()
g = graph.traversal().withRemote(DriverRemoteConnection('ws://localhost:8182/gremlin','g'))


print('Number of nodes {}, number of edges {}.'.format(g.V().count().next(),g.E().count().next()))
# Create nodes
print('Writing nodes...')
node1 = (g.addV('label1').property('name','Node1')
		.property('description','First node')
		.property('Node number',1))
node1.next()

node2 = (g.addV('label1').property('name','Node2')
		.property('description','Second node')
		.property('Node number',2))
node2.next()

# Adding a vertexProperty (property of node property):
g.V().has('name','Node1').properties('name').property('Created','Today').next()

# Create a edge between Node1 and Node2
print('writing edge...')
edge = (g.V().has('name','Node1')
	.addE('edge_label').to(g.V().has('name','Node2')).next())

# Check if it has been written correctly
print('Number of nodes {}, number of edges {}.'.format(g.V().count().next(),g.E().count().next()))

# Showing the graph nodes:
nodes_data = g.V().valueMap().toList()
print('Nodes and the data associated:')
print(nodes_data)

print('Property associated to "name" on Node1:')
name_property = g.V().has('name','Node1').properties('name').valueMap().next()
print(name_property)

# Showing data on the edge:
edges_data = g.E().valueMap().toList()
print('Edge and the data associated:')
print(edges_data)

# Remove all
print('Removing the nodes...')
g.V().drop().iterate()
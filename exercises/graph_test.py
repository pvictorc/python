from graphADT import *

import unittest


# TODO implementar testes com grafos dirigidos
class TestEdgeListGraph(unittest.TestCase):

    def setUp(self):
        self.graph = EdgeListGraph(directed=False)
        self.v1 = Vertex('u')
        self.v2 = Vertex('v')
        self.v3 = Vertex('w')
        self.v4 = Vertex('z')
        self.graph.insert_vertex(self.v1)
        self.graph.insert_vertex(self.v2)
        self.graph.insert_vertex(self.v3)
        self.graph.insert_vertex(self.v4)

    def test_vertex_operations(self):
        self.assertEqual(self.graph.vertex_count(), 4)
        self.graph.remove_vertex(self.v1)
        self.assertEqual(self.graph.vertex_count(), 3)

    def test_edge_operations(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.assertEqual(self.graph.edge_count(), 1)  # undirected graph creates 2 edges
        edge = self.graph.get_edge(self.v1, self.v2)
        self.assertIsNotNone(edge)
        self.graph.remove_edge(edge)
        self.assertEqual(self.graph.edge_count(), 0)

    def test_vertex_degree(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.graph.insert_edge(self.v1, self.v3, 'edge2')
        self.assertEqual(self.graph.degree(self.v1), 2)
        self.assertEqual(self.graph.degree(self.v2), 1)

    def test_incident_edges(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.graph.insert_edge(self.v1, self.v3, 'edge2')
        edges = list(self.graph.incident_edges(self.v1))
        self.assertEqual(len(edges), 2)


class TestAdjacencyListGraph(unittest.TestCase):

    def setUp(self):
        self.graph = AdjacencyListGraph(directed=False)
        self.v1 = Vertex('u')
        self.v2 = Vertex('v')
        self.v3 = Vertex('w')
        self.v4 = Vertex('z')
        self.graph.insert_vertex(self.v1)
        self.graph.insert_vertex(self.v2)
        self.graph.insert_vertex(self.v3)
        self.graph.insert_vertex(self.v4)

    def test_vertex_operations(self):
        self.assertEqual(self.graph.vertex_count(), 4)
        self.graph.remove_vertex(self.v1)
        self.assertEqual(self.graph.vertex_count(), 3)

    def test_edge_operations(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.assertEqual(self.graph.edge_count(), 1)
        edge = self.graph.get_edge(self.v1, self.v2)
        self.assertIsNotNone(edge)
        self.graph.remove_edge(edge)
        self.assertEqual(self.graph.edge_count(), 0)

    def test_vertex_degree(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.graph.insert_edge(self.v1, self.v3, 'edge2')
        if self.graph._directed:
            self.assertEqual(self.graph.degree(self.v1), 2)
            self.assertEqual(self.graph.degree(self.v2), 1)
            # somente para grafos não dirigidos
        else: 
            self.assertEqual(self.graph.degree(self.v1), 2)
            self.assertEqual(self.graph.degree(self.v2), 2) 

    def test_incident_edges(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.graph.insert_edge(self.v1, self.v3, 'edge2')
        edges = list(self.graph.incident_edges(self.v1))
        self.assertEqual(len(edges), 2)


class TestAdjacencyMapGraph(unittest.TestCase):

    def setUp(self):
        self.graph = AdjacencyMapGraph(directed=False)
        self.v1 = Vertex('u')
        self.v2 = Vertex('v')
        self.v3 = Vertex('w')
        self.v4 = Vertex('z')
        self.graph.insert_vertex(self.v1)
        self.graph.insert_vertex(self.v2)
        self.graph.insert_vertex(self.v3)
        self.graph.insert_vertex(self.v4)
        # Insert edges between vertices
        self.graph.insert_edge(self.v1, self.v2, None)
        self.graph.insert_edge(self.v2, self.v3, None)
        self.graph.insert_edge(self.v3, self.v1, None)
        self.graph.insert_edge(self.v3, self.v4, None)

    def test_vertex_operations(self):
        self.assertEqual(self.graph.vertex_count(), 4)
        self.graph.remove_vertex(self.v1)
        self.assertEqual(self.graph.vertex_count(), 3)

    def test_edge_operations(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.assertEqual(self.graph.edge_count(), 1)
        edge = self.graph.get_edge(self.v1, self.v2)
        self.assertIsNotNone(edge)
        self.graph.remove_edge(edge)
        self.assertEqual(self.graph.edge_count(), 0)

    def test_vertex_degree(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.graph.insert_edge(self.v1, self.v3, 'edge2')
        self.assertEqual(self.graph.degree(self.v1), 2)
        self.assertEqual(self.graph.degree(self.v2), 1)

    def test_incident_edges(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.graph.insert_edge(self.v1, self.v3, 'edge2')
        edges = list(self.graph.incident_edges(self.v1))
        self.assertEqual(len(edges), 2)


class TestAdjacencyMatrixGraph(unittest.TestCase):

    def setUp(self):
        self.graph = AdjacencyMatrixGraph(directed=False)
        self.v1 = Vertex('u')
        self.v2 = Vertex('v')
        self.v3 = Vertex('w')
        self.v4 = Vertex('z')
        self.graph.insert_vertex(self.v1)
        self.graph.insert_vertex(self.v2)
        self.graph.insert_vertex(self.v3)
        self.graph.insert_vertex(self.v4)

    def test_vertex_operations(self):
        self.assertEqual(self.graph.vertex_count(), 4)
        self.graph.remove_vertex(self.v1)
        self.assertEqual(self.graph.vertex_count(), 3)
        self.assertNotIn(self.v1, self.graph.vertices())

    def test_edge_operations(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.assertEqual(self.graph.edge_count(), 1)
        edge = self.graph.get_edge(self.v1, self.v2)
        self.assertIsNotNone(edge)
        self.graph.remove_edge(edge)
        self.assertEqual(self.graph.edge_count(), 0)

    def test_vertex_degree(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.graph.insert_edge(self.v1, self.v3, 'edge2')
        self.assertEqual(self.graph.degree(self.v1), 2)
        self.assertEqual(self.graph.degree(self.v2), 1)

    def test_incident_edges(self):
        self.graph.insert_edge(self.v1, self.v2, 'edge1')
        self.graph.insert_edge(self.v1, self.v3, 'edge2')
        edges = list(self.graph.incident_edges(self.v1))
        self.assertEqual(len(edges), 2)

    def test_directed_graph(self):
        directed_graph = AdjacencyMatrixGraph(directed=True)
        directed_graph.insert_vertex(self.v1)
        directed_graph.insert_vertex(self.v2)
        directed_graph.insert_edge(self.v1, self.v2, 'edge1')
        self.assertEqual(directed_graph.degree(self.v1, outgoing=True), 1)
        self.assertEqual(directed_graph.degree(self.v1, outgoing=False), 0)
        self.assertEqual(directed_graph.degree(self.v2, outgoing=True), 0)
        self.assertEqual(directed_graph.degree(self.v2, outgoing=False), 1)

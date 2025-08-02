# pid_reader_project/backend/graph_builder.py
import networkx as nx

class DiagramGraphBuilder:
    def __init__(self, lines, components, labels):
        self.lines = lines
        self.components = components
        self.labels = labels
        self.graph = nx.DiGraph()

    def build_graph(self):
        # Tambah node dari komponen
        for idx, comp in enumerate(self.components):
            node_id = f"comp_{idx}"
            self.graph.add_node(node_id, **comp)

        # Tambah label teks sebagai node
        for idx, label in enumerate(self.labels):
            node_id = f"label_{idx}"
            self.graph.add_node(node_id, **label)

        # Tambah edge dummy (belum spatial-aware)
        for i in range(len(self.components) - 1):
            self.graph.add_edge(f"comp_{i}", f"comp_{i+1}", relation="pipe")

        return self.graph

    def export_graph(self, format='json'):
        if format == 'json':
            import json
            return json.dumps(nx.node_link_data(self.graph), indent=2)
        elif format == 'gml':
            return nx.generate_gml(self.graph)
        else:
            raise ValueError("Unsupported export format")
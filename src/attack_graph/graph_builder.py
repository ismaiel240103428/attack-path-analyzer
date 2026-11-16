import networkx as nx


def build_attack_graph():
    graph = nx.DiGraph()

    graph.add_node("Web Server", type="Asset")
    graph.add_node("Application Server", type="Asset")
    graph.add_node("Database Server", type="Critical Asset")

    graph.add_edge("Web Server", "Application Server")
    graph.add_edge("Application Server", "Database Server")

    return graph
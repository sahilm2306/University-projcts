# MST using Prim's Algorithm
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import time


# ---------------------------------------------------
# Step 1: Let’s build a simple weighted graph
# ---------------------------------------------------
def create_sample_graph():
    """Creates a sample connected graph with 7 nodes and weighted edges."""
    G = nx.Graph()

    edges = [
        ('A', 'B', 7), ('A', 'D', 5),
        ('B', 'C', 8), ('B', 'D', 9), ('B', 'E', 7),
        ('C', 'E', 5),
        ('D', 'E', 15), ('D', 'F', 6),
        ('E', 'F', 8), ('E', 'G', 9),
        ('F', 'G', 11)
    ]
    G.add_weighted_edges_from(edges)
    return G


# ---------------------------------------------------
# 🎨 Helper: Draw the graph (with optional highlights)
# ---------------------------------------------------
def draw_graph(G, title="Graph", highlight_edges=None):
    """Draws the graph nicely with edge weights and optional highlights."""
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(6, 5))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color="#ADD8E6",
        node_size=800,
        font_size=10,
        font_weight="bold"
    )

    # Show edge weights
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Highlight MST edges in red if provided
    if highlight_edges:
        nx.draw_networkx_edges(
            G, pos,
            edgelist=highlight_edges,
            width=3,
            edge_color='red'
        )

    plt.title(title)
    plt.show()


# ---------------------------------------------------
# Step 2: Prim’s Algorithm in action
# ---------------------------------------------------
def prim_mst(G):
    """
    Runs Prim’s Algorithm to find the Minimum Spanning Tree (MST).
    It also pauses between steps to visually show the process.
    """
    start_node = list(G.nodes())[0]  # Start from the first node
    visited = {start_node}
    mst_edges = []

    # A priority queue keeps track of the smallest edges we can take next
    edge_queue = [
        (data['weight'], start_node, to)
        for to, data in G[start_node].items()
    ]
    heapq.heapify(edge_queue)

    print(f"🌱 Starting Prim’s Algorithm from node '{start_node}'...\n")

    while edge_queue and len(mst_edges) < len(G.nodes()) - 1:
        weight, frm, to = heapq.heappop(edge_queue)

        # If we've already visited this node, skip it
        if to in visited:
            continue

        # Otherwise, we’ll take this edge
        visited.add(to)
        mst_edges.append((frm, to, weight))
        print(f"✅ Added edge ({frm}, {to}) with weight {weight}")

        # Show the step visually
        draw_graph(
            G, title=f"Step: Added edge ({frm}, {to})", highlight_edges=[(frm, to)])
        time.sleep(1)

        # Look at the new node’s edges and add them to our priority queue
        for neighbor, data in G[to].items():
            if neighbor not in visited:
                heapq.heappush(edge_queue, (data['weight'], to, neighbor))

    # Build and return the MST as its own graph
    MST = nx.Graph()
    MST.add_weighted_edges_from(mst_edges)
    print("\n🌳 All done! Here's the final MST.\n")
    return MST


# ---------------------------------------------------
# 🚀 Step 3: Run the demo
# ---------------------------------------------------
def run_prim_demo():
    G = create_sample_graph()
    print("Here’s our original graph:")
    draw_graph(G, title="Original Graph")

    MST = prim_mst(G)
    draw_graph(MST, title="🎯 Final Minimum Spanning Tree",
               highlight_edges=MST.edges())
    return MST


# ---------------------------------------------------
# Bonus: Try it out on other example graphs
# ---------------------------------------------------
def create_graph_2():
    G = nx.Graph()
    edges = [
        ('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 5),
        ('B', 'D', 10), ('C', 'D', 3), ('C', 'E', 7),
        ('D', 'E', 1), ('D', 'F', 8), ('E', 'F', 6)
    ]
    G.add_weighted_edges_from(edges)
    return G


def create_graph_3():
    G = nx.Graph()
    edges = [
        ('1', '2', 3), ('1', '3', 1), ('2', '3', 7),
        ('2', '4', 5), ('3', '4', 2),
        ('3', '5', 8), ('4', '5', 4),
        ('4', '6', 6), ('5', '6', 9)
    ]
    G.add_weighted_edges_from(edges)
    return G


def test_three_graphs():
    graphs = [create_sample_graph, create_graph_2, create_graph_3]

    for i, graph_fn in enumerate(graphs, start=1):
        print(f"\n🔹 Running Prim’s Algorithm on Graph {i}")
        G = graph_fn()
        draw_graph(G, f"Graph {i}")
        MST = prim_mst(G)
        draw_graph(MST, f"Graph {i} - Final MST", highlight_edges=MST.edges())


# ---------------------------------------------------
# 🏁 The program starts here
# ---------------------------------------------------
if __name__ == "__main__":
    print("👋 Welcome to the Prim’s Algorithm Visualizer!\n")
    print("You’ll see how the algorithm builds the MST, step by step.")
    test_three_graphs()
    print("\n✨ Thanks for watching! Hope you enjoyed the visualization.")

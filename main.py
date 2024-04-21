import streamlit as st
import pandas as pd
from streamlit_agraph import agraph, Node, Edge, Config

def load_data(filepath):
    return pd.read_csv(filepath, index_col=0)

def create_graph(df):
    nodes = []
    edges = []

    # Create nodes
    for character in df.columns:
        nodes.append(Node(id=character, label=character, size=30, color="#D8C7B2"))

    # Create edges based on the adjacency matrix
    for i, row in df.iterrows():
        for j, value in row.items():
            if value != 0:  # Assuming only non-zero values should create edges
                edges.append(Edge(source=i, target=j, width=value, color="#E6D0AB"))

    # Graph configuration
    config = Config(width=2000, height=2000, directed=False, hierarchical=False, physics={
                        "barnesHut": {
                            "gravitationalConstant": -8000,  # Increased repulsive force
                            "centralGravity": 0.3,
                            "springLength": 200,  # Increased spring length
                            "springConstant": 0.04,
                            "damping": 0.09,
                            "avoidOverlap": 0.1
                        },
                        "minVelocity": 0.75,
                        "solver": "barnesHut",
                        "timestep": 0.5
                    },)

    # Display the graph
    return_value = agraph(nodes=nodes, edges=edges, config=config)
    return return_value

# Streamlit interface
def main():
    df = load_data("adjmatrix.csv")
    create_graph(df)

if __name__ == '__main__':
    main()

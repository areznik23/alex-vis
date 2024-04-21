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
        nodes.append(Node(id=character, label=character, size=10))

    # Create edges based on the adjacency matrix
    for i, row in df.iterrows():
        for j, value in row.items():
            if value != 0:  # Assuming only non-zero values should create edges
                edges.append(Edge(source=i, target=j, label=str(value), length=10))

    # Graph configuration
    config = Config(width=1000, height=1200, directed=False, physics=True, hierarchical=False)

    # Display the graph
    return_value = agraph(nodes=nodes, edges=edges, config=config)
    return return_value

# Streamlit interface
def main():
    df = load_data("adjmatrix.csv")
    create_graph(df)

if __name__ == '__main__':
    main()

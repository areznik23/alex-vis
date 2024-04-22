import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
from streamlit_agraph import agraph, Node, Edge, Config

def load_data(filepath):
    return pd.read_csv(filepath, index_col=0)

def create_graph(df):
    nodes = []
    edges = []

    # Create nodes
    for character in df.columns:
        nodes.append(Node(id=character, label=character, size=15, color="#d8c7b2"))

    # Create edges based on the adjacency matrix
    for i, row in df.iterrows():
        for j, value in row.items():
            if value != 0:  # Assuming only non-zero values should create edges
                edges.append(Edge(source=i, target=j, width=value * 0.3, color="#e6d0ab"))

    # Graph configuration
    config = Config(width=2000, height=2000, directed=False, hierarchical=False, physics={
                         "barnesHut": {
                            "gravitationalConstant": -15000,  # More negative for increased repulsion
                            "centralGravity": 0.1,  # Reduced to allow more dispersion
                            "springLength": 300,  # Increased for greater distance between nodes
                            "springConstant": 0.05,
                            "damping": 0.09,
                            "avoidOverlap": 0.2  # Increased to prevent nodes from overlapping
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

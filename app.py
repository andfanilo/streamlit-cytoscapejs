import streamlit as st
from streamlit_cytoscapejs import st_cytoscapejs

elements = [
    {"data": {"id": "one", "label": "Node 1"}, "position": {"x": 0, "y": 0}},
    {"data": {"id": "two", "label": "Node 2"}, "position": {"x": 100, "y": 0}},
    {"data": {"source": "one", "target": "two", "label": "Edge from Node1 to Node2"}},
]
stylesheet = [
    {"selector": "node", "style": {"width": 20, "height": 20, "shape": "rectangle"}},
    {"selector": "edge", "style": {"width": 10}},
]

st.title("Hello Cytoscape.js")
clicked_elements = st_cytoscapejs(elements, stylesheet)

if clicked_elements is not None:
    st.write(clicked_elements)
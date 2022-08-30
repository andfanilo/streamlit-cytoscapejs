# Streamlit Cytoscape.js

Streamlit wrapper of [React Cytoscape.js](https://github.com/plotly/react-cytoscapejs).

## Installation

```
pip install streamlit-cytoscapejs
```

## Try it

```python
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
```

## Development

### Install

- JS side

```shell script
cd streamlit_cytoscape/frontend
npm install
```

- Python side

```shell script
conda create -n streamlit-cytoscapejs python=3.7
conda activate streamlit-cytoscapejs
pip install -e .
```

### Run

Both webpack dev server and Streamlit should run at the same time.

- JS side

```shell script
cd streamlit_cytoscape/frontend
npm run start
```

- Python side

```shell script
streamlit run app.py
```

## Next steps

I don't plan to make a lot of progress on this for now (except if huge interest) but if you want to contribute/take over its development I'm happy to lend a hand :).

Obviously missing lots of things like:

- viewport manipulation props from React cytoscapejs.
- custom layout
- adding an extension (but also you'd better fork this repo and add the extension yourself I think :/)

## References

- [React Cytoscape.js](https://github.com/plotly/react-cytoscapejs)
- [Cytoscape.js source code demos](https://github.com/cytoscape/cytoscape.js/tree/master/documentation/demos)

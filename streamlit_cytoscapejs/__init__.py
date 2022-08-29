import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "streamlit_cytoscapejs", url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component(
        "streamlit_cytoscapejs", path=build_dir
    )


def st_cytoscapejs(elements, stylesheet, width=400, height=400, key=None):
    """Cytoscape.js in Streamlit.

    Parameters
    ----------
    elements: Dict
        
    stylesheet: Dict
    
    height: int

    width: int
        
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    """
    return _component_func(
        elements=elements,
        stylesheet=stylesheet,
        width=width,
        height=height,
        key=key,
        default=None,
    )


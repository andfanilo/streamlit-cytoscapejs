import {
  Streamlit,
  ComponentProps,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { useEffect } from "react"
import CytoscapeComponent from "react-cytoscapejs"

const StreamlitCytoscape = ({ args }: ComponentProps) => {
  useEffect(() => Streamlit.setFrameHeight())
  return (
    <CytoscapeComponent
      elements={args.elements}
      stylesheet={args.stylesheet}
      style={{ width: args.width, height: args.height }}
      cy={(cy) => {
        cy.on('tap', 'node', function (evt) {
          var node = evt.target;
          Streamlit.setComponentValue({ 'selected_node_id': node.id() });
        });
      }}
    />
  )
}

export default withStreamlitConnection(StreamlitCytoscape)

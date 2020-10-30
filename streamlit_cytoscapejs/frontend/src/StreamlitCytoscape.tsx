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
    />
  )
}

export default withStreamlitConnection(StreamlitCytoscape)

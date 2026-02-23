"use client"
import ReactFlow, { useNodesState, useEdgesState } from 'reactflow'
export default function MemoryFlow() {
  const [nodes] = useNodesState([{id:'1', position:{x:0,y:0}, data:{label:'ConsolidationNode'}}])
  return <ReactFlow nodes={nodes} />
}
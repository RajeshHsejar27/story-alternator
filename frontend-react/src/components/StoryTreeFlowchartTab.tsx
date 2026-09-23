import React from 'react';
import { ReactFlow, Controls, Background } from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import type { Book } from '../types';

interface StoryTreeFlowchartTabProps {
  books: Book[];
  activeBookId: string;
  onBranchSelect: (branchId: string) => void;
}

export const StoryTreeFlowchartTab: React.FC<StoryTreeFlowchartTabProps> = ({
  books,
  activeBookId,
  onBranchSelect
}) => {
  const currentBook = books.find((b) => b.id === activeBookId) || books[0];

  // Dynamically build React Flow nodes and edges from story branches
  const initialNodes = currentBook.branches.map((branch, idx) => ({
    id: branch.id,
    position: { x: 250, y: 50 + idx * 140 },
    data: {
      label: (
        <div style={{ padding: '8px 12px', textAlign: 'center' }}>
          <div style={{ fontWeight: 800, color: idx === 0 ? '#475569' : '#6d28d9', fontSize: '0.85rem' }}>
            {idx === 0 ? '📖 Canonical Story Node' : '⚡ Alternate Plot Branch'}
          </div>
          <div style={{ fontSize: '0.95rem', fontWeight: 700, color: '#0f172a', marginTop: '4px' }}>
            {branch.title}
          </div>
        </div>
      )
    },
    style: {
      background: idx === 0 ? '#f8fafc' : '#fcfbf7',
      border: idx === 0 ? '2px solid #cbd5e1' : '2px solid #6d28d9',
      borderRadius: '12px',
      width: 280,
      boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)'
    }
  }));

  const initialEdges = currentBook.branches.slice(1).map((branch) => ({
    id: `e-root-${branch.id}`,
    source: currentBook.branches[0].id,
    target: branch.id,
    animated: true,
    style: { stroke: '#6d28d9', strokeWidth: 2 }
  }));

  return (
    <div className="flowchart-container">
      <div style={{ padding: '1rem', background: '#f8fafc', borderBottom: '1px solid #e2e8f0', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h2 style={{ fontSize: '1.2rem', fontWeight: 800, color: '#0f172a' }}>
            Story Decision Tree: {currentBook.title}
          </h2>
          <p style={{ fontSize: '0.85rem', color: '#64748b' }}>
            Interactive React Flow node graph visualizing narrative branches and plot pivots.
          </p>
        </div>
      </div>

      <ReactFlow
        nodes={initialNodes}
        edges={initialEdges}
        onNodeClick={(_, node) => onBranchSelect(node.id)}
        fitView
      >
        <Background gap={16} size={1} />
        <Controls />
      </ReactFlow>
    </div>
  );
};

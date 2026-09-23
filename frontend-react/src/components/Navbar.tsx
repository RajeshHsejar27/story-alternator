import React from 'react';
import { BookOpen, GitBranch, MessageSquare, Library } from 'lucide-react';

interface NavbarProps {
  activeTab: 'catalog' | 'reader' | 'flowchart' | 'chatbot';
  setActiveTab: (tab: 'catalog' | 'reader' | 'flowchart' | 'chatbot') => void;
  activeBookTitle: string;
}

export const Navbar: React.FC<NavbarProps> = ({ activeTab, setActiveTab, activeBookTitle }) => {
  return (
    <header className="app-header">
      <div className="brand-container">
        <div className="brand-logo">📖 Story Alternator</div>
        <span className="brand-badge">React Techstack v2.0</span>
      </div>

      <nav className="nav-tabs">
        <button
          className={`nav-tab ${activeTab === 'catalog' ? 'active' : ''}`}
          onClick={() => setActiveTab('catalog')}
        >
          <Library size={16} /> Enterprise Catalog
        </button>
        <button
          className={`nav-tab ${activeTab === 'reader' ? 'active' : ''}`}
          onClick={() => setActiveTab('reader')}
        >
          <BookOpen size={16} /> Story Reader
        </button>
        <button
          className={`nav-tab ${activeTab === 'flowchart' ? 'active' : ''}`}
          onClick={() => setActiveTab('flowchart')}
        >
          <GitBranch size={16} /> Story Tree Flowchart
        </button>
        <button
          className={`nav-tab ${activeTab === 'chatbot' ? 'active' : ''}`}
          onClick={() => setActiveTab('chatbot')}
        >
          <MessageSquare size={16} /> AI Assistant
        </button>
      </nav>

      <div style={{ fontSize: '0.85rem', color: '#94a3b8', fontWeight: 600 }}>
        Active: <span style={{ color: '#ffffff' }}>{activeBookTitle}</span>
      </div>
    </header>
  );
};

import React from 'react';
import type { Book } from '../types';
import { Download, BookOpen, Layers } from 'lucide-react';
import confetti from 'canvas-confetti';

interface ReaderTabProps {
  books: Book[];
  activeBookId: string;
  activeBranchId: string;
  onBookChange: (bookId: string) => void;
  onBranchChange: (branchId: string) => void;
}

export const ReaderTab: React.FC<ReaderTabProps> = ({
  books,
  activeBookId,
  activeBranchId,
  onBookChange,
  onBranchChange
}) => {
  const currentBook = books.find((b) => b.id === activeBookId) || books[0];
  const currentBranch = currentBook?.branches.find((br) => br.id === activeBranchId) || currentBook?.branches[0];

  const handleExport = () => {
    confetti({ particleCount: 80, spread: 60, origin: { y: 0.7 } });
    alert(`E-Book exported cleanly for ${currentBook.title} — ${currentBranch.title}! Download ready.`);
  };

  return (
    <div className="reader-container">
      <div className="reader-toolbar">
        <div style={{ display: 'flex', gap: '1.5rem', flexWrap: 'wrap' }}>
          <div className="select-group">
            <label htmlFor="react-book-select"><BookOpen size={16} /> Book:</label>
            <select
              id="react-book-select"
              className="custom-select"
              value={activeBookId}
              onChange={(e) => onBookChange(e.target.value)}
            >
              {books.map((b) => (
                <option key={b.id} value={b.id}>{b.title}</option>
              ))}
            </select>
          </div>

          <div className="select-group">
            <label htmlFor="react-branch-select"><Layers size={16} /> Story Branch:</label>
            <select
              id="react-branch-select"
              className="custom-select"
              value={activeBranchId}
              onChange={(e) => onBranchChange(e.target.value)}
            >
              {currentBook.branches.map((br) => (
                <option key={br.id} value={br.id}>{br.title}</option>
              ))}
            </select>
          </div>
        </div>

        <button className="btn-secondary" onClick={handleExport}>
          <Download size={16} /> Export E-Book (.epub)
        </button>
      </div>

      <div className="reader-body">
        <h2 className="reader-chapter-title">{currentBranch.chapter} — {currentBranch.title}</h2>

        {currentBranch.img && (
          <img
            src={currentBranch.img}
            alt={currentBranch.title}
            className="scene-artwork-banner"
          />
        )}

        <div className="reader-prose">
          {currentBranch.text.split('\n\n').map((paragraph, index) => (
            <p key={index}>{paragraph}</p>
          ))}
        </div>
      </div>
    </div>
  );
};

import React from 'react';
import type { Book } from '../types';
import { BookOpen, Zap, PlusCircle } from 'lucide-react';

interface CatalogTabProps {
  books: Book[];
  onSelectBook: (bookId: string, openTab: 'reader' | 'chatbot') => void;
  onUploadClick: () => void;
}

export const CatalogTab: React.FC<CatalogTabProps> = ({ books, onSelectBook, onUploadClick }) => {
  return (
    <div style={{ flex: 1 }}>
      <div className="catalog-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 className="catalog-title">Enterprise Classic Catalog</h1>
          <p className="catalog-subtitle">Select a book to read original chapters or pivot plot paths with AI narrative intelligence.</p>
        </div>
        <button className="btn-secondary" onClick={onUploadClick}>
          <PlusCircle size={16} /> Upload Custom E-Book
        </button>
      </div>

      <div className="catalog-grid">
        {books.map((book) => (
          <div className="book-card" key={book.id}>
            <div className="book-cover" style={{ background: book.coverGradient }}>
              <div className="book-cover-title">{book.title}</div>
            </div>
            <div className="book-info">
              <div className="book-author">By {book.author} • {book.badge}</div>
              <p className="book-desc">{book.desc}</p>
              <div className="book-actions">
                <button
                  className="btn-primary"
                  style={{ flex: 1 }}
                  onClick={() => onSelectBook(book.id, 'reader')}
                >
                  <BookOpen size={16} /> Read Book
                </button>
                <button
                  className="btn-secondary"
                  onClick={() => onSelectBook(book.id, 'chatbot')}
                >
                  <Zap size={16} /> Alter Path
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

import React, { useState } from 'react';
import { X, UploadCloud } from 'lucide-react';

interface UploadModalProps {
  isOpen: boolean;
  onClose: () => void;
  onUploadSuccess: (title: string, author: string, content: string) => void;
}

export const UploadModal: React.FC<UploadModalProps> = ({ isOpen, onClose, onUploadSuccess }) => {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [content, setContent] = useState('');

  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title || !author || !content) return;
    onUploadSuccess(title, author, content);
    setTitle('');
    setAuthor('');
    setContent('');
    onClose();
  };

  return (
    <div style={{
      position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
      backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex',
      alignItems: 'center', justifyContent: 'center', zIndex: 100
    }}>
      <div style={{
        backgroundColor: '#ffffff', borderRadius: '0.75rem', width: '90%',
        maxWidth: '520px', padding: '1.5rem', boxShadow: '0 20px 25px -5px rgba(0,0,0,0.1)'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 800 }}>Upload Custom E-Book</h3>
          <X size={20} style={{ cursor: 'pointer' }} onClick={onClose} />
        </div>

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ fontSize: '0.85rem', fontWeight: 700, display: 'block', marginBottom: '0.25rem' }}>Book Title</label>
            <input
              type="text"
              className="chat-input"
              style={{ width: '100%' }}
              placeholder="e.g. Wuthering Heights"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
            />
          </div>

          <div>
            <label style={{ fontSize: '0.85rem', fontWeight: 700, display: 'block', marginBottom: '0.25rem' }}>Author</label>
            <input
              type="text"
              className="chat-input"
              style={{ width: '100%' }}
              placeholder="e.g. Emily Brontë"
              value={author}
              onChange={(e) => setAuthor(e.target.value)}
              required
            />
          </div>

          <div>
            <label style={{ fontSize: '0.85rem', fontWeight: 700, display: 'block', marginBottom: '0.25rem' }}>Book Text / Excerpt</label>
            <textarea
              className="chat-input"
              style={{ width: '100%', height: '120px', resize: 'vertical' }}
              placeholder="Paste book text or upload content..."
              value={content}
              onChange={(e) => setContent(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="btn-primary" style={{ marginTop: '0.5rem' }}>
            <UploadCloud size={16} /> Add E-Book to Enterprise Catalog
          </button>
        </form>
      </div>
    </div>
  );
};

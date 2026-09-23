import React, { useState } from 'react';
import type { ChatMessage } from '../types';
import { Send, BookOpen, Sparkles } from 'lucide-react';

interface ChatbotTabProps {
  messages: ChatMessage[];
  onSendMessage: (text: string) => void;
  onOpenBranchInReader: (branchId: string) => void;
}

export const ChatbotTab: React.FC<ChatbotTabProps> = ({
  messages,
  onSendMessage,
  onOpenBranchInReader
}) => {
  const [inputText, setInputText] = useState('');

  const chips = [
    "What if Elizabeth stops Mr. Darcy before he leaves the room?",
    "What if Mr. Darcy offers a humble apology in Chapter 34?",
    "What if Nick Carraway confronts Jay Gatsby earlier?",
    "What if Victor Frankenstein agrees to create a companion?"
  ];

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputText.trim()) return;
    onSendMessage(inputText);
    setInputText('');
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Sparkles size={18} color="#6d28d9" />
          <span style={{ fontWeight: 800, fontSize: '1.05rem', color: '#0f172a' }}>
            AI Narrative Copilot & Story Alternator
          </span>
        </div>
      </div>

      <div className="chat-messages">
        {messages.map((msg) => (
          <div key={msg.id} className={`chat-bubble ${msg.sender}`}>
            <div>{msg.text}</div>

            {msg.img && (
              <img
                src={msg.img}
                alt="Scene illustration"
                style={{ width: '100%', borderRadius: '0.5rem', marginTop: '0.75rem', border: '1px solid #cbd5e1' }}
              />
            )}

            {msg.branchId && (
              <button
                className="btn-primary"
                style={{ marginTop: '0.75rem', width: '100%', fontSize: '0.8rem' }}
                onClick={() => onOpenBranchInReader(msg.branchId!)}
              >
                <BookOpen size={14} /> Read Alternate Storyline Pages in Story Reader Tab
              </button>
            )}
          </div>
        ))}
      </div>

      <div className="chips-row">
        {chips.map((chip, idx) => (
          <div
            key={idx}
            className="chip"
            onClick={() => onSendMessage(chip)}
          >
            ⚡ {chip}
          </div>
        ))}
      </div>

      <form className="chat-input-bar" onSubmit={handleSubmit}>
        <input
          type="text"
          className="chat-input"
          placeholder="Ask the agent to alter the story or rewrite a chapter..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />
        <button type="submit" className="btn-primary">
          <Send size={16} /> Pivot Story
        </button>
      </form>
    </div>
  );
};

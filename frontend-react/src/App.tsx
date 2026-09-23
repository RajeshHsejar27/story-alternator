import { useState } from 'react';
import type { Book, ChatMessage } from './types';
import { Navbar } from './components/Navbar';
import { CatalogTab } from './components/CatalogTab';
import { ReaderTab } from './components/ReaderTab';
import { StoryTreeFlowchartTab } from './components/StoryTreeFlowchartTab';
import { ChatbotTab } from './components/ChatbotTab';
import { UploadModal } from './components/UploadModal';

const initialBooks: Book[] = [
  {
    id: "pride_and_prejudice",
    title: "Pride and Prejudice",
    author: "Jane Austen",
    coverGradient: "linear-gradient(135deg, #4f46e5, #7c3aed)",
    badge: "Classic Romance",
    desc: "Elizabeth Bennet navigates issues of manners, upbringing, and marriage in Regency England.",
    activeBranchId: "pride_orig",
    branches: [
      {
        id: "pride_orig",
        title: "Original Chapter 34",
        chapter: "Chapter 34",
        img: "https://storage.googleapis.com/story-alternator-media-qwiklabs-gcp-02-f255a355adec/scene_e94e0ab1.jpg",
        text: `Elizabeth was sitting by herself, reading Jane's letters again, and finding little in them to console her. She was suddenly disturbed by the sound of the door bell, and her surprise was great on finding it to be Mr. Darcy. He entered the room in a hurried manner, and inquired after her health, imputing his visit to a wish of hearing that she were better.\n\nHe sat down for a few moments, and then getting up, walked about the room. Elizabeth was surprised, but said not a word. After a silence of several minutes, he came towards her in an agitated manner, and thus began:\n\n"In vain have I struggled. It will not do. My feelings will not be repressed. You must allow me to tell you how ardently I admire and love you." Elizabeth's astonishment was beyond expression.`
      },
      {
        id: "pride_apology",
        title: "Darcy's Humble Apology",
        chapter: "Chapter 34 Alternate",
        img: "https://storage.googleapis.com/story-alternator-media-qwiklabs-gcp-02-f255a355adec/scene_e94e0ab1.jpg",
        text: `Mr. Darcy paused at the doorway, his posture softening as Elizabeth's sharp words hung in the air. Instead of leaving in wounded pride, he turned back to face her with quiet humility.\n\n"Miss Bennet," he said softly, "I realize now how deeply my pride has blinded me to the distress I have caused. I ask for your patience to let me explain my actions regarding your sister and Mr. Wickham before I take my leave forever." Elizabeth looked at him, surprised by the sudden vulnerability in his voice.`
      },
      {
        id: "pride_stopped",
        title: "Elizabeth Stops Mr. Darcy",
        chapter: "Chapter 34 Divergence",
        img: "https://storage.googleapis.com/story-alternator-media-qwiklabs-gcp-02-f255a355adec/scene_e94e0ab1.jpg",
        text: `The air in the Hunsford parsonage drawing-room was thick with the weight of unspoken recriminations. Mr. Darcy, his face a mask of wounded dignity, turned to quit the room. Yet, as his hand touched the doorknob, Elizabeth called out sharply:\n\n"Mr. Darcy! I believe there is more to be said. If my beliefs regarding your treatment of my sister and Mr. Wickham are founded upon misapprehension, then it is incumbent upon you to offer a defence." Mr. Darcy stopped, released the doorknob, and stepped back into the room.`
      }
    ]
  },
  {
    id: "great_gatsby",
    title: "The Great Gatsby",
    author: "F. Scott Fitzgerald",
    coverGradient: "linear-gradient(135deg, #059669, #0d9488)",
    badge: "Modernist Classic",
    desc: "Jay Gatsby's obsessive pursuit of Daisy Buchanan amidst the roaring twenties.",
    activeBranchId: "gatsby_orig",
    branches: [
      {
        id: "gatsby_orig",
        title: "Original Chapter 5 (Reunion)",
        chapter: "Chapter 5",
        img: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",
        text: `Gatsby, his hands still in his pockets, was reclining against the mantelpiece in a strained counterfeit of perfect ease. His head leaned back so far that it rested against the face of an extinct mantelpiece clock.\n\n"We've met before," muttered Gatsby. His eyes met Nick's, and a faint smile crossed his face.`
      },
      {
        id: "gatsby_confrontation",
        title: "Gatsby Confronts Tom Early",
        chapter: "Chapter 7 Alternate",
        img: "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",
        text: `Instead of waiting for the hot afternoon in New York, Gatsby walked directly up the steps of Tom Buchanan's estate in East Egg, demanding an open conversation regarding Daisy's future.`
      }
    ]
  },
  {
    id: "frankenstein",
    title: "Frankenstein",
    author: "Mary Shelley",
    coverGradient: "linear-gradient(135deg, #d97706, #b45309)",
    badge: "Gothic Horror",
    desc: "Victor Frankenstein creates a sentient creature with unforeseen catastrophic consequences.",
    activeBranchId: "frankenstein_orig",
    branches: [
      {
        id: "frankenstein_orig",
        title: "Original Summit Encounter",
        chapter: "Chapter 10",
        img: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=800&q=80",
        text: `It was nearly noon when I reached the summit of the Montanvert. I suddenly beheld the figure of a man, advancing towards me with superhuman speed. The stature of the man exceeded that of a man. It was the wretch whom I had created.`
      },
      {
        id: "frankenstein_pact",
        title: "The Peaceful Pact",
        chapter: "Chapter 10 Alternate",
        img: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=800&q=80",
        text: `Victor listened to the creature's impassioned plea with a newfound sense of empathy, agreeing to construct a companion in exchange for a peaceful retreat to South America.`
      }
    ]
  }
];

export function App() {
  const [activeTab, setActiveTab] = useState<'catalog' | 'reader' | 'flowchart' | 'chatbot'>('catalog');
  const [books, setBooks] = useState<Book[]>(initialBooks);
  const [activeBookId, setActiveBookId] = useState<string>("pride_and_prejudice");
  const [activeBranchId, setActiveBranchId] = useState<string>("pride_orig");
  const [isUploadOpen, setIsUploadOpen] = useState(false);

  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: '1',
      sender: 'agent',
      text: "Greetings! I am your AI Story Alternator Copilot. Select a book, choose a pivot scenario chip, or ask me to alter any plotline in authentic literary style!"
    }
  ]);

  const activeBook = books.find((b) => b.id === activeBookId) || books[0];

  const handleSelectBook = (bookId: string, openTab: 'reader' | 'chatbot') => {
    const book = books.find((b) => b.id === bookId);
    if (book) {
      setActiveBookId(book.id);
      setActiveBranchId(book.branches[0].id);
      setActiveTab(openTab);
    }
  };

  const handleSendMessage = (text: string) => {
    const userMsg: ChatMessage = { id: Date.now().toString(), sender: 'user', text };
    setMessages((prev) => [...prev, userMsg]);

    setTimeout(() => {
      const agentMsg: ChatMessage = {
        id: (Date.now() + 1).toString(),
        sender: 'agent',
        text: `Here is the modified story branch for "${text}". Elizabeth Bennett stood resolutely as Mr. Darcy turned back at the threshold, altering the course of Regency history.`,
        branchId: 'pride_stopped',
        img: 'https://storage.googleapis.com/story-alternator-media-qwiklabs-gcp-02-f255a355adec/scene_e94e0ab1.jpg'
      };
      setMessages((prev) => [...prev, agentMsg]);
    }, 1200);
  };

  const handleOpenBranchInReader = (branchId: string) => {
    setActiveBranchId(branchId);
    setActiveTab('reader');
  };

  const handleUploadSuccess = (title: string, author: string, content: string) => {
    const newBookId = `upload_${Date.now()}`;
    const newBranchId = `${newBookId}_orig`;
    const newBook: Book = {
      id: newBookId,
      title,
      author,
      coverGradient: "linear-gradient(135deg, #ec4899, #8b5cf6)",
      badge: "Custom Upload",
      desc: `Uploaded e-book: ${title}`,
      activeBranchId: newBranchId,
      branches: [
        {
          id: newBranchId,
          title: "Uploaded Book Chapter 1",
          chapter: "Chapter 1",
          img: "",
          text: content
        }
      ]
    };
    setBooks((prev) => [newBook, ...prev]);
    setActiveBookId(newBookId);
    setActiveBranchId(newBranchId);
    setActiveTab('reader');
  };

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Navbar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        activeBookTitle={activeBook.title}
      />

      <main className="main-content">
        {activeTab === 'catalog' && (
          <CatalogTab
            books={books}
            onSelectBook={handleSelectBook}
            onUploadClick={() => setIsUploadOpen(true)}
          />
        )}

        {activeTab === 'reader' && (
          <ReaderTab
            books={books}
            activeBookId={activeBookId}
            activeBranchId={activeBranchId}
            onBookChange={(bId) => {
              setActiveBookId(bId);
              const b = books.find((x) => x.id === bId);
              if (b) setActiveBranchId(b.branches[0].id);
            }}
            onBranchChange={setActiveBranchId}
          />
        )}

        {activeTab === 'flowchart' && (
          <StoryTreeFlowchartTab
            books={books}
            activeBookId={activeBookId}
            onBranchSelect={(brId) => {
              setActiveBranchId(brId);
              setActiveTab('reader');
            }}
          />
        )}

        {activeTab === 'chatbot' && (
          <ChatbotTab
            messages={messages}
            onSendMessage={handleSendMessage}
            onOpenBranchInReader={handleOpenBranchInReader}
          />
        )}
      </main>

      <UploadModal
        isOpen={isUploadOpen}
        onClose={() => setIsUploadOpen(false)}
        onUploadSuccess={handleUploadSuccess}
      />
    </div>
  );
}

export default App;

export interface Branch {
  id: string;
  title: string;
  chapter: string;
  img: string;
  text: string;
}

export interface Book {
  id: string;
  title: string;
  author: string;
  coverGradient: string;
  badge: string;
  desc: string;
  activeBranchId: string;
  branches: Branch[];
}

export interface ChatMessage {
  id: string;
  sender: 'user' | 'agent';
  text: string;
  branchId?: string;
  img?: string;
}

import { useState } from "react";
import ChatHeader from "./ChatHeader";
import ChatMessages from "./ChatMessages";
import ChatInput from "./ChatInput";
import { sendChatMessage } from "../services/api";

function cleanAnswer(answer) {
  const fallback = "The information is not available in the provided college data.";
  return answer.replace(fallback, "").trim();
}

export default function ChatContainer() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function handleSend(query) {
    if (!query.trim()) return;

    setMessages((prev) => [...prev, { role: "user", text: query }]);
    setLoading(true);

    try {
      const data = await sendChatMessage(query);
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: cleanAnswer(data.answer),
          sources: data.sources,
        },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: "Something went wrong. Please try again." },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="w-full max-w-3xl h-[85vh] bg-slate-900 rounded-2xl shadow-xl flex flex-col">
      <ChatHeader />
      <ChatMessages messages={messages} loading={loading} />
      <ChatInput onSend={handleSend} disabled={loading} />
    </div>
  );
}
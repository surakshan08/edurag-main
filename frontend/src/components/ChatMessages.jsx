import { useEffect, useRef } from "react";
import TypingIndicator from "./TypingIndicator";
import MessageBubble from "./MessageBubble";

export default function ChatMessages({ messages, loading }) {
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  return (
    <div className="flex-1 px-6 py-4 overflow-y-auto">
      {messages.map((msg, idx) => (
        <MessageBubble key={idx} {...msg} />
      ))}

      {loading && <TypingIndicator />}

      <div ref={bottomRef} />
    </div>
  );
}
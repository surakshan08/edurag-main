import { useEffect, useState } from "react";

export default function TypingIndicator() {
  const [dots, setDots] = useState("");

  useEffect(() => {
    const interval = setInterval(() => {
      setDots((prev) => (prev.length === 3 ? "" : prev + "."));
    }, 500);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="text-slate-400 text-sm mt-2">
      Assistant is thinking{dots}
    </div>
  );
}
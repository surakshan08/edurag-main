import SourceBadge from "./SourceBadge";
import { getConfidence } from "../utils/confidence";

export default function MessageBubble({ role, text, sources }) {
  const isUser = role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-4`}>
      <div className={`max-w-[75%] px-4 py-3 rounded-xl text-sm ${
        isUser ? "bg-indigo-600 text-white" : "bg-slate-800 text-slate-100"
      }`}>
        <div>{text}</div>

        {!isUser && sources && (
          <div className="mt-3 border-t border-slate-700 pt-2 space-y-2">
            <div className="flex gap-2 flex-wrap">
              {sources.map((s, i) => (
                <SourceBadge key={i} category={s.category} />
              ))}
            </div>
            <div className="text-xs text-slate-400">
              Confidence: {getConfidence(sources[0].distance)}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
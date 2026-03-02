import { useState } from "react";

export default function ChatInput({ onSend, disabled }) {
  const [value, setValue] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    if (disabled || !value.trim()) return;
    onSend(value);
    setValue("");
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="p-4 border-t border-slate-200 bg-white rounded-b-2xl"
    >
      <div className="relative flex items-center">
        <input
          type="text"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          disabled={disabled}
          placeholder={disabled ? "Assistant is thinking..." : "Type your question..."}
          className="
            w-full
            bg-slate-50
            border
            border-slate-200
            rounded-xl
            px-4
            py-3
            pr-12
            text-sm
            focus:outline-none
            focus:ring-2
            focus:ring-indigo-500
            disabled:opacity-50
            disabled:cursor-not-allowed
          "
        />

        <button
          type="submit"
          disabled={disabled}
          className="
            absolute
            right-2
            p-2
            rounded-lg
            bg-indigo-500
            text-white
            hover:bg-indigo-600
            disabled:opacity-50
            disabled:cursor-not-allowed
            transition
          "
          title="Send"
        >
          ➤
        </button>
      </div>
    </form>
  );
}
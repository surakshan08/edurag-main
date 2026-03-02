import axios from "axios";

const API_URL = "https://edurag-main-production.up.railway.app/chat";

export async function sendChatMessage(query) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query }),
  });

  if (!response.ok) {
    throw new Error("Failed to fetch response");
  }

  return await response.json();
}
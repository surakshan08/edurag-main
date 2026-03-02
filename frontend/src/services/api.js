import axios from "axios";

const API_BASE = "https://e934-2401-4900-882e-d6f1-a95b-5b04-96b1-770e.ngrok-free.app";

export async function sendChatMessage(query) {
  const response = await axios.post(`${API_BASE}/chat`, {
    query,
  });
  return response.data;
}
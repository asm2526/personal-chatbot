import { useState } from "react";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    // Add user message
    setMessages((prev) => [...prev, { sender: "You", text: input }]);

    try {
      // Call FastAPI backend (proxy in package.json handles base URL)
      const response = await fetch("/api/message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });

      const data = await response.json();

      // Add bot reply
      setMessages((prev) => [...prev, { sender: "Bot", text: data.reply }]);
    } catch (err) {
      setMessages((prev) => [...prev, { sender: "Bot", text: "Error: " + err.message }]);
    }

    setInput("");
  };

  return (
    <div style={{ maxWidth: "600px", margin: "40px auto", fontFamily: "Arial, sans-serif" }}>
      <h2>Algo Chatbot</h2>
      <div style={{ border: "1px solid #ccc", padding: "10px", height: "400px", overflowY: "auto" }}>
        {messages.map((msg, idx) => (
          <div key={idx} style={{ margin: "5px 0" }}>
            <b>{msg.sender}:</b> {msg.text}
          </div>
        ))}
      </div>
      <div style={{ marginTop: "10px", display: "flex" }}>
        <input
          style={{ flex: 1, padding: "10px" }}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
          onKeyPress={(e) => e.key === "Enter" && sendMessage()}
        />
        <button onClick={sendMessage} style={{ padding: "10px 20px" }}>
          Send
        </button>
      </div>
    </div>
  );
}

export default App;

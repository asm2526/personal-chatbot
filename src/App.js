/**
 * React frontend for Algo Chatbot
 * this component renders a simple chat UI where users can type messages,
 * send them to FastAPI backend, and display bot responses
 */


import { useState } from "react";

function App() {
    //state to hold the conversation
  const [messages, setMessages] = useState([]);
  // state to hold the current input from the user
  const [input, setInput] = useState("");

    /**
     * Handles sending a message to backend.
     * 1. Adds the user's message to chat history.
     * 2. Sends a POST request to FastAPI
     * 3. Adds the bot's repy to chat history
     */
  const sendMessage = async () => {
    // Prevent sending empty messages
    if (!input.trim()) return;

    // Add user message to chat history
    setMessages((prev) => [...prev, { sender: "You", text: input }]);

    try {
        // Send the message to FastAPI backend
        // Proxy is set in package.json, so we can use relative path api/message
      const response = await fetch("/api/message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });
      // parse the JSON reply
      const data = await response.json();

      // Add bot reply to chat history
      setMessages((prev) => [...prev, { sender: "Bot", text: data.reply }]);
    } catch (err) {
        // handle network or server errors gracefully
      setMessages((prev) => [...prev, { sender: "Bot", text: "Error: " + err.message }]);
    }
    // clear the input box after sending
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

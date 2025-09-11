/**
 * React frontend for Algo Chatbot
 * Features:
 * - Chat bubbles (user right, bot left)
 * - Auto-scroll to bottom of container
 * - Autofocus input
 * - Handles both reply + error responses
 */

import { Link, Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Chat from "./Chat";
import Intents from "./Intents";

function App() {
    return (
        <Router>
            <nav style={{ display: "flex", gap: "20px", padding: "10px", borderBottom: "1px solid #ccc"}}>
                <Link to="/">Chat</Link>
                <Link to="/intents">Manage Intents</Link>
            </nav>

            <Routes>
                <Route path="/" element={<Chat />} />
                <Route path="/intents" element={<Intents />} />
            </Routes>
        </Router>
    );
}

export default App;
/** 
import { useEffect, useLayoutEffect, useRef, useState } from "react";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  // Ref for the scrollable chat container
  const chatContainerRef = useRef(null);
  // Ref to keep input focused
  const inputRef = useRef(null);

  // Auto-scroll when messages update
  useLayoutEffect(() => {
    if (chatContainerRef.current) {
      const container = chatContainerRef.current;
      container.scrollTop = container.scrollHeight;
    }
  }, [messages]);

  // Autofocus input
  useEffect(() => {
    inputRef.current?.focus();
  }, [messages]);

  // Send message handler
  const sendMessage = async () => {
    if (!input.trim()) return;

    try {
      const response = await fetch("/api/message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        { sender: "You", text: input },
        {
          sender: "Bot",
          text:
            data.reply ||
            data.message ||
            "I don't understand yet.",
        },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: "You", text: input },
        { sender: "Bot", text: "Error: " + err.message },
      ]);
    }

    setInput("");
  };

  return (
    <div
      style={{
        maxWidth: "600px",
        margin: "40px auto",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h2 style={{ textAlign: "center" }}>Algo Chatbot</h2>

      <div
        ref={chatContainerRef}
        style={{
          border: "1px solid #ccc",
          padding: "10px",
          height: "400px",        // fixed height
          maxHeight: "400px",     // prevent growing
          overflowY: "scroll",    // force scrollbar
          backgroundColor: "#f9f9f9",
        }}
      >
        {messages.map((msg, idx) => (
          <div
            key={idx}
            style={{
              display: "flex",
              justifyContent: msg.sender === "You" ? "flex-end" : "flex-start",
              margin: "5px 0",
            }}
          >
            <div
              style={{
                padding: "10px",
                borderRadius: "15px",
                maxWidth: "70%",
                backgroundColor: msg.sender === "You" ? "#007bff" : "#e5e5ea",
                color: msg.sender === "You" ? "white" : "black",
              }}
            >
              {msg.text}
            </div>
          </div>
        ))}
      </div>

      <div style={{ marginTop: "10px", display: "flex" }}>
        <input
          ref={inputRef}
          style={{
            flex: 1,
            padding: "10px",
            borderRadius: "5px",
            border: "1px solid #ccc",
          }}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
          onKeyPress={(e) => e.key === "Enter" && sendMessage()}
        />
        <button
          onClick={sendMessage}
          style={{
            marginLeft: "10px",
            padding: "10px 20px",
            border: "none",
            borderRadius: "5px",
            backgroundColor: "#007bff",
            color: "white",
            cursor: "pointer",
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default App;
*/
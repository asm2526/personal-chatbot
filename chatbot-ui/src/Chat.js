import { useEffect, useLayoutEffect, useRef, useState } from "react";

function Chat() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    // Ref for the chat container
    const chatContainerRef = useRef(null);
    // Ref to keep input foucsed
    const inputRef = useRef(null);

    // Auto-scroll to bottom when messages update
    useLayoutEffect(() => {
        if (chatContainerRef.current) {
            const container = chatContainerRef.current;
            container.scrollTop = container.scrollHeight;
        }
    }, [messages]);

    // Autofocus input
    useEffect(() => {
        inputRef.current?.focus();
    }, [messages])

    //Handle sending message
    const sendMessage = async () => {
        if (!input.trim()) return;

        try {
            const response = await fetch("/api/message", {
                method: "POST",
                headers: { "Content-Type": "application/json"},
                body: JSON.stringify({message: input}),
            });

            const data = await response.json();

            setMessages((prev) => [
                ...prev,
                { sender: "You", text: input},
                { sender: "Bot",
                    text:
                        data.reply || //normal bot reply
                        data.message || // backend error respons
                        "I don't understand yet", //fallback
                },
            ]);
        } catch (err) {
            setMessages((prev) => [
                ...prev,
                { sender: "You", text: input},
                { sender: "Bot", text: "Error: " + err.message},
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

      {/* Chat container */}
      <div
        ref={chatContainerRef}
        style={{
          border: "1px solid #ccc",
          padding: "10px",
          height: "400px",
          maxHeight: "400px",
          overflowY: "scroll",
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

      {/* Input box */}
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

export default Chat;
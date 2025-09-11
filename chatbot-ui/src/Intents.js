import { useEffect, useState } from "react";

function Intents() {
    const [intents, setIntents] = useState([]);
    const [newIntent, setNewIntent] = useState("");
    const [newResponses, setNewResponses] = useState("");
    const [newExamples, setNewExamples] = useState("")

    // new editing state
    const [editingIntent, setEditingIntent] = useState(null);
    const [editResponses, setEditResponses] = useState("");
    const [editExamples, setEditExamples] = useState("");

    // Load all intents
    useEffect(() => {
        fetch("/api/intent")
        .then((res) => res.json())
        .then(setIntents)
        .catch((err) => console.error("Error fetching intents:", err));
    }, []);

    // Add a new intent
    const addIntent = async () => {
        if (!newIntent.trim() || !newResponses.trim()) {
            alert("Intent name and at least one response are required");
            return;
        }

        const intent = {
            intent: newIntent,
            responses: newResponses.split(",").map((r) => r.trim()),
            examples: newExamples
                ? newExamples.split(",").map((e) => e.trim())
                : [],
        };

        const res = await fetch("/api/intent", {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify(intent),
        })

        if (res.ok) {
            setIntents([...intents, intent]);
            setNewIntent("");
            setNewResponses("");
            setNewExamples("");
        } else {
            console.error("Failed to add intent")
        }
    };

    // Delete an intent
    const deleteIntent = async (name) => {
        await fetch(`/api/intent/${name}`, { method: "DELETE" });
        setIntents(intents.filter((i) => i.intent !== name));
    };

    // update intent
    const saveEdit = async (name) => {
    const updated = {
      intent: name,
      responses: editResponses.split(",").map((r) => r.trim()),
      examples: editExamples ? editExamples.split(",").map((e) => e.trim()) : [],
    };

    const res = await fetch(`/api/intent/${name}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(updated),
    });

    if (res.ok) {
      setIntents(
        intents.map((i) => (i.intent === name ? updated : i))
      );
      setEditingIntent(null); // exit edit mode
      setEditResponses("");
      setEditExamples("");
    } else {
      console.error("Failed to update intent");
    }
  };

   
    return (
    <div style={{ padding: "20px" }}>
      <h2>Manage Intents</h2>

      {/* Add Intent Form */}
      <div style={{ marginBottom: "20px" }}>
        <input
          value={newIntent}
          onChange={(e) => setNewIntent(e.target.value)}
          placeholder="Intent name"
        />
        <input
          value={newResponses}
          onChange={(e) => setNewResponses(e.target.value)}
          placeholder="Responses (comma separated)"
        />
        <input
          value={newExamples}
          onChange={(e) => setNewExamples(e.target.value)}
          placeholder="Examples (comma separated)"
        />
        <button onClick={addIntent}>Add Intent</button>
      </div>

      {/* List Intents */}
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Intent</th>
            <th>Responses</th>
            <th>Examples</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {intents.map((i, idx) => (
            <tr key={idx}>
              <td>{i.intent}</td>
              <td>
                {editingIntent === i.intent ? (
                  <input
                    value={editResponses}
                    onChange={(e) => setEditResponses(e.target.value)}
                    placeholder="Edit responses"
                  />
                ) : (
                  i.responses.join(", ")
                )}
              </td>
              <td>
                {editingIntent === i.intent ? (
                  <input
                    value={editExamples}
                    onChange={(e) => setEditExamples(e.target.value)}
                    placeholder="Edit examples"
                  />
                ) : (
                  i.examples?.join(", ") || ""
                )}
              </td>
              <td>
                {editingIntent === i.intent ? (
                  <>
                    <button onClick={() => saveEdit(i.intent)}>Save</button>
                    <button onClick={() => setEditingIntent(null)}>Cancel</button>
                  </>
                ) : (
                  <>
                    <button
                      onClick={() => {
                        setEditingIntent(i.intent);
                        setEditResponses(i.responses.join(", "));
                        setEditExamples(i.examples?.join(", ") || "");
                      }}
                    >
                      Edit
                    </button>
                    <button onClick={() => deleteIntent(i.intent)}>Delete</button>
                  </>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Intents;
# personal-chatbot
A chatbot backend built with Java (Spring Boot) + MongoDB, powered by advanced data structures and algorithms (tries, edit distance, TF-IDF, graph search).

To run
1. Activate local environment source .venv/bin/activate
2. uvicorn src.main:app --reload
3. Link: http://127.0.0.1:8000

Algo Chatbot

A Python FastAPI + MongoDB chatbot backend, powered by advanced data structures and algorithms.
Instead of relying only on AI/ML, this chatbot uses techniques like:

Edit Distance (Levenshtein) → fuzzy matching & typo correction

Tries / Prefix Trees → autocomplete & intent lookup

Inverted Index + TF-IDF → fast query search & ranking

Graph Search (BFS/DFS) → knowledge graph exploration

Heaps & Priority Queues → top-K best response selection

This project is designed as a practice ground for algorithms, backend engineering, and API design — inspired by platforms like LeetCode and HackerRank.

Features (Planned & Implemented)
FastAPI backend running locally
MongoDB integration for storing intents and responses
REST API to send and receive messages
Autocomplete for query suggestions (Trie)
Fuzzy string matching for typo handling
Ranking responses using TF-IDF
Graph-based knowledge relationships
Leaderboard system (like a mini LeetCode rank)

Tech Stack

Backend: FastAPI
Database: MongoDB
Language: Python 3.13
Algorithms & Data Structures: Tries, Graphs, Heaps, Edit Distance


Clone Repository
git clone https://github.com/asm2526/personal-chatbot.git
cd personal-chatbot

set up a virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

install dependencies
pip install -r requirements.txt

run the server
uvicorn src.main:app --reload


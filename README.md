##🎮 Game Recommendation System

# Overview
This project is a Game Recommendation System built using the Steam 200k dataset. It recommends games to users based on their playing behavior using Collaborative Filtering techniques.

#The system provides:
 Personalized recommendations (User-Based)
 Similar game suggestions (Item-Based)

An interactive web app is built using Streamlit.

# Features
✅ User-Based Collaborative Filtering
✅ Item-Based Collaborative Filtering
✅ Uses playtime as implicit feedback
✅ Interactive UI with Streamlit
✅ Real-time recommendations

# How It Works
1. Data Preprocessing
Removed "purchase" data
Used only "play" data (important for user interest)
Created a User-Game Matrix
2. Similarity Calculation
Used Cosine Similarity
Computed:
User-to-User similarity
Game-to-Game similarity
3. Recommendation Logic
🔹 User-Based
Find similar users
Recommend games they played
🔹 Game-Based
Select a game
Recommend similar games
🛠️ Tech Stack
Python
Pandas
Scikit-learn
Streamlit
📂 Project Structure
game-recommendation/
│
├── app.py              # Streamlit UI
├── model.py            # Recommendation logic
├── steam-200k.csv      # Dataset
├── requirements.txt    # Dependencies
└── README.md
▶️ Installation & Run
1. Clone Repository
git clone https://github.com/your-username/game-recommendation.git
cd game-recommendation
2. Install Dependencies
pip install -r requirements.txt
3. Run App
streamlit run app.py

👉 Open in browser:

http://localhost:8501


💡 Key Concepts
Collaborative Filtering
Cosine Similarity
Sparse Matrix Handling
Implicit Feedback System
 Future Improvements
 Better UI (cards, images, dark theme)
 Popularity-based recommendations (cold start)
 Model evaluation (precision/recall)
 Deployment (Streamlit Cloud / Render)
 
 #Author
Ritik Roushan
BTech CSE Graduate
Interested in Data Science & ML
⭐ If You Like This Project

Give it a ⭐ on GitHub!

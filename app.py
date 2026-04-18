import streamlit as st
from models import *

st.title("🎮 Game Recommendation System")

# Load data
df = load_data()
user_game_matrix = create_matrix(df)

# Similarity
user_similarity_df = compute_similarity(user_game_matrix)
item_similarity_df = compute_item_similarity(user_game_matrix)

# Sidebar options
option = st.sidebar.selectbox(
    "Choose Recommendation Type",
    ["User-Based", "Game-Based"]
)

# -------------------------
# USER BASED
# -------------------------
if option == "User-Based":
    
    user_id = st.sidebar.number_input("Enter User ID", min_value=1)
    
    if st.sidebar.button("Recommend"):
        recs = recommend_games(user_id, user_game_matrix, user_similarity_df)
        
        st.subheader("Recommended Games 🎯")
        for game in recs:
            st.write(f"👉 {game}")

# -------------------------
# GAME BASED
# -------------------------
else:
    
    game_list = user_game_matrix.columns.tolist()
    
    selected_game = st.sidebar.selectbox("Select a Game", game_list)
    
    if st.sidebar.button("Find Similar Games"):
        
        recs = recommend_similar_games(selected_game, item_similarity_df)
        
        st.subheader(f"Games similar to {selected_game} 🎯")
        
        for game in recs:
            st.write(f"👉 {game}")


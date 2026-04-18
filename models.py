import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    df = pd.read_csv("steam-200k.csv", header=None)
    df.columns = ['user_id', 'game', 'behavior', 'hours', 'dummy']
    
    # Keep only play data
    df = df[df['behavior'] == 'play']
    
    return df

def create_matrix(df):
    user_game_matrix = df.pivot_table(
        index='user_id',
        columns='game',
        values='hours'
    ).fillna(0)
    
    return user_game_matrix

def compute_similarity(user_game_matrix):
    similarity = cosine_similarity(user_game_matrix)
    
    similarity_df = pd.DataFrame(
        similarity,
        index=user_game_matrix.index,
        columns=user_game_matrix.index
    )
    
    return similarity_df

def recommend_games(user_id, user_game_matrix, similarity_df, top_n=5):
    
    if user_id not in user_game_matrix.index:
        return ["User not found"]
    
    similar_users = similarity_df[user_id].sort_values(ascending=False)[1:6]
    
    similar_users_games = user_game_matrix.loc[similar_users.index]
    avg_scores = similar_users_games.mean(axis=0)
    
    user_games = user_game_matrix.loc[user_id]
    recommendations = avg_scores[user_games == 0]
    
    return recommendations.sort_values(ascending=False).head(top_n).index.tolist()


def compute_item_similarity(user_game_matrix):
    
    # Transpose matrix (game x user)
    game_user_matrix = user_game_matrix.T
    
    similarity = cosine_similarity(game_user_matrix)
    
    similarity_df = pd.DataFrame(
        similarity,
        index=game_user_matrix.index,
        columns=game_user_matrix.index
    )
    
    return similarity_df

def recommend_similar_games(game_name, item_similarity_df, top_n=5):
    
    if game_name not in item_similarity_df.index:
        return ["Game not found"]
    
    similar_games = item_similarity_df[game_name] \
    .sort_values(ascending=False)[1:top_n+1]
    
    return similar_games.index.tolist()
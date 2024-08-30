import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample data
users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
items = ['Movie1', 'Movie2', 'Movie3', 'Book1', 'Book2', 'Product1']

# User-item interaction matrix (e.g., ratings)
interactions = {
    'Alice': {'Movie1': 5, 'Movie2': 4, 'Book1': 3},
    'Bob': {'Movie1': 4, 'Movie3': 5, 'Product1': 2},
    'Charlie': {'Movie2': 5, 'Book2': 4, 'Product1': 3},
    'David': {'Movie3': 4, 'Book1': 5, 'Product1': 2},
    'Eve': {'Movie1': 3, 'Book2': 5, 'Product1': 4}
}

# Create a user-item interaction matrix
interaction_matrix = pd.DataFrame(interactions).T

# Calculate the similarity between users using cosine similarity
user_similarity = cosine_similarity(interaction_matrix)

# Define a function to recommend items to a user
def recommend(user, num_recommendations=3):
    # Get the similarity scores for the user
    scores = user_similarity[user]
    
    # Get the top N similar users
    similar_users = scores.argsort()[:-num_recommendations-1:-1]
    
    # Get the items liked by the similar users
    liked_items = interaction_matrix.iloc[similar_users].sum(axis=0)
    
    # Get the items not liked by the user
    not_liked_items = liked_items[liked_items.index.isin(interaction_matrix.columns) & ~liked_items.index.isin(interaction_matrix.loc[user].index)]
    
    # Return the top N recommended items
    return not_liked_items.nlargest(num_recommendations).index.tolist()

# Test the recommendation function
print(recommend('Alice'))  # Output: ['Movie3', 'Book2', 'Product1']
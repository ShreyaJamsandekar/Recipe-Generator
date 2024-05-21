import csv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import json

# Function to read recipes from CSV file
def read_recipes_from_csv(file_path):
    recipes = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            name = row[0]
            ingredients = row[1][2:-2].split("', '")
            instructions = row[3][2:-2].split("', '")
            time = int(row[2])
            cuisine_list = row[4].split(', ')
            cuisine = [i.lower() for i in cuisine_list]
            course = row[5].lower() # New addition for COURSE field
            recipes.append((name, ingredients, instructions, time, cuisine, course))  # Include course
    return recipes

def load_cuisine_courses(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def load_word_embeddings(file_path):
    word_embeddings = {}
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            embedding = np.array(values[1:], dtype='float32')
            word_embeddings[word] = embedding
    return word_embeddings

# Function to generate recipe vectors
def generate_recipe_vector(ingredients, instructions, word_embeddings):
    words = ingredients + instructions
    word_vectors = [word_embeddings.get(word, np.zeros(100)) for word in words]
    recipe_vector = np.mean(word_vectors, axis=0)
    return recipe_vector

# Function to retrieve top-k recipes given a query
def retrieve_recipes(query, recipe_vectors, word_embeddings, recipes, k=10):
    ingredient, max_time, cuisine, course = query
    query_vector = generate_recipe_vector([ingredient], [], word_embeddings)
    
    # Filter recipes based on cuisine, time, and course
    filtered_recipes = [recipe for recipe in recipes if cuisine.lower() in recipe[4] and recipe[3] <= max_time and ingredient.lower() in ' '.join(recipe[1]).lower() and course.lower() in recipe[5].lower()]
    
    if len(filtered_recipes) == 0:
        st.text("No recipes found matching the query ingredient, cuisine, and course.")
        return []
    
    # Get indices of filtered recipes
    filtered_indices = [recipes.index(recipe) for recipe in filtered_recipes]
    
    # Calculate similarity for filtered recipes
    similarities = [cosine_similarity([query_vector], [recipe_vectors[i]])[0][0] for i in filtered_indices]
    top_indices = np.argsort(similarities)[::-1][:k]
    
    top_recipes = [filtered_recipes[i] for i in top_indices]
    return top_recipes

# Load pre-trained word embeddings
word_embeddings = load_word_embeddings('glove.6B.100d.txt')

# Read recipes from CSV file
recipes = read_recipes_from_csv('recipes2.csv')  # Update file path to your CSV file

# Generate recipe vectors for all recipes
recipe_vectors = [generate_recipe_vector(ingredients, instructions, word_embeddings) for name, ingredients, instructions, time, cuisine, course in recipes]

# Load cuisine-course mapping from JSON file
cuisine_courses = load_cuisine_courses('cuisine.json')

# Sample query
st.text("Enter the ingredient, max time, and cuisine for the recipe you want to find:")
ingredient = st.text_input('Enter the ingredient')
max_time = st.slider('Enter the amount of time you have in minutes', 0, 50)
cuisine = st.selectbox('Choose the cuisine', list(cuisine_courses.keys()))

# Based on the selected cuisine, display the available courses
selected_cuisine_courses = cuisine_courses.get(cuisine.lower(), [])
course = st.selectbox('Choose the course', set(selected_cuisine_courses))

if st.button('Enter'):
    st.text("Please wait while we find the best recipe for you...")
    query = [ingredient, max_time, cuisine, course]

    # Retrieve and print top-k recipes
    top_recipes = retrieve_recipes(query, recipe_vectors, word_embeddings, recipes)
    for i, recipe in enumerate(top_recipes):
        st.text(f"Rank {i+1}: {recipe[0]}")
        st.markdown(f"Ingredients: {', '.join(recipe[1])}")
        st.markdown("Instructions:")
        for step in recipe[2]:
            st.markdown(step)
        st.text(f"Time: {recipe[3]} minutes")
        st.text(f"Cuisine: {', '.join(recipe[4])}")
        st.text(f"Course: {recipe[5]}")

        # Add an empty line between recipes
        st.text("")

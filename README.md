1 Introduction
The main aim is to create a Web-Crawler Based
Recipe Generator that will introduce enough filters
in a domain that it will help the user to find the
exact recipe that they are looking for. The model
will be fed recipes from different websites which it
will be able to structurize into a vector form. These
vector forms will be subjected to various filters that
will help the user decide the meal they want to
create.
2 Requirements
1) Python 3.8 or later
2) Pip upgraded version
3) Kaggle Stopwords Dataset - Glove.6B.100d.txt
4) Streamlit
3 Steps to run the project
1) Install pip and python
2) Download the Kaggle data set
(https://www.kaggle.com/datasets/danielwillgeorge/
glove6b100dtxt)
3) In the command prompt run the command
’streamlite run modelv1.py’
(vectorrmv1 is the python code project name -
please change accordingto the name you have
saved it as)
4) The project will open on your default browser or
On your browser copy the links Local URL:
http://localhost:8501
Network URL: http://10.203.21.74:8501 (please
note the server takes some time to load if it takes
too long I have
4 Explanation
4.1 Objectives
The primary purpose of this project is to simplify
the process of finding relevant recipes tailored to
users’ specific requirements. By leveraging web
scraping to gather a diverse range of recipes and
utilizing word embeddings to represent recipe data,
the system generates recipe vectors that enable efficient similarity-based search and recommendation.
The key objectives of this project include:
Data Collection: Extract recipe data from online sources, such as the Skinnytaste website,
using web scraping techniques to build a comprehensive recipe database. Recipe Representation: Utilizing word embeddings, specifically the
glove.6B.100d.txt dataset, to convert recipe ingredients and instructions into vector representations for
efficient computation and comparison. Recommendation System: Implementing a recommendation
algorithm based on cosine similarity of recipe vectors to provide top-k recipe suggestions to users
based on their input parameters (ingredient, max
time, cuisine, course). User Interface: Developing a user-friendly interface using Streamlit, allowing users to input their preferences and view
recommended recipes in a clear and accessible format. Through these objectives, the Web Crawler
Recipe Maker Generator project aims to enhance
the user experience in discovering and trying out
new recipes, catering to diverse culinary preferences and time constraints.
4.2 Technology
Libraries csv: Used for reading and writing CSV
files, as seen in the readrecipesfromcsv function.
numpy: Utilized for numerical computations and
array operations, such as generating recipe vectors and calculating cosine similarity. sklearn:
Specifically, the cosinesimilarity function from
sklearn.metrics.pairwise is used for calculating cosine similarity between vectors. streamlit: Employs
Streamlit as the framework for building the web application user interface. requests: Used for sending
HTTP requests and fetching data from URLs, as
seen in the web crawler part of the code. BeautifulSoup: Used for parsing HTML content and extracting data from web pages during web scraping.
Word Embeddings The project uses pre-trained
word embeddings from the glove.6B.100d.txt file.
These embeddings play a crucial role in representing recipes as vectors and calculating the similarity
between them.
4.3 Data Collection
Data Preprocessing Steps Fetching Recipe Links:
The web crawler was designed to navigate through
multiple pages of the Skinnytaste website, fetching
links to individual recipe pages. Extracting Recipe
Information: For each recipe link, the crawler extracted essential data elements such as ingredients,
instructions, cooking time, cuisine classification,
and course categorization. Data Cleaning and Formatting: Cleaning Ingredients and Instructions:
The extracted ingredients and instructions underwent cleaning to remove unwanted characters, such
as extra spaces, punctuation marks, and HTML
tags. Parsing Cooking Time: The cooking time information extracted from the website was parsed to
convert it into a standardized format, such as minutes. Standardizing Cuisine and Course: Cuisine
and course categorizations were standardized to ensure consistency and ease of processing during recommendation. Storing Data: The cleaned and formatted data was stored in a CSV file (recipes2.csv),
providing a structured repository of recipe information for the recipe maker generator application.
4.4 Architecture
In the recipe maker generator project, recipe representation plays a crucial role in enabling effective
recommendation systems. Here’s how the recipe
data is represented and utilized within the project:
Word Embeddings and Their Role: Word embeddings, such as the GloVe embeddings (Global
Vectors for Word Representation), are utilized in
this project. GloVe embeddings are pre-trained
word vectors that capture semantic relationships
between words based on their co-occurrence in
large text corpora. These word embeddings serve
as a foundational element for representing words in
a continuous vector space, allowing for meaningful
comparisons and computations between words and
phrases. Recipe Vector Generation: The project
employs word embeddings to generate vector representations for recipes. The ingredients and instructions of each recipe are tokenized and converted into word vectors using GloVe embeddings.
A recipe vector is then formed by averaging the
word vectors of ingredients and instructions, creating a comprehensive representation of the recipe in
the embedding space. This vectorization process
transforms qualitative recipe data into quantitative
vectors, facilitating similarity calculations and recommendation algorithms. Role of Recipe Vectors:
Recipe vectors encapsulate the essential characteristics of each recipe, including its ingredients,
cooking instructions, and semantic context. These
vectors enable efficient comparison and similarity assessments between different recipes based on
their vector representations. By leveraging recipe
vectors, the recommendation system can identify
recipes that closely match user preferences and
search criteria. Cosine Similarity for Recipe Comparison: Cosine similarity is utilized as a metric
to measure the similarity between recipe vectors.
Given a user query specifying ingredients, maximum cooking time, cuisine, and course preferences,
the system computes the cosine similarity between
the query’s recipe vector and the vectors of available recipes. Recipes with higher cosine similarity
scores are considered more similar to the user’s
query and are prioritized in the recommendation
list. Vectorized Recipe Space: The project operates
within a vectorized recipe space, where recipes are
represented as points in a high-dimensional vector space. This vector space facilitates efficient
retrieval and ranking of recipes based on their proximity and similarity to user-defined criteria. The
use of vector representations enhances the system’s
ability to provide personalized and relevant recipe
recommendations tailored to user preferences. By
employing word embeddings and generating recipe
vectors, the project transforms raw recipe data into
a structured and analyzable format, empowering
the recommendation system to deliver accurate and
personalized recipe suggestions to users
4.5 Reccomandation System
Recommendation System The recommendation
system in the web crawler recipe maker generator
project is designed to provide users with personalized and relevant recipe suggestions based on their
input parameters. Here’s an in-depth look at how
the recommendation system functions:
Input Parameters for Recipe Search: Users input several parameters to specify their recipe preferences: Ingredient: The main ingredient or key
ingredient desired in the recipe. Max Time: The
maximum amount of time the user is willing to
spend on cooking or preparation. Cuisine: The
preferred cuisine type, such as Italian, Mexican,
Indian, etc. Course: The course or meal type, such
as appetizer, main course, dessert, etc. Retrieval
Algorithm: The recommendation system utilizes
a retrieval algorithm based on cosine similarity
of recipe vectors. Upon receiving user input, the
system generates a recipe vector representing the
user’s query based on the specified ingredient. It
then calculates the cosine similarity between the
query vector and the vectors of all available recipes
in the dataset. Cosine similarity measures the angle between two vectors in the vector space, with
higher values indicating greater similarity. Top-k
Recipe Recommendation Process: After computing cosine similarities, the system identifies the
top-k recipes that closely match the user’s query.
The value of k determines the number of top recipes
to be recommended to the user, typically ranging
from 5 to 10. The top-k recipes are selected based
on their cosine similarity scores, with higher scores
indicating stronger relevance to the user’s preferences. User Interaction and Output Display: The
system provides a user-friendly interface, powered
by Streamlit, for users to input their recipe preferences. Input fields allow users to specify the ingredient, maximum cooking time, cuisine, and course.
Upon submitting the input, the system processes
the query, retrieves the top-k recommended recipes,
and displays them in an organized manner. Each
recommended recipe is presented with its name, ingredients, cooking instructions, cooking time, cuisine type, and course information. Users can easily
view and explore the recommended recipes, facilitating a seamless and engaging recipe discovery
experience. Dynamic and Real-time Recommendations: The recommendation system operates dynamically, providing real-time recommendations
based on user input. As users adjust their preferences or criteria, the system dynamically updates
the recommended recipes to reflect the changes.
This dynamic behavior enhances user interaction
and allows for instant feedback on recipe recommendations. By combining user input parameters,
cosine similarity calculations, and a top-k recommendation approach, the recommendation system
delivers accurate, personalized, and context-aware
recipe suggestions to users, enhancing their cooking and culinary exploration experiences.
4.6 Logic
Web Crawler Logic: The web crawler component is responsible for data collection from external sources, specifically recipe websites. It utilizes web scraping techniques to extract reciperelated information, including ingredients, cooking instructions, cooking time, cuisine, and course
details. The crawler starts by sending HTTP GET
requests to the target recipe website(s) using the
requests library in Python. Upon receiving the
HTML content of a page, the crawler parses it using BeautifulSoup, a Python library for parsing
HTML and XML documents. It identifies relevant
HTML elements such as recipe titles, ingredient
lists, cooking instructions, time estimates, cuisine
labels, and course types. The extracted data is
then processed and structured into a suitable format, typically a CSV file, for further analysis and
utilization by the recommendation model. Recommendation Model Logic: The recommendation
model operates on the processed recipe data obtained from the web crawler. It begins by loading pre-trained word embeddings, such as GloVe
embeddings (glove.6B.100d.txt), which represent
words as dense vectors in a high-dimensional space.
Recipe data from the CSV file is read and transformed into recipe vectors using the word embeddings. Each recipe vector captures the semantic
meaning and context of the ingredients and instructions. When a user interacts with the system
through the Streamlit interface, they input their
recipe preferences, including the main ingredient,
maximum cooking time, preferred cuisine, and
course type. The user’s input is used to generate a
query vector representing their recipe search criteria. The query vector is also constructed using the
loaded word embeddings. The recommendation
system calculates the cosine similarity between the
query vector and the recipe vectors of all available
recipes. Based on the cosine similarity scores, the
system retrieves the top-k recipes that best match
the user’s preferences and displays them in the
Streamlit interface. Flow of the Model: The overall
flow of the model can be summarized as follows:
Data collection: Web crawler collects recipe data
from external sources and stores it in a CSV file
(recipes2.csv). Data preprocessing: Recipe data is
preprocessed to extract relevant information and
prepare it for vectorization. Vectorization: Word
embeddings are used to convert ingredients and
instructions into dense vectors, creating recipe vectors. User interaction: Users input their recipe
preferences via the Streamlit application, specifying ingredient, time, cuisine, and course. Query
generation: User input is used to generate a query
vector representing the user’s recipe search criteria. Recommendation generation: Cosine similarity
is computed between the query vector and recipe
vectors to retrieve top-k recommended recipes. Display: The recommended recipes, along with their
details, are displayed in the Streamlit interface for
user exploration and selection. The architecture
seamlessly integrates web crawling for data acquisition and a recommendation model for personalized recipe suggestions, providing users with an
intuitive and efficient recipe discovery platform.
User Interface
The user interface (UI) of the web crawler recipe
maker generator project is built using Streamlit, a
Python library for creating interactive web applications. The UI plays a crucial role in facilitating user
interaction, inputting preferences, and displaying
recommended recipes. Here’s an overview of the
UI components and their functionalities:
Streamlit Application: The Streamlit application
serves as the frontend interface for users to interact
with the recipe recommendation system. Users access the application through a web browser, where
they are presented with input fields and output displays. Input Fields for User Preferences: Ingredient Input: Users can enter the main ingredient they
want to use for their recipe. This input is essential for generating personalized recommendations
based on ingredient preferences. Maximum Time
Input: Users specify the maximum amount of time
they are willing to spend on cooking or preparing the recipe. This time constraint helps filter out
recipes that exceed the user’s time limit. Cuisine Input: Users can select or enter their preferred cuisine
type, such as American, Indian, Italian, etc. This selection influences the recommendation algorithm to
prioritize recipes from the chosen cuisine. Course
Input: Users indicate the course type of the recipe
they are looking for, such as appetizer, main course,
dessert, etc. This input narrows down the search
to recipes suitable for the specified course. Output
Display of Recommended Recipes: Upon submitting their preferences through the input fields, users
trigger the recommendation system to process their
query and retrieve relevant recipes. The recommended recipes are displayed in the UI, providing
users with detailed information about each recipe,
including: Recipe Name: The title or name of the
recommended recipe. Ingredients: A list of ingredients required for the recipe. Instructions: Stepby-step cooking or preparation instructions for the
recipe. Time: The estimated cooking or preparation time in minutes. Cuisine: The cuisine type or
origin of the recipe. Course: The course type (e.g.,
appetizer, main course, dessert) to which the recipe
belongs. The UI presents the recommended recipes
in a structured and user-friendly format, allowing
users to browse through the options easily. Users
can view multiple recommended recipes at once,
each presented with its unique details and cooking
instructions. Interaction Flow: Users start by accessing the Streamlit application hosted on a web
server. They input their recipe preferences, such
as ingredient, time, cuisine, and course, into the
respective input fields. Upon submission, the application processes the user’s preferences and triggers
the backend recommendation system to retrieve
suitable recipes. The recommended recipes are
dynamically populated in the UI, providing users
with real-time feedback and options based on their
preferences. Users can explore the recommended
recipes, read their details, and select recipes that
align with their cooking requirements and tastes.
Overall, the Streamlit-based user interface offers a
seamless and intuitive experience for users to discover, explore, and select recipes tailored to their
preferences and cooking needs. It bridges the gap
between user input and system output, facilitating
effective recipe discovery and selection.
Results and Evaluation
The results and evaluation section of the web
crawler recipe maker generator project focuses on
assessing the performance of the recommendation
system, evaluating user feedback, and discussing
potential metrics for measuring the system’s effectiveness. Here’s a detailed breakdown of this
section:
Evaluation Criteria for Recipe Recommendations: Accuracy: The accuracy of recipe recommendations is a fundamental metric that measures
how well the system’s recommendations match
user preferences. It considers factors such as ingredient relevance, cuisine alignment, course appropriateness, and time constraints. Diversity: Recipe
diversity evaluates the variety and range of recommended recipes. A good recommendation system should offer diverse options across different
cuisines, courses, and ingredients to cater to users
with varying tastes and preferences. Relevance:
Relevance assesses the alignment of recommended
recipes with the user’s specified preferences, including ingredient choice, cuisine type, course selection, and time constraints. Relevant recommendations are those that closely match user expectations. User Satisfaction: User satisfaction is a
qualitative measure gathered through user feedback
and interactions. It reflects how satisfied users are
with the recommended recipes, the usability of the
application, and the overall experience of using the
system. Performance Metrics: Cosine Similarity
Scores: The cosine similarity scores computed during the recommendation process serve as a quantitative metric for assessing the similarity between
user preferences and recommended recipes. Higher
cosine similarity scores indicate closer matches and
better alignment. Top-k Recommendations: The
top-k recommendations returned by the system are
evaluated based on their relevance, diversity, and
accuracy. The top-k approach allows for a focused
evaluation of the most promising recommendations.
Time Efficiency: Time efficiency metrics measure
the system’s performance in generating recommendations within reasonable time constraints. This
metric is crucial for real-time or interactive applications where users expect prompt responses. User
Feedback and Usability Evaluation: Surveys and
Feedback Forms: Collecting user feedback through
surveys, feedback forms, or direct user interactions
provides valuable insights into user satisfaction,
preferences, and areas for improvement. Feedback
can highlight user preferences, suggested enhancements, and usability issues. Usability Testing: Usability testing involves evaluating the application’s
ease of use, interface intuitiveness, and overall user
experience. Testing sessions with target users can
uncover usability challenges, navigation issues, and
opportunities to enhance user satisfaction. Performance Analysis: Case Studies: Presenting case
studies or user scenarios can illustrate how the recommendation system performs in real-world usage
scenarios. These case studies can showcase successful recommendations, user interactions, and
the impact of personalized recommendations on
user experience. Comparison with Baselines: Comparing the system’s performance against baseline
models or alternative recommendation approaches
can provide benchmarking insights. It helps validate the system’s effectiveness and identify areas
where it outperforms or underperforms compared
to existing methods. Usability and Robustness: Robustness Testing: Robustness testing evaluates the
system’s resilience to edge cases, outliers, and unexpected inputs. Testing scenarios with diverse
user inputs, unusual preferences, or ambiguous
queries can assess how well the system handles
such situations. Scalability: Scalability considerations explore how the recommendation system
performs as the dataset size increases. Evaluating
scalability helps anticipate performance issues as
the system handles larger volumes of recipes and
user interactions. Feedback Incorporation: Iterative Improvements: Based on evaluation results
and user feedback, iterative improvements can be
implemented to enhance the recommendation system. This iterative approach ensures continuous
enhancement of system performance, user satisfaction, and recommendation quality. By evaluating
the recommendation system based on the outlined
criteria, metrics, and user feedback, we gain valuable insights into its effectiveness, usability, and
potential areas for enhancement. This evaluation
forms the basis for refining the system, optimizing recommendation algorithms, and delivering an
impactful user experience.

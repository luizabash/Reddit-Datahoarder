# Import necessary libraries
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize Lemmatizer
lemmatizer = WordNetLemmatizer()

# Define an expanded list of stop words
stop_words = set(stopwords.words('english'))
# Add custom stop words specific to your dataset
custom_stop_words = set(["sep", "d", "would", "like", "one", "also", "new", "many", "us", "could"])
stop_words.update(custom_stop_words)

# Function to clean the text
def preprocess_text(text):
    # Ensure the text is a string
    text = str(text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # Remove punctuation and special characters
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Convert to lowercase
    text = text.lower().strip()  # Convert to lowercase and strip leading/trailing spaces
    
    # Remove stop words (including custom stop words)
    text = ' '.join([word.strip() for word in text.split() if word.strip() not in stop_words])
    
    # Lemmatize words
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
    
    return text

# Load your CSV file (replace with your actual file path if necessary)
data = pd.read_csv('datahoarder_posts_cleaned.csv')

# Apply preprocessing to the 'title' and 'body' columns
data['cleaned_title'] = data['title'].apply(preprocess_text)
data['cleaned_body'] = data['body'].apply(preprocess_text)

# Display the first few rows to check the cleaned text
print(data[['cleaned_title', 'cleaned_body']].head())

# Basic statistics about the dataset
print(f"Number of posts: {len(data)}")
print(f"Average length of titles: {data['cleaned_title'].apply(len).mean():.2f} characters")
print(f"Average length of bodies: {data['cleaned_body'].apply(len).mean():.2f} characters")

# Word Frequency Analysis
all_titles = ' '.join(data['cleaned_title'])
all_bodies = ' '.join(data['cleaned_body'])

# Use Counter to count word frequencies
title_word_freq = Counter(all_titles.split())
body_word_freq = Counter(all_bodies.split())

# Get the 10 most common words in titles and bodies
most_common_title_words = title_word_freq.most_common(10)
most_common_body_words = body_word_freq.most_common(10)

print("Most common words in titles:", most_common_title_words)
print("Most common words in bodies:", most_common_body_words)

# Visualization: Word Cloud for Titles
plt.figure(figsize=(10, 6))
wordcloud_title = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
plt.imshow(wordcloud_title, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Titles')
plt.savefig('images/word_cloud_titles.png')
plt.show()

# Visualization: Word Cloud for Bodies
plt.figure(figsize=(10, 6))
wordcloud_body = WordCloud(width=800, height=400, background_color='white').generate(all_bodies)
plt.imshow(wordcloud_body, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Bodies')
plt.savefig('images/word_cloud_bodies.png')
plt.show()

# Visualization: Bar Plot for Top 10 Words in Titles
title_words, title_counts = zip(*most_common_title_words)
plt.figure(figsize=(8, 5))
plt.bar(title_words, title_counts, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Words in Titles')
plt.savefig('images/bar_plot_common_title_words.png')
plt.show()

# Visualization: Bar Plot for Top 10 Words in Bodies
body_words, body_counts = zip(*most_common_body_words)
plt.figure(figsize=(8, 5))
plt.bar(body_words, body_counts, color='salmon')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Words in Bodies')
plt.savefig('images/bar_plot_common_body_words.png')
plt.show()

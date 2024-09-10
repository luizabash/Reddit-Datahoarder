# Reddit-Datahoarder
this repository contains a data analysis project focused on the subreddit r/datahoarder
# Reddit Data Analysis - r/datahoarder

This project explores the community discussions and trends in the subreddit [r/datahoarder](https://www.reddit.com/r/datahoarder/). The analysis focuses on understanding what topics and themes are popular in the subreddit by examining word frequencies and visualizing key terms.

## Project Overview

- **Objective**: To analyze Reddit posts from `r/datahoarder` and identify the most common words, trends, and sentiment in the community's discussions.
- **Data Source**: Reddit posts were collected using the PRAW library (Python Reddit API Wrapper).
- **Tools and Libraries Used**: Python, Pandas, Matplotlib, NLTK, Gensim, and Streamlit.

## Project Structure

- **`data/`**: Contains the cleaned dataset used for analysis.
- **`notebooks/`**: Jupyter Notebook with Exploratory Data Analysis (EDA) and visualizations.
- **`images/`**: Visualizations generated during EDA.
- **`streamlit_app.py`**: A Streamlit app to create an interactive dashboard.

## Key Steps

1. **Data Collection**: Collected Reddit posts from `r/datahoarder` using the PRAW API.
2. **Data Preprocessing**: Cleaned the text data by removing URLs, punctuation, stop words, and lemmatizing.
3. **Exploratory Data Analysis (EDA)**: Conducted word frequency analysis and created visualizations like word clouds and bar plots.
4. **Sentiment Analysis** (Optional): Attempted sentiment analysis using VADER, but faced compatibility issues with the current setup.
5. **Results and Visualization**: Visualized the most common words in titles and post bodies, and identified key trends.

import pandas as pd
#from faker import Faker
from textblob import TextBlob
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initializing the libraries
nlp = spacy.load('en_core_web_sm')
analyzer = SentimentIntensityAnalyzer()

# Preprocessing function
def preprocess_text_spacy(text):
    doc = nlp(text.lower())
    return [token.text for token in doc if not token.is_stop and not token.is_punct]

# TextBlob sentiment analysis
def get_sentiment_textblob(tokens):
    text = " ".join(tokens)
    blob = TextBlob(text)
    return blob.sentiment.polarity

# VADER sentiment analysis
def get_sentiment_vader(text):
    sentiment = analyzer.polarity_scores(text)
    return sentiment['compound']

# Categorize sentiments
def categorize_sentiment_custom(score):
    if score > 0.1:
        return 'Satisfactory'
    elif score < -0.1:
        return 'Unsatisfactory'
    else:
        return 'Neutral'
    
# Main function to process the CSV
def analyze_sentiments(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Preprocess the feedback text
    df['ProcessedFeedback'] = df['FeedbackText'].apply(preprocess_text_spacy)

    # Apply sentiment analysis
    df['SentimentTextblob'] = df['ProcessedFeedback'].apply(get_sentiment_textblob)
    df['SentimentVader'] = df['FeedbackText'].apply(get_sentiment_vader)

    # Categorize sentiments based on the analysis
    df['SentimentCategoryTextblob'] = df['SentimentTextblob'].apply(categorize_sentiment_custom)
    df['SentimentCategoryVader'] = df['SentimentVader'].apply(categorize_sentiment_custom)

    return df

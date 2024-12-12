import pandas as pd
#from faker import Faker
#from textblob import TextBlob
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy
from transformers import pipeline

# Initializing the libraries
nlp = spacy.load('en_core_web_sm')
analyzer = pipeline("sentiment-analysis", model = "nlptown/bert-base-multilingual-uncased-sentiment")

# Preprocessing function
def preprocess_text_spacy(text):
    doc = nlp(text.lower())
    return [token.text for token in doc if not token.is_stop and not token.is_punct]

# TextBlob sentiment analysis
'''
def get_sentiment_textblob(tokens):
    text = " ".join(tokens)
    blob = TextBlob(text)
    return blob.sentiment.polarity
'''

# VADER sentiment analysis
'''
def get_sentiment_vader(text):
    sentiment = analyzer.polarity_scores(text)
    return sentiment['compound']
'''

#BERT sentiment analysis
def get_sentiment_bert(tokens):
    text = " ".join(tokens)
    sentiment = analyzer(text)
    #extracting the sentiment labels and score
    sentiment_label = sentiment[0]['label']
    sentiment_score = sentiment[0]['score']

    #mapping the sentiment labels
    label_mapping = {
        "1 star" : "Very Negative",
        "2 stars" : "Negative",
        "3 stars" : "Neutral",
        "4 stars" : "Positive",
        "5 stars" : "Very Positive"
    }
    sentiment_label_human = label_mapping.get(sentiment_label, "Unknown")

    return sentiment_score, sentiment_label_human


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

    # Apply BERT sentiment analysis
    df['SentimentBertScore'], df['SentimentBertLabel'] = zip(*df['ProcessedFeedback'].apply(get_sentiment_bert))

    return df

    '''# Categorize sentiments based on the analysis
    df['SentimentCategoryTextblob'] = df['SentimentTextblob'].apply(categorize_sentiment_custom)
    df['SentimentCategoryVader'] = df['SentimentVader'].apply(categorize_sentiment_custom)
    '''
    

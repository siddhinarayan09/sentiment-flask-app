from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Import the analysis function
from sentiment_analysis import analyze_sentiments

app = Flask(__name__)
CORS(app, origins = ["http://localhost:3000"])

# Route to display the upload form
@app.route('/')
def upload_form():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Upload File</title>
    </head>
    <body>
        <h1>Welcome to the Sentiment Analysis App</h1>
        <p>Use the form below to upload a CSV file for sentiment analysis:</p>
        <form action="/upload" method="POST" enctype="multipart/form-data">
            <input type="file" name="file" accept=".csv" required>
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    '''

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    if not file.filename.endswith('.csv'):
        return jsonify({'error': 'File must be a CSV'}), 400

    file_path = os.path.join('uploads', file.filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(file_path)

    try:
        # Analyze sentiments
        analyzed_df = analyze_sentiments(file_path)

        # Generate pie charts
        '''
        vader_chart_path = generate_pie_chart(analyzed_df, 'SentimentCategoryVader', 'VADER Sentiment Distribution')
        textblob_chart_path = generate_pie_chart(analyzed_df, 'SentimentCategoryTextblob', 'TextBlob Sentiment Distribution')
        '''
        #Generate pie chart for BERT analysis
        bert_chart_path = generate_pie_chart(analyzed_df, 'SentimentBertLabel', 'BERT Sentiment Distribution')

        
        # Remove the uploaded file
        os.remove(file_path)

        # Serve the result as an HTML page with both charts embedded
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Analysis Result</title>
        </head>
        <body>
            <h1>Sentiment Analysis Result</h1>
            <p>Below is the sentiment distribution using BERT analysis:</p>
            <h2>BERT Sentiment Analysis</h2>
            <img src="/static/{bert_chart_path}" alt="BERT Sentiment Chart">
        </body>
        </html>
        '''
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Function to generate pie charts
def generate_pie_chart(df, column, title):
    sentiment_counts = df[column].value_counts()

    # Create the pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')  # Ensures the pie chart is a circle

    # Ensure static folder exists
    os.makedirs('static', exist_ok=True)

    # Save the chart
    chart_filename = f"{title.replace(' ', '_').lower()}.png"
    chart_path = os.path.join('static', chart_filename)
    plt.savefig(chart_path)
    plt.close()

    return chart_filename


if __name__ == '__main__':
    app.run(debug=True)

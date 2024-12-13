# Sentiment Analysis with Flask and BERT

This project is a sentiment analysis application built using Flask for the backend, a React frontend, and the BERT model for NLP-based sentiment analysis. Users can upload a CSV file with feedback data, and the application categorizes the sentiments, generates pie charts for visual insights, and displays the results dynamically.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Output](#output)
- [Future Enhancements](#future-enhancements)
- [Acknowledgments](#acknowledgments)

---

## Overview

This project leverages **BERT (Bidirectional Encoder Representations from Transformers)** for sentiment analysis, analyzing customer feedback or textual data. Sentiments are classified into categories like "Very Positive," "Positive," "Neutral," "Negative," and "Very Negative." The results are visualized through  a pie chart.

---

## Features

- **Dynamic Sentiment Analysis**: Uses the BERT NLP model for accurate sentiment classification.
- **File Upload Support**: Allows uploading CSV files containing textual feedback for analysis.
- **Data Visualization**: Generates and displays pie charts for sentiment distributions.
- **User-Friendly Web Interface**: Powered by Flask and React.js for seamless user interaction.

---

## Technologies Used

- **Backend**: Flask
- **Frontend**: React.js
- **NLP Model**: `nlptown/bert-base-multilingual-uncased-sentiment` from the Hugging Face Transformers library
- **Libraries**:
  - Pandas for CSV processing
  - Matplotlib for chart generation
  - SpaCy for text preprocessing
- **Deployment Environment**: Localhost

---

## How It Works

1. **Input**:
   - User uploads a CSV file containing feedback data.
   - Each feedback entry is preprocessed using SpaCy to remove stopwords and punctuation.

2. **Sentiment Analysis**:
   - Each preprocessed feedback text is analyzed using the BERT model.
   - BERT provides a sentiment label (e.g., "Very Positive") and a confidence score.

3. **Visualization**:
   - The results are categorized and visualized as pie charts for easy understanding.

4. **Output**:
   - The app dynamically generates HTML to display sentiment distributions with charts.

---

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Node.js (for React frontend)
- Pipenv or pip for Python dependency management

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd sentiment-analysis-app
2. **Set Up the Backend**:
  Create a virtual environment and install dependencies:
   ```bash
    pip install -r requirements.txt

3. **Start the Flask App**:
   ```bash
     python app1.py

## Usage

Launch the app in your browser.
Upload a CSV file containing feedback data. Ensure the file has a column named FeedbackText.
Wait for the analysis to complete.
View the sentiment distribution charts and detailed results.

## Output

The application produces:

**Pie Charts**: Visual representations of sentiment distributions (e.g., "Very Positive," "Negative").
**Processed Feedback Data**: CSV output showing sentiment scores and labels for each entry.


![Screenshot 2024-12-12 223725](https://github.com/user-attachments/assets/b5737036-0697-45a5-be01-734d9a9126e8)


![Screenshot 2024-12-12 222709](https://github.com/user-attachments/assets/d27d0cee-65ce-4160-b954-3254c4a23ac2)


## Future Enhancements

**MongoDB Integration**:
Store feedback data and sentiment results for persistent access and historical analysis.
**Dashboard**:
Add features for filtering and viewing historical results by date or sentiment category.
**Advanced Visualizations**:
Use more sophisticated tools like Plotly or D3.js for interactive charts.
**Multi-language Support**:
Extend the app to support feedback in multiple languages.
**Authentication**:
Allow users to save their analysis securely with user accounts.

## Acknowledgments

**Hugging Face**: For providing the nlptown/bert-base-multilingual-uncased-sentiment model.
**Flask**: For the lightweight and flexible backend framework.
**React.js**: For building a responsive and dynamic frontend.
**Matplotlib**: For generating charts.
**SpaCy**: For NLP preprocessing.

Inspiration from NLP projects and sentiment analysis examples.

*Thank you :)*








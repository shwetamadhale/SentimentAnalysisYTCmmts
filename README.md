# Chatbot - Sentiment Analysis and Clustering of YouTube Comments

A Python-based project that performs sentiment analysis and clustering on YouTube comments using APIs, text processing, and machine learning techniques.

## Table of Contents
- [Background](#background)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Background
This project collects YouTube comments using the YouTube Data API, processes the text data, applies clustering techniques to group similar comments, and performs sentiment analysis. It helps uncover insights and discover key discussion topics.

## Features
- **YouTube API Integration**: Fetches comments from YouTube videos.
- **Text Preprocessing**: Cleans and normalizes text data.
- **Feature Extraction**: Uses TF-IDF vectorization for text representation.
- **Clustering**: Applies K-Means clustering to group similar comments.
- **Sentiment Analysis**: Determines the sentiment polarity of comments.
- **Visualization**: Generates insights through data visualization.

## Technologies Used
- **Python**: Core programming language.
- **APIs**:
  - YouTube Data API for comment retrieval.
- **Text Processing**:
  - NLTK, TextBlob, and custom text cleaning functions.
- **Machine Learning**:
  - Scikit-learn for clustering (K-Means) and vectorization (TF-IDF).
- **Data Handling**:
  - Pandas for data manipulation.
- **Visualization**:
  - Matplotlib and Seaborn for visual representation.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/shwetamadhale/SentimentAnalysisYTComments.git
   ```
2. Navigate to the project directory:
   ```sh
   cd SentimentAnalysisYTComments
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the script for YouTube comment retrieval:
   ```sh
   python get_yt_comments.py
   ```
5. Run the analysis and clustering:
   ```sh
   python analysis.py
   ```

## Usage
1. **Retrieve YouTube Comments**:
   - Configure the API key in `get_yt_comments.py`.
   - Fetch comments from a specific video or channel.
2. **Preprocess Data**:
   - Clean and normalize text using NLP techniques.
3. **Perform Clustering & Sentiment Analysis**:
   - Apply K-Means clustering.
   - Use sentiment analysis techniques.
4. **Visualize Results**:
   - View clustering insights and sentiment trends.

## Project Structure
```
SentimentAnalysisYTComments/
│── analysis.py             # Script for clustering & analysis
│── get_yt_comments.py      # Fetches comments from YouTube
│── requirements.txt        # List of dependencies
│── yt_comments.csv         # Retrieved comments dataset
│── elbow.png               # Visualization of Elbow Method
│── notebooks/              # Jupyter notebooks for analysis
```

## Contributing
Contributions are welcome! Feel free to submit pull requests or open issues.

## License
This project is licensed under the MIT License.


# preprocess.py
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import joblib

# Download NLTK resources
nltk.download('punkt_tab')
nltk.download('stopwords')


# Load dataset
def load_dataset(filepath):
    """
    Load and prepare the dataset.
    Ensure the dataset has 'text' and 'label' columns.
    """
    data = pd.read_csv(filepath)
    data = data[['text', 'label']]  # Columns must be named 'text' and 'label'
    return data

# Clean text
def clean_text(text):
    """
    Clean the input text.
    """
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    tokens = nltk.word_tokenize(text)  # Tokenize
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]  # Remove stopwords
    return ' '.join(tokens)

# Preprocess dataset
def preprocess_data(data):
    """
    Clean and vectorize the dataset.
    """
    data['cleaned_text'] = data['text'].apply(clean_text)
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(data['cleaned_text']).toarray()
    y = data['label']
    return X, y, vectorizer

# Main execution
if __name__ == "__main__":
    dataset_path = "data/dataset.csv"  # Path to your dataset
    data = load_dataset(dataset_path)

    print("Cleaning and preprocessing data...")
    X, y, vectorizer = preprocess_data(data)

    print("Splitting data into training and testing sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Save vectorizer and preprocessed data
    joblib.dump(vectorizer, "models/vectorizer.pkl")
    joblib.dump((X_train, X_test, y_train, y_test), "data/preprocessed_data.pkl")

    print("Preprocessing complete. Saved vectorizer and preprocessed data.")

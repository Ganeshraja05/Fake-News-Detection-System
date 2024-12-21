# Fake News Detection System

This project is a machine learning-based system designed to identify fake news articles using natural language processing (NLP). By leveraging datasets of labeled fake and real news, the system trains a classification model to distinguish between genuine and fabricated news articles.

---

## Features
- **Dataset Merging:** Combines and processes datasets of fake and real news articles with appropriate labels.
- **Model Training:** Implements a Logistic Regression model to classify news articles as fake or real.
- **Evaluation Metrics:** Provides accuracy, confusion matrix, and a detailed classification report for model performance.
- **Reusable Model:** Saves the trained model for future use and predictions.

---

## Requirements

Before running the project, ensure you have the following installed:
- Python 3.8+
- Pandas
- Scikit-learn
- Joblib

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Project Structure

- **`merge_datasets.py`**: Prepares the dataset by merging, labeling, and shuffling fake and real news articles.
- **`train_model.py`**: Trains the Logistic Regression model on the preprocessed dataset and evaluates its performance.

---

## Workflow

1. **Prepare the Dataset**:
   Run the `merge_datasets.py` script to combine and preprocess the fake and real news datasets.
   ```bash
   python merge_datasets.py
   ```
   - Input:
     - `data/Fake.csv` (Fake news articles)
     - `data/True.csv` (Real news articles)
   - Output:
     - `data/dataset.csv` (Combined dataset with labels)

2. **Train the Model**:
   Use the `train_model.py` script to train and evaluate the model.
   ```bash
   python train_model.py
   ```
   - Input:
     - `data/preprocessed_data.pkl` (Preprocessed training and testing data)
   - Output:
     - `models/model.pkl` (Trained model)

3. **Evaluate Performance**:
   After training, the script provides:
   - Accuracy score
   - Confusion matrix
   - Classification report

---

## How It Works

1. **Dataset Preparation**:
   The datasets are labeled as:
   - `1` for Fake news
   - `0` for Real news
   These are then combined, shuffled, and saved as a single CSV file.

2. **Model Training**:
   A Logistic Regression model is trained using the labeled dataset. The data is split into training and testing sets to evaluate the model's effectiveness.

3. **Model Evaluation**:
   Metrics such as accuracy and confusion matrix provide insights into the model's performance.

---

## Future Enhancements

- Add support for other machine learning models like Random Forest or Neural Networks.
- Incorporate advanced NLP techniques like word embeddings (e.g., Word2Vec, BERT).
- Create a user-friendly interface for predictions.

---

## Acknowledgements

- **Datasets**:
  - `Fake.csv` and `True.csv` sourced from open datasets of news articles.
- **Tools & Libraries**:
  - Python, Pandas, Scikit-learn, Joblib

---

## Author

Developed by [Your Name]. Contributions are welcome. Feel free to submit pull requests or issues on GitHub.

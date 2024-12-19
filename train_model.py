import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Load preprocessed data
print("Loading preprocessed data...")
X_train, X_test, y_train, y_test = joblib.load("data/preprocessed_data.pkl")

# Train the model
print("Training Logistic Regression model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate the model
print("Evaluating the model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("\nModel Evaluation Results:")
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(report)

# Save the trained model
print("Saving the trained model...")
joblib.dump(model, "models/model.pkl")
print("Model saved as models/model.pkl")

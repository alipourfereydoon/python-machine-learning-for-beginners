
# First Machine Learning Project
# Predicting Student Exam Results

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 1: Create the dataset
# Input: Hours studied
X = [
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10],
    [1.5], [2.5], [3.5], [4.5], [5.5],
    [6.5], [7.5], [8.5], [9.5], [11]
]

# Output: Exam result
# 0 = Failed, 1 = Passed
y = [
    0, 0, 0, 0, 1,
    1, 1, 1, 1, 1,
    0, 0, 0, 1, 1,
    1, 1, 1, 1, 1
]

# Step 2: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Step 3: Create the machine learning model
model = DecisionTreeClassifier(max_depth=3, random_state=42)

# Step 4: Train the model
model.fit(X_train, y_train)

# Step 5: Make predictions on test data
y_pred = model.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Step 7: Predict the result for a new student
hours = [[5]]

prediction = model.predict(hours)

if prediction[0] == 1:
    print("The student is predicted to PASS.")
else:
    print("The student is predicted to FAIL.")

# Python Machine Learning for Beginners

A beginner-friendly collection of practical Python exercises for learning the fundamentals of Machine Learning.

This repository is designed for students who are starting their Machine Learning journey. Each exercise introduces a concept through simple, readable Python code.

## Learning Goals

By working through these exercises, students will learn how to:

- Understand the basic workflow of a Machine Learning project.
- Prepare input features and target labels.
- Split data into training and testing sets.
- Train a simple Machine Learning model.
- Make predictions on new examples.
- Evaluate a model using basic metrics.
- Experiment with model settings and understand their effects.

## Requirements

- Python 3.9 or newer
- Basic Python knowledge
- `scikit-learn`

Install the required library:

```bash
python -m pip install scikit-learn
```

## Exercise 1: Predicting Student Exam Results

**File:** `first_machine_learning.py`

In this introductory exercise, a Decision Tree classifier learns from a small, illustrative dataset containing students' study hours and exam outcomes.

- **Input feature:** Number of hours studied
- **Target label:** `0` = Failed, `1` = Passed
- **Model:** `DecisionTreeClassifier`
- **Evaluation metric:** Accuracy

### Run the exercise

```bash
python first_machine_learning.py
```

The script trains a model, evaluates its predictions on a test split, and predicts an outcome for a new example.

> **Important:** The dataset is small and artificial, intended only for learning. Study hours alone cannot reliably determine whether a real student will pass an exam. The model's predictions are not guarantees, and the accuracy score should not be interpreted as evidence of real-world performance.

## Student Tasks

After running the example, try the following:

1. Predict the outcome for students who studied for 2, 5, and 9 hours.
2. Add at least five new examples to the dataset, including their target labels.
3. Change `max_depth` from `3` to `2`, then to `5`. Compare the results.
4. Explain what the accuracy score measures.
5. Run the experiment several times with different `random_state` values and discuss why the test accuracy may change.
6. Identify limitations of using study hours as the only input feature.

## Suggested Learning Roadmap

1. Python fundamentals
2. NumPy and Pandas
3. Data cleaning and exploratory data analysis
4. Training and testing datasets
5. Classification with Decision Trees
6. Model evaluation
7. Linear Regression
8. Logistic Regression
9. More practice projects with real datasets

## Project Structure

```text
python-machine-learning-for-beginners/
├── README.md
└── first_machine_learning.py
```

As the repository grows, each new exercise can be added as a separate Python file with its own explanation and tasks.

## Contributing

Students are encouraged to practice, experiment with the code, and suggest improvements. If you find an error or have an idea for a new beginner exercise, feel free to open an issue or submit a pull request.

## License

This project is intended for educational use. A license has not yet been selected. If you want others to reuse, modify, and distribute the code, consider adding an appropriate open-source license, such as the MIT License.

---

**Happy Learning!**

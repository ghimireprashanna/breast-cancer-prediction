# Breast Cancer Prediction using Machine Learning

This project predicts whether a tumor is benign or malignant using machine learning algorithms (Logistic Regression, KNN, and Naive Bayes).

## Run Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Run Streamlit app: `streamlit run app.py`

## Best Model
**Logistic Regression** achieved 97.36% accuracy.

lets see what have we done here.
1. Data Collection and Exploration
 Load the Dataset:
o Use Pandas to load the dataset into a DataFrame.
 Initial Exploration:
o Examine the dataset structure, data types, and summary statistics.
o Identify potential issues such as missing values, inconsistent data, or
outliers.

2. Data Cleaning and Transformation
 Handle Missing Values:
o Apply appropriate techniques such as imputation or removal.
 Outlier Detection and Treatment:
o Use statistical methods or visualization techniques to identify and
handle outliers.
 Data Transformation:
o Encode categorical variables using methods like one-hot encoding or
label encoding.
o Normalize or scale numerical features as needed.
o Create new features if necessary to improve model performance.

3. Exploratory Data Analysis (EDA)

 Visualization:
o Use tools such as Matplotlib and Seaborn to analyze data
distributions, correlations, and trends.
o Explore relationships between variables and identify patterns.
 Key Findings:
o Summarize insights obtained from the visualizations and statistical
analysis.
4. Feature Selection
 Relevance Analysis:
o Use correlation analysis, feature importance metrics, or domain
knowledge to identify the most relevant features.

 Dimensionality Reduction:
o Remove irrelevant or redundant features to simplify the model.

5. Model Development
 Data Splitting:
o Divide the dataset into training and testing sets.
 Algorithm Selection:
o Choose a machine learning algorithm suitable for the problem (e.g.,
Linear Regression, Logistic Regression, KNN, Naïve Bayes,etc).

 Model Training:
o Train the model using the training data.
 Model Evaluation:
o Validate the model on the testing data using appropriate performance
metrics depending on the problem type. (e.g., accuracy, precision,
recall, F1-score,MSE, MAE, RMSE).
6. Model Evaluation and Hyperparameter Tuning
 Cross-Validation:
o Perform cross-validation to assess the model’s performance.
 Hyperparameter Tuning:
o Optimize model parameters using techniques like Grid Search or
Random Search.
 Final Evaluation:
o Compare models and select the best-performing one based on
evaluation metrics.

7. Model Deployment
 Streamlit Deployment on localhost:
o Build an interactive web application using Streamlit on localhost.
o Create a user-friendly interface to accept user inputs and display
model predictions.

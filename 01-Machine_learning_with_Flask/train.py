import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

DATASET_PATH = "src/Salary_Data.csv"

# Load dataset
datas = pd.read_csv(DATASET_PATH)
X = datas["YearsExperience"].values
# We need to reshape because we have a 1D array intead of 2D, and our regressor
# needs 2D shape input X
X = X.reshape(-1,1)
y = datas["Salary"].values

# Split into train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Create a linear regression model
regressor = LinearRegression()

# We are ready to fit our model
regressor.fit(X_train, y_train)

# Compute score on test set
test_score = regressor.score(X_test, y_test)
print(f"Test score: {test_score}")

# Create the folder "models" if not exists
if not os.path.exists("models"):
    os.makedirs("models")

# Dump model in pickle file
# We could improve this script by generating a file name with date and hour for
# example for later selection
joblib.dump(regressor, "models/regressor_model.joblib")

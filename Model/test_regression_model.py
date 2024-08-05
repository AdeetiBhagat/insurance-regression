import unittest
import os
import pandas as pd
from regression_model import load_data, preprocess_data, train_model

# Sample data for testing
data = {
    'age': [19, 18, 28, 33, 32],
    'sex_male': [0, 1, 1, 0, 0],
    'bmi': [27.9, 33.77, 33, 22.705, 28.88],
    'children': [0, 1, 3, 0, 0],
    'smoker_yes': [1, 0, 0, 0, 0],
    'region_northwest': [0, 1, 0, 0, 0],
    'region_southeast': [1, 0, 1, 0, 0],
    'region_southwest': [0, 0, 0, 1, 0],
    'charges': [16884.92, 1725.55, 4449.46, 21984.47, 3866.86]
}
df = pd.DataFrame(data)

class TestRegressionModel(unittest.TestCase):

    def test_load_data(self):
         # Ensure the path is relative to the root of the repository
        file_path = os.path.join(os.path.dirname(__file__), '../Data/insurance-1.csv')
        df_loaded = load_data(file_path)
        self.assertIsInstance(df_loaded, pd.DataFrame, "Loaded data is not a DataFrame")

    def test_preprocess_data(self):
        X, y = preprocess_data(df)
        self.assertFalse(X.empty, "Features DataFrame is empty")
        self.assertFalse(y.empty, "Target Series is empty")
        self.assertNotIn('charges', X.columns, "Target column should not be in features")

    def test_train_model(self):
        X, y = preprocess_data(df)
        model, mse = train_model(X, y)
        self.assertIsNotNone(model, "Model is not trained")
        self.assertGreaterEqual(mse, 0, "MSE should be non-negative")

if __name__ == "__main__":
    unittest.main()

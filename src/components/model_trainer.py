import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test data")

            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            # ✅ MODELS (ONLY sklearn-compatible)
            models = {
                "Random Forest": RandomForestRegressor(random_state=42),
                "Decision Tree": DecisionTreeRegressor(random_state=42),
                "Gradient Boosting": GradientBoostingRegressor(random_state=42),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(
                    objective="reg:squarederror",
                    random_state=42,
                    verbosity=0
                ),
                "AdaBoost Regressor": AdaBoostRegressor(random_state=42),
            }

            # ✅ HYPERPARAMETERS
            params = {
                "Decision Tree": {
                    "criterion": ["squared_error", "friedman_mse"],
                },
                "Random Forest": {
                    "n_estimators": [50, 100, 200],
                },
                "Gradient Boosting": {
                    "learning_rate": [0.05, 0.1],
                    "n_estimators": [50, 100],
                },
                "Linear Regression": {},
                "XGBRegressor": {
                    "learning_rate": [0.05, 0.1],
                    "n_estimators": [50, 100],
                },
                "AdaBoost Regressor": {
                    "learning_rate": [0.05, 0.1],
                    "n_estimators": [50, 100],
                },
            }

            logging.info("Starting model evaluation")

            model_report = evaluate_models(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models,
                param=params,
            )

            # ✅ Best model selection
            best_model_score = max(model_report.values())
            best_model_name = max(model_report, key=model_report.get)
            best_model = models[best_model_name]

            logging.info(f"Best Model: {best_model_name} | R2 Score: {best_model_score}")

            if best_model_score < 0.6:
                raise CustomException("No suitable model found", sys)

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model,
            )

            predictions = best_model.predict(X_test)
            r2 = r2_score(y_test, predictions)

            return r2

        except Exception as e:
            raise CustomException(e, sys)

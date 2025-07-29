import os
import pandas as pd
import mlflow
import mlflow.sklearn
import joblib
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from src.utils.common import save_json
from src.entity.config_entity import ModelEvaluationConfig
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        r2 = r2_score(actual, pred)
        return rmse, r2
    
    def log_into_mlflow(self):
        
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop(columns=[self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme     
        
        with mlflow.start_run():
            
            (rmse, r2) = self.eval_metrics(test_y, model.predict(test_x))
            
            scores = {
                "rmse": rmse,
                "r2": r2
            }
            
            save_json(path = Path(self.config.metric_filename), data=scores)
            
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name='ElasticNet')
            else:
                mlflow.sklearn.log_model(model, "model") 
    
    
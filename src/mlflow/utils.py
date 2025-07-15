import mlflow

mlflow.set_tracking_uri("http://mlflow_host:5000")
mlflow.set_experiment("nombre_experimento")

with mlflow.start_run():
    mlflow.log_param("param1", 10)
    mlflow.log_metric("accuracy", 0.87)
    mlflow.log_artifact("/local/path/model.pt")

import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5001")

mlflow.set_experiment("Check localhost connection")
with mlflow.start_run():
    mlflow.log_metric("test", 1)
    mlflow.log_metric("rmse", 0.29)

with mlflow.start_run():
    mlflow.log_metric("ak1", 456)
    mlflow.log_metric("ak2", 789)
    
import mlflow

experiment_name = "experment_2" # nombre de experimento existente
entry_point = "app.main.py"

mlflow.projects.run(
    uri=".",
    entry_point=entry_point,
    experiment_name=experiment_name
)
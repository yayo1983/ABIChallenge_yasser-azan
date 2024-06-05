name: "RFM ML my_ml"

docker_env:
  image: "abichallenge_yasser-azan_fastapi"  # Nombre de la imagen Docker que quieres usar
  build:
    context_path: .  # Ruta al contexto de construcción del Dockerfile (normalmente el directorio actual)
    dockerfile_path: "Dockerfile"  # Ruta al Dockerfile (si no está en el contexto de construcción, ajusta esta ruta)

entry_points:
  app:
    command: "python3 app.main.py"

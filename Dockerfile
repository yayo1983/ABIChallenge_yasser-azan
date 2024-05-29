# Utilizar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo requirements.txt a la imagen
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación a la imagen
COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

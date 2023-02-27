# Utiliser une image Python
FROM python:3.9-slim-buster

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier les fichiers requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader punkt

# Copier le reste des fichiers dans le conteneur
COPY . .

# Exposer le port 8000 pour que l'application soit accessible depuis l'extérieur du conteneur
EXPOSE 8000

# Démarrer l'application Flask
CMD ["python", "server.py"]

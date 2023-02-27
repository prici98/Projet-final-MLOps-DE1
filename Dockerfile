# Utiliser une image Node.js
FROM node:14-alpine

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier les fichiers package.json et package-lock.json dans le conteneur
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier le reste des fichiers dans le conteneur
COPY . .

# Construire l'application React
RUN npm run build


# Exposer le port 3000 pour que l'application soit accessible depuis l'extérieur du conteneur
EXPOSE 3000

# Démarrer l'application React
CMD ["npm", "start"]

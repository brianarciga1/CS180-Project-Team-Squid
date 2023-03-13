FROM node:16

EXPOSE 5173

WORKDIR /app

COPY package*.json ./
RUN npm install
COPY . .

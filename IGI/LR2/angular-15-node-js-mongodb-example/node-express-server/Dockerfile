FROM node:18

WORKDIR /app

# список зависимостей
COPY package.json .
RUN npm install

COPY . .

# из readme
EXPOSE 8080

CMD ["node", "server.js"]
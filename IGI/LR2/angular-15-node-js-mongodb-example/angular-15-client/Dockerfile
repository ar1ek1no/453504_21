FROM node:18

WORKDIR /app

COPY package.json .
RUN npm install
# angular CLI для ng отдельно
RUN npm install -g @angular/cli@15

COPY . .

EXPOSE 8081
ENV NG_CLI_ANALYTICS=false
# 0.0.0.0 - запросы со всех сетевых интерфейсов
CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "8081", "--disable-host-check"]

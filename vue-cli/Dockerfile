FROM node:14-bullseye

RUN npm install -g @vue/cli
RUN mkdir -p /var/www/sampleproject
WORKDIR /var/www/sampleproject
COPY ./ /var/www/sampleproject
RUN npm install
RUN npm run build

EXPOSE 8080

ENTRYPOINT ["npm", "run", "serve"]

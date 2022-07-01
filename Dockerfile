FROM nikolaik/python-nodejs:latest

WORKDIR /app
COPY . .
RUN make configure

# Build Application
RUN make build

# Start Application
CMD make serve
EXPOSE 8080

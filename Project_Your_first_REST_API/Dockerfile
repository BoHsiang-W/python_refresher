FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["/bin/bash", "docker-entrypoint.sh"]

# build image:
# docker build -t flask-smorest-api .

# run container:
# Mac/Linux command:
## docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api
# Windows command:
# docker run -dp 5000:5000 -w /app -v "/c/Documents/yourproject:/app" flask-smorest-api
### -w: working directory
### -v: volume mapping

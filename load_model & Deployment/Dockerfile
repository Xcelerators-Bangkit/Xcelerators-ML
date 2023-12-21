# FROM python:3.9-slim

# # Step 2. Copy local code to the container image.
# ENV APP_HOME /app
# WORKDIR /code
# COPY . ./

# RUN pip install --upgrade pip

# # Step 3. Install production dependencies.
# RUN pip install -r requirements.txt

# # Step 4: Run the web service on container startup using gunicorn webserver.
# CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app

FROM python:3.9

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

# As an example here we're running the web service with one worker on uvicorn.
CMD exec uvicorn main:app --host 0.0.0.0 --port 8080 --workers 1
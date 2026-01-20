# base image
FROM python:3.10

# working directory
WORKDIR /app

# copy files
COPY . /app

# run 
RUN pip install -r requirements.txt

# exposing ports
EXPOSE 5001

# run command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5001"]

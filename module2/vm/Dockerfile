#Use official Python image
FROM python:3.11-slim

#Set working directory inside container
WORKDIR /app


#Copy requirements 
COPY requirements.txt .

#install dependencies

RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the code

COPY . .

#run the code app

CMD [ "python","main.py" ]
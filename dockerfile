FROM python:3.8

WORKDIR /App

COPY requirements.txt ./
#gets the necessary packages for the project.
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
#uses port 5000
EXPOSE 5000

CMD ["python","main.py"]
# Dockerfile to build a flask app
FROM python:3.10



WORKDIR /usr/app



#copy the requirement file into the same directory which is /usr/app

COPY requirements.txt .



#install the requirements

RUN pip install -r requirements.txt



#copy the app to the current directory

COPY . .



EXPOSE 8000



#run the app

CMD ["python", "-m", "flask", "run","--host=0.0.0.0"]
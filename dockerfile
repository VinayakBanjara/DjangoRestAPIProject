FROM python:3.11.2
EXPOSE 8081
WORKDIR /app 
RUN pip install Django
RUN pip3 install djangorestframework
COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8081"]


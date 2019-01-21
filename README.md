# recipe-app-api
This is our recipe api course

#After creating all the application we will run the docker container
docker-compose run app sh -c "django-admin startproject app ."

#To run the test with flake8
docker-compose run app sh -c "python manage.py test && flake8"

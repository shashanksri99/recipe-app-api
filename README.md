# recipe-app-api
This is our recipe api course

#After creating all the application we will run the docker container
docker-compose run app sh -c "django-admin startproject app ."

For working
Important proxy setting for applications
npm config set proxy http://10.112.50.97:8080/
git config --global http.proxy http://10.112.50.97:8080/
apm config set proxy http://10.112.50.97:8080/
pip install --proxy=10.112.50.97:8080 django==1.10.5
/usr/bin/chromium-browser --proxy-server=http://10.112.50.97:8080

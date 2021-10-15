# XAITK - Saliency

## Intent
Provide dockerized api module for interaction with https://github.com/XAITK/xaitk-saliency package

ROUGH DOCUMENTATION (October 15)

How to run: 
1. Download from Github
2. Create a docker image by running the command 'docker build -t [imagename] .'
3. Create the container and run: 'docker run -d --name [containername] -p 80:80 [imagename]
4. Check that the container was created: 'docker ps' to list all running docker containers
5. check 'http://127.0.0.1/docs#/' to see the Swagger UI of the API, running on your local machine
6. <img width="1440" alt="Screen Shot 2021-10-15 at 4 55 27 PM" src="https://user-images.githubusercontent.com/58711019/137554647-7f0c338c-6781-41c4-a469-6bfae9967fc3.png">

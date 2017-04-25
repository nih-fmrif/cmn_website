# Django, uWSGI and Nginx in a container, using Supervisord

This django website and server are based on the respository at 
https://github.com/dockerfiles/django-uwsgi-nginx

Most of their setup comes from the excellent tutorial on 
https://uwsgi.readthedocs.org/en/latest/tutorials/Django_and_nginx.html

### Build and run
#### Build with python3
* `docker build -t webapp .`
* `docker run -d -p 80:80 --name webapp webapp`
* go to 127.0.0.1 to see if works

#### Alternate run command for bash session in container with current directory mounted in place of container's code directory (useful for developing)
* `docker run -it -p 80:80 -v $PWD:/home/docker/code --name webapp --entrypoint=/bin/bash webapp`

### Kill a running conatainer in the case you need to restart
* `docker rm -vf webapp`

## For crn admins
This repo will get you most of the files you need to set up the website. 
You will additionally need the files in https://github.com/nih-fmrif/crn_private.
Instructions for setting up the website with ssl certs is in crn_private.

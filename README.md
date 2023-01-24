# ContainersDemo
Source code for the Lunch and Learn session - 24th Jan 2022

## Prerequisites

1. Install Docker Desktop - https://www.docker.com/products/docker-desktop/

## dotnetapp
The following commands were used throughout the demo.

Build an image from the dotnetapp Dockerfile(s)

`docker build -t dotnetapp:latest ./dotnetapp`

`docker build -t dotnetapp:latest ./dotnetapp -f ./dotnetapp/Dockerfile.slim`

See: https://docs.docker.com/engine/reference/commandline/build/

Run the the dotnetapp container image

`docker run --name dotnetapp -d -p 8080:80 dotnetapp:latest`

See: https://docs.docker.com/engine/reference/commandline/run/

List images

`docker images`

See: https://docs.docker.com/engine/reference/commandline/images/

List containers

`docker ps`

`docker ps -a`

See: https://docs.docker.com/engine/reference/commandline/ps/

Remove one or more containers

`docker rm <container_id_1> <container_id_2> .. .. -f`

See: https://docs.docker.com/engine/reference/commandline/rm/

Remove one or more images

`docker rmi <image_id_1> <image_id_2> ... ... -f`

See: https://docs.docker.com/engine/reference/commandline/rmi/

Create a tag

See: https://docs.docker.com/engine/reference/commandline/tag/

Push an image to a registry

https://docs.docker.com/engine/reference/commandline/push/

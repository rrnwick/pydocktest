# use a slim small base image
FROM python:3.13-slim

# create working dir in container
WORKDIR /app

# copy our apps source code into container
# this run binding method allows changes to host src code 
# to be shown within running container
# docker run -it --mount type=bind,src=./src,dst=/app pydock bash
COPY src .

# install python packages
RUN pip install --no-cache-dir -r requirements.txt

# run the app named d1a.py
CMD ["python", "d1a.py"]

# build with:
# > docker build -t imagename .
# To run terminal in container and use PuDB:
# > docker run -it imagename bash

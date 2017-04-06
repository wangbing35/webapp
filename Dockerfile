FROM ubuntu:14.04
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-all python-pip 
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp
EXPOSE 5000
CMD ["python", "app.py"]

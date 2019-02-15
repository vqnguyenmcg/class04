FROM ubuntu:16.04
MAINTAINER Van Quang Nguyen
RUN apt-get update
RUN cat /etc/lsb-release
RUN apt-get install -y python3-pip
RUN apt install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install numpy pandas
RUN mkdir -p /home/work
COPY ./python_script.py /home/work/python_script.py
COPY ./breast-cancer-wisconsin.data.txt /home/work/breast-cancer-wisconsin.data.txt
ENTRYPOINT ["python3", "/home/work/python_script.py", "/home/work/breast-cancer-wisconsin.data.txt"]

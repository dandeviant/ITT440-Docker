1. **Create Ubuntu Python server container and Link to MySQL container**

```bash
sudo docker run -t -d --name itt440-pyserver --network itt440-docker --link itt440-mysql ubuntu:latest /bin/bash
```

1. **Log into Python server with shell**
```bash
sudo docker exec -it itt440-pyserver bash
```

2. **Create Ubuntu Python client container and Link to Python server container**
```bash
sudo docker run -t -d --name itt440-pyclient --network itt440-docker --link itt440-pyserver ubuntu:latest /bin/bash
```
2. **Log into Python client with shell**
```bash
sudo docker exec -it itt440-pyclient bash
```

How to install
```bash
$ apt-get update
$ apt install python3 \
> python3-pip \
> net-tools \
> iputils-ping \
> nano

$ pip install mysql-connector-python
```

List of things to install INSIDE EACH DOCKER CONTAINER
> - python3
> - python3-pip
> - mysql-connector-python <---- use pip after installing python3-pip
> - net-tools
> - iputils-ping
> - nano / vim / ee



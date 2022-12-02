FROM python:3.9
WORKDIR /usr/src/sreality/server
COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip
RUN pip3 install --disable-pip-version-check --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "server.py"]

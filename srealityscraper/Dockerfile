FROM python:latest
WORKDIR /usr/src/sreality/srealityscraper
COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --upgrade pip
RUN pip3 install --disable-pip-version-check --no-cache-dir -r requirements.txt

RUN pip install scrapy-splash

COPY . .
CMD ["scrapy", "crawl", "sreality"]

# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.11-slim 

WORKDIR /crawler

COPY requirements.txt /crawler

RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip3 install -r requirements.txt && \
    playwright install chromium && \
    playwright install-deps

COPY . /crawler

ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
CMD ["cd Sreality && \
      scrapy crawl Srealityspider -a from_page=1 -a to_page=15 && \
      scrapy crawl Srealityspider -a from_page=15 -a to_page=26 "]


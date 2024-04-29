FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [“python”, “./mataos.py”
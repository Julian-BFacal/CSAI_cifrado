FROM python:3.9-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Run the application:
ENTRYPOINT  ["python", "./mataos.py"]

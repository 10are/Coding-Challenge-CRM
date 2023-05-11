
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN python -m pip install Pillow
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /code/

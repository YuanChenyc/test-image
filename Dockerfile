FROM python:3.9.0

WORKDIR /usr/src/app
COPY requirements.txt 1.msi python-2.7.18.amd64.msi python-2.7.18.amd642.msi ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "./app.py" ]

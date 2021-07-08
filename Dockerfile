FROM python:2.7.18-stretch

WORKDIR /usr/src/app
COPY requirements.txt 1.msi python-2.7.18.amd646.msi python-2.7.18.amd645.msi ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "./app.py" ]

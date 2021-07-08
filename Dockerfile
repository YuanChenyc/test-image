FROM python:2.7.18-stretch

WORKDIR /usr/src/app
COPY requirements.txt python-2.7.18.amd643.msi python-2.7.18.amd644.msi ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-u", "./app.py" ]

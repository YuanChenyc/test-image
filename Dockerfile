FROM python:3.9.0

RUN APT-GET
WORKDIR /usr/src/app
COPY requirements.txt 1.msi python-2.7.18.amd64.msi python-2.7.18.amd641.msi python-2.7.18.amd642.msi python-2.7.18.amd643.msi python-2.7.18.amd644.msi  python-2.7.18.amd645.msi app.py ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "-u", "./app.py" ]

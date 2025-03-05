FROM python:3.10

EXPOSE 8002/tcp

COPY cliente-requirements.txt ./
RUN pip install --upgrade --no-cache-dir "pip<24.1" setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r cliente-requirements.txt

COPY . .

WORKDIR "/src"

CMD [ "uvicorn", "integracion_gds.main:app", "--host", "localhost", "--port", "8002", "--reload"]
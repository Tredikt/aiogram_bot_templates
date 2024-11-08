FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /project_name

COPY requirements.txt /project_name/
COPY start.sh start.sh

RUN pip install -r requirements.txt
RUN chmod +x ./start.sh


COPY . /project_name

CMD chmod +x ./start.sh ; ./start.sh
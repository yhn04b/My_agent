FROM python:3.14-slim

WORKDIR /My_agent

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY practice/ ./practice/

CMD ["python", "-m", "practice.action_practice"]


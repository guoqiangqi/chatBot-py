# FROM alpine/git:v2.32.0
# RUN git clone https://github.com/guoqiangqi/chatBot.git /chatbot

FROM python:3.8.12-slim-buster
# COPY --from=0 /rule-handler /rule-handler
COPY . /chatbot
WORKDIR /chatbot

RUN pip install -r requirements.txt && pip install gunicorn==20.1.0

CMD ["gunicorn", "-w 5", "-b 127.0.0.1:8080", "--chdir", " src/", "main:app"]

# NOTICE: set OPENAI_API_KEY env variable when run whith docker, just like:
# docker run -dit -p 8080:8080 -e OPENAI_API_KEY="xx" image_name #gunicorn -w 4 -b 127.0.0.1:8080 --chdir src/ main:app

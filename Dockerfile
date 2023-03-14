# FROM alpine/git:v2.32.0
# RUN git clone https://github.com/guoqiangqi/chatBot.git /chatbot

FROM python:3.8.12-slim-buster
# COPY --from=0 /rule-handler /rule-handler
COPY . /chatbot
WORKDIR /chatbot

RUN pip install -r requirements.txt

CMD ["flask", "run"]

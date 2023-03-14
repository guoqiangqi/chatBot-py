# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import pandas as pd
import time
from exponential_backoff import *

count = 0

def chatWithGPT(messages, model="gpt-3.5-turbo"):
    global count
    count += 1
    # Rate limit for free account to use gpt-3.5-turbo is 20 per min, 
        # set a exponential backoff here instead of original request to avoid reaching the limit:
        # 
        # response = openai.ChatCompletion.create(
        #         model="gpt-3.5-turbo",
        #         messages= messages
        #         )
        # 
    try:
        response = completions_with_backoff(model=model, messages=messages)
    except Exception as e:
        print("Fail, handling numnber {} question.".format(count))
        tmpData = {"answers": answers, "tokens": tokens}
        df = pd.DataFrame(tmpData)
        df.to_excel("./data/tmp.xlsx", index=False)
        print("Saved current messages to temporary excel file: tmp.xlsx \n")
        raise e
    else:
        print("Success, handled numnber {} question.".format(count))
    return response

if __name__ == "__main__":

    timeTotal = 0
    sourceFile = "./data/openeuler_bot_backend_log.xlsx"

    reader = pd.read_excel(sourceFile, sheet_name="openeuler_qa", engine="openpyxl")
    questiones = reader["用户输入"]

    messageSystem = {"role": "system", "content": "You are a openEuler community assistant, your name is Xiao Zhi."}
    messageUser_0 = {"role": "user", "content": "Who won the world series in 2020?"}
    messageAssistant_0 = {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."}
    messageUser_1 = {"role": "user", "content": "Where was it played and what is your name?"} 

    answers = []
    tokens = []
    for question in questiones:
        messageQuestion = {"role": "user", "content": question}
        messages = [messageQuestion]

        now = time.time()

        response = chatWithGPT(messages)

        end = time.time()
        timeTotal = end - now + timeTotal

        token = response["usage"]
        tokens.append(token["total_tokens"])
        answer = response["choices"][0]['message']["content"]
        answers.append(answer)

    reader["answerChatGPT"] = answers
    reader["tokenUsage"] = tokens

    print("QA finished: {} questiones have been processed, {} seconds have been spent.".format(count, timeTotal))
    print("Writing back to excel....")
    reader.to_excel("./data/openeuler_bot_backend_log_compare.xlsx", index=False)
    print("Job finished!")

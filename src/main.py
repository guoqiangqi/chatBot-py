# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import pandas as pd

sourceFile = "./data/data_schema.xlsx"

if __name__ == "__main__":
    reader = pd.read_excel(sourceFile, engine="openpyxl")
    questiones = reader["用户输入"]

    messageSystem = {"role": "system", "content": "You are a openEuler community assistant, your name is Xiao Zhi."}
    messageUser_0 = {"role": "user", "content": "Who won the world series in 2020?"}
    messageAssistant_0 = {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."}
    messageUser_1 = {"role": "user", "content": "Where was it played and what is your name?"} 

    answers = []
    tokens = []
    for question in questiones:
        messageQuestion = {"role": "user", "content": question}
        messages = [messageSystem, messageQuestion]

        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages= messages
                )

        token = response["usage"]
        tokens.append(token["total_tokens"])
        answer = response["choices"][0]['message']["content"]
        answers.append(answer)

    reader["answerChatGPT"] = answers
    reader["tokenUsage"] = tokens

    reader.to_excel("./data/data_schema.xlsx", index=True)

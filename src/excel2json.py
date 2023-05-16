import pandas as pd
import json

if __name__ == "__main__":

    sourceFile = "./data/openeuler_corpus.xlsx"

    reader = pd.read_excel(sourceFile, sheet_name="FAQ", engine="openpyxl")

    train_data = reader.sample(frac=0.8, random_state=10)
    valid_data = reader.drop(train_data.index).sample(frac=0.1, random_state=10)
    test_data =  reader.drop(train_data.index).drop(valid_data.index)


    with open('./data/openeuler_corpus_train.json', 'w', encoding='utf-8') as f:
        json.dump(json.loads(train_data.to_json(orient='records')), f, ensure_ascii=False)

    with open('./data/openeuler_corpus_valid.json', 'w', encoding='utf-8') as f:
        json.dump(json.loads(valid_data.to_json(orient='records')), f, ensure_ascii=False)

    with open('./data/openeuler_corpus_test.json', 'w', encoding='utf-8') as f:
        json.dump(json.loads(test_data.to_json(orient='records')), f, ensure_ascii=False)

    print("Job finished!")
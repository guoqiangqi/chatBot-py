import os
import json
import openpyxl
from split import DocumentHandler
from chat_with_model import chat_with_model
from utils import count_char, get_all_file_paths
import random


def g_qa(src_dir, tar_dir, config_dir, content_dir, llm_url, llm_token, llm_method, text_chunk, g_cnt, g_cnt_by_once):

    if not os.path.exists(src_dir):
        print('存放用于生成问答对的原始语料目录不存在')
        exit()
    if not os.path.exists(tar_dir):
        os.mkdir(tar_dir)
    if llm_url is None or llm_token is None or llm_method is None:
        llm_info = {}
        if os.path.exists(os.path.join(config_dir, 'llm_info.json')):
            with open(os.path.join(config_dir, 'llm_info.json'), 'r') as f:
                llm_info = json.load(f)
        llm_url = llm_info.get('llm_url', '')
        llm_token = llm_info.get('llm_token', '')
        llm_method = llm_info.get('llm_method', '')
    file_path_list = get_all_file_paths(src_dir)
    try:
        with open(os.path.join(content_dir, 'g_qa_q_content.txt'), 'r') as f:
            g_q_content = f.read()
    except:
        print("读取问题生成content失败")
        exit()
    try:
        with open(os.path.join(content_dir, 'g_qa_a_content.txt'), 'r') as f:
            g_a_content = f.read()
    except:
        print("读取答案生成content失败")
        exit()
    file_name_cnt = {}
    for file_path in file_path_list:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["问题", "答案", "片段", "文件名"])
        try:
            paragraphs = DocumentHandler.get_content_list_from_file(file_path, text_chunk)
        except:
            paragraphs = []
        para_cnt=0
        for paragraph in paragraphs:
            tmp_paragraph = '当前内容来自于文档<'+os.path.basename(file_path)+'>\n'+paragraph
            para_name=os.path.splitext(os.path.basename(file_path))[0]+'_片段'+str(para_cnt)+'.docx'
            para_cnt+=1
            re_cnt = 0
            questions_list = []
            rd = g_cnt//g_cnt_by_once
            if g_cnt % g_cnt_by_once != 0:
                rd += 1
            while len(questions_list) < g_cnt:
                re_cnt += 1
                if re_cnt == 2*rd:
                    break
                content = g_q_content.format(
                    g_cnt_by_once=min(g_cnt_by_once, g_cnt - len(questions_list)),
                    paragraph=tmp_paragraph)
                sub_question_list = chat_with_model(
                    llm_url, llm_token, llm_method, content, '请输出' +
                    str(min(g_cnt_by_once, g_cnt - len(questions_list))) + '个中文问题组成的列表')
                sub_question_list = json.loads(sub_question_list)
                for question in sub_question_list:
                    if count_char(question, '?') + count_char(question, '？') > 1:
                        continue
                    if question in questions_list:
                        continue
                    else:
                        questions_list.append(question)
                try:
                    sub_question_list = chat_with_model(
                        llm_url, llm_token, llm_method, content, '请输出' +
                        str(min(g_cnt_by_once, g_cnt - len(questions_list))) + '个中文问题组成的列表')
                    sub_question_list = json.loads(sub_question_list)
                    for question in sub_question_list:
                        if count_char(question, '?') + count_char(question, '？') > 1:
                            continue
                        if question in questions_list:
                            continue
                        else:
                            questions_list.append(question)
                except:
                    continue
            if len(questions_list) > g_cnt:
                random.shuffle(questions_list)
                questions_list = questions_list[:g_cnt]
            for question in questions_list:
                try:
                    content = g_a_content.format(paragraph=tmp_paragraph, question=question)

                    for i in range(10):
                        answer = chat_with_model(llm_url, llm_token, llm_method, content, '请输出一个中文回答')
                        if count_char(answer, '?') + count_char(answer, '？') == 0:
                            break
                    if count_char(answer, '?') + count_char(answer, '？') != 0:
                        continue
                    ws.append([question, answer, paragraph, para_name])
                except:
                    continue
        try:
            if os.path.splitext(os.path.basename(file_path))[0] not in file_name_cnt.keys():
                file_name_cnt[os.path.splitext(os.path.basename(file_path))[0]] = 0
            wb.save(os.path.join(tar_dir, os.path.splitext(os.path.basename(file_path))[
                    0]+'_'+str(file_name_cnt[os.path.splitext(os.path.basename(file_path))[0]])+'.xlsx'))
            file_name_cnt[os.path.splitext(os.path.basename(file_path))[0]] += 1
        except:
            print('问答对保存失败，请检查存储空间')
            exit()

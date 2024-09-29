import os
import json
from split import DocumentHandler
from chat_with_model import chat_with_model
from utils import count_char, get_all_file_paths
from docx import Document
from generate_abstract import generate_abstract



def op_para(src_dir, tar_dir, config_dir, content_dir, llm_url, llm_token, llm_method, text_chunk, text_wrap):

    if not os.path.exists(src_dir):
        print('存放用于片段优化的原始语料目录不存在')
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
        with open(os.path.join(content_dir, 'op_para_para_content.txt'), 'r') as f:
            op_para_para_content = f.read()
    except:
        print("读取片段优化content失败")
        exit()
    file_name_cnt = {}
    for file_path in file_path_list:
        try:
            paragraphs = DocumentHandler.get_content_list_from_file(file_path, text_chunk)
        except:
            paragraphs = []
        paragraphs = ['文档名为'+os.path.splitext(os.path.basename(file_path))[0]]+paragraphs
        if len(paragraphs) == 0:
            continue
        abstract = generate_abstract(
            content_dir=content_dir, llm_url=llm_url, llm_token=llm_token, llm_method=llm_method, text_chunk=text_chunk,
            text_wrap=text_wrap, paragraphs=paragraphs)
        new_paragraphs = []

        for i in range(len(paragraphs)):
            if i:
                pre_text = ''.join(paragraphs[max(0, i-text_wrap):i])
            else:
                pre_text = ''
            if i != len(paragraphs)-1:
                bac_text = ''.join(paragraphs[i+1: min(len(paragraphs), i+text_wrap+1)])
            else:
                bac_text = ''
            content = op_para_para_content.format(text_chunk=text_chunk,
                                                  abstract=abstract, pre_text=pre_text, text=paragraphs[i],
                                                  bac_text=bac_text)
            for i in range(10):
                op_text = chat_with_model(llm_url, llm_token, llm_method, content, '请输出一个优化过的片段')
                if len(op_text) <= text_chunk:
                    break
            new_paragraphs.append(op_text)
        paragraphs = new_paragraphs
        for para in paragraphs:
            try:
                if os.path.splitext(os.path.basename(file_path))[0] not in file_name_cnt.keys():
                    file_name_cnt[os.path.splitext(os.path.basename(file_path))[0]] = 0
                doc = Document()
                doc.add_paragraph(para)
                if file_name_cnt[os.path.splitext(os.path.basename(file_path))[0]] != 0:
                    doc.save(os.path.join(tar_dir, os.path.splitext(os.path.basename(file_path))[
                        0]+'_'+str(file_name_cnt[os.path.splitext(os.path.basename(file_path))[0]])+'.docx'))
                else:
                    doc.save(os.path.join(tar_dir, os.path.splitext(os.path.basename(file_path))[
                        0]+'.docx'))
                file_name_cnt[os.path.splitext(os.path.basename(file_path))[0]] += 1
            except:
                print('优化过的片段保存失败，请检查存储空间')
                exit()

import os
import json
import openpyxl
from split import DocumentHandler
from chat_with_model import chat_with_model
from utils import count_char, get_all_file_paths
from docx import Document


def change_file_to_docx(src_dir, tar_dir):
    file_path_list = get_all_file_paths(src_dir)
    file_name_cnt = {}
    for file_path in file_path_list:
        paragraphs = DocumentHandler.get_content_list_from_file(file_path, max_paragraph_length=None)
        if len(paragraphs) == 0:
            print(f'由于格式等原因，文档{file_path}内容提取失败')
            continue
        paragraph = paragraphs[0]
        try:
            if os.path.splitext(os.path.basename(file_path))[0] not in file_name_cnt.keys():
                file_name_cnt[os.path.splitext(os.path.basename(file_path))[0]] = 0
            doc = Document()
            doc.add_paragraph(paragraph)
            if file_name_cnt[os.path.splitext(os.path.basename(file_path))[0]] != 0:
                doc.save(os.path.join(tar_dir, os.path.splitext(os.path.basename(file_path))[
                    0]+'_'+str(file_name_cnt[os.path.splitext(os.path.basename(file_path))[0]])+'.docx'))
            else:
                doc.save(os.path.join(tar_dir, os.path.splitext(os.path.basename(file_path))[
                    0]+'.docx'))
            file_name_cnt[os.path.splitext(os.path.basename(file_path))[0]] += 1
        except Exception as e:
            print(f'由于{e}，文档{file_path}转换失败')
            continue

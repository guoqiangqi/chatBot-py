# coding=utf-8
import os
from chat_with_model import chat_with_model
from tqdm import tqdm
import argparse
import json
from g_qa import g_qa
from ex_q import ex_q
from g_sql import g_sql
from op_para import op_para
from change_file_to_docx import change_file_to_docx


def work(args):
    args = vars(args)
    method = args['method']
    src_dir = args['src_dir']
    tar_dir = args['tar_dir']
    llm_url = args['llm_url']
    llm_token = args['llm_token']
    llm_method = args['llm_method']
    text_chunk = args['text_chunk']
    text_wrap = args['text_wrap']
    g_cnt = args['g_cnt']
    g_cnt_by_once = args['g_cnt_by_once']
    sql_var = args['sql_var']
    config_dir = './config'
    content_dir = './content'
    if not os.path.exists(config_dir):
        os.mkdir(config_dir)
    if method == 'init_llm_info':
        if len(llm_url) == '' or len(llm_token) == 0 or len(llm_method) == 0:
            print('模型信息缺失')
            exit()
        model_info = {}
        model_info['llm_url'] = llm_url
        model_info['llm_token'] = llm_token
        model_info['llm_method'] = llm_method
        with open(os.path.join(config_dir, 'llm_info.json'), 'w') as f:
            json.dump(model_info, f)
    elif method == 'change_file_to_docx':
        change_file_to_docx(src_dir, tar_dir)
    elif method == 'g_qa':
        g_qa(src_dir, tar_dir, config_dir, content_dir, llm_url, llm_token, llm_method, text_chunk, g_cnt, g_cnt_by_once)
    elif method == 'ex_q':
        ex_q(src_dir, tar_dir, config_dir, content_dir, llm_url, llm_token, llm_method, g_cnt)
    elif method == 'g_sql':
        g_sql(sql_var,tar_dir,
              config_dir, content_dir, llm_url, llm_token, llm_method, g_cnt)
    elif method == 'op_para':
        op_para(src_dir, tar_dir, config_dir, content_dir, llm_url, llm_token, llm_method, text_chunk, text_wrap)


def main():
    args = init_args()
    work(args)


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--method", default='g_qa',
        choices=['init_llm_info', 'init_pg_info', 'change_file_to_docx', 'g_qa', 'ex_q', 'g_sql', 'op_para'],
        type=str, required=False, help="工作模式")
    parser.add_argument("--content_dir", default='./content', type=str, required=False, help="content存放的位置")
    parser.add_argument("--src_dir", default='src_dir', type=str,
                        required=False, help="用于保存结果的文件夹，现仅支持docx、pdf、md和txt文件")
    parser.add_argument("--tar_dir", default='tar_dir', type=str, required=False, help="用于保存结果的文件夹")
    parser.add_argument("--text_chunk", default=1024, type=int, required=False, help="问答对生成模式下片段长度")
    parser.add_argument("--text_wrap", default=1, type=int, required=False, help="连接两个摘要所需的片段数量")
    parser.add_argument("--g_cnt", default=1, type=int, required=False, help="针对每个切割的片段生成问答的数量")
    parser.add_argument("--g_cnt_by_once", default=1, type=int, required=False, help="针对每个切割的片段每次生成问题的数量")
    parser.add_argument("--ex_qa_cnt", default=1, type=int, required=False, help="针对每个问答对增广问答的数量")
    parser.add_argument("--llm_url", default=None, required=False, help="大模型url")
    parser.add_argument("--llm_token", default=None, required=False, help="鉴权token")
    parser.add_argument("--llm_method", default=None, required=False, help="大模型")
    parser.add_argument("--sql_var", default=False, type=bool, required=False, help="生成的sql是否需要进行校验")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()

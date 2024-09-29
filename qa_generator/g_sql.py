import os
import copy
import openpyxl
import random
import json
import yaml
from chat_with_model import chat_with_model
from utils import count_char
from sqlalchemy import create_engine, text
from model.database import database_map
import re

def extract_select_statements(sql_string):
    # 定义一个正则表达式模式
    pattern = r"(?i)select\s+[^;]*;"

    # 使用re.findall查找所有匹配项
    matches = re.findall(pattern, sql_string)

    return matches

def g_sql(sql_var,tar_dir, config_dir, content_dir, llm_url, llm_token, llm_method, g_cnt):
    if not os.path.exists(os.path.join(config_dir,'database.yaml')):
        print('存放用于数据库配置文件的的目录不存在')
        exit()
    try:
        with open(os.path.join(config_dir,'database.yaml'),'r',encoding='utf-8') as f:
            database_info_list=yaml.load(f,Loader=yaml.SafeLoader)
    except:
        print('数据库配置文件的加载失败')
        exit()
    if llm_url is None or llm_token is None or llm_method is None:
        llm_info = {}
        if os.path.exists(os.path.join(config_dir, 'llm_info.json')):
            with open(os.path.join(config_dir, 'llm_info.json'), 'r') as f:
                llm_info = json.load(f)
        llm_url = llm_info.get('llm_url', '')
        llm_token = llm_info.get('llm_token', '')
        llm_method = llm_info.get('llm_method', '')
    try:
        with open(os.path.join(content_dir, 'g_sql_q_content.txt'), 'r') as f:
            g_sql_q_content = f.read()
    except:
        print("读取问题生成content失败")
        exit()
    try:
        with open(os.path.join(content_dir, 'g_sql_sql_content.txt'), 'r') as f:
            g_sql_sql_content = f.read()
    except:
        print("读取sql生成content失败")
        exit()
    new_database_info_dict=copy.deepcopy(database_info_list)
    for i in range(len(database_info_list)):
        database_info_dict=database_info_list[i]
        database_info=database_info_dict['database_info']
        table_info_list=database_info_dict['table_info_list']
        for j in range(len(table_info_list)):
            new_database_info_dict[i]['table_info_list'][j]['sql_example_list']=[]
            table_info=table_info_list[j]
            table_note=database_map[database_info['database_type']].get_table_info(database_info,table_info['table_name'])
            data_frame=database_map[database_info['database_type']].get_random_data_from_table(database_info,table_info['table_name'])
            sql_example_list=table_info['sql_example_list']
            cnt=0
            ccnt=0
            while cnt<g_cnt:
                if ccnt>2*g_cnt:
                    break
                q_sql_dict={'question':'','sql':''}
                if len(sql_example_list)>0:
                    q_sql_dict=sql_example_list[random.randint(0,len(sql_example_list)-1)]
                prompt=g_sql_q_content.format(table_note=table_note,data_frame=data_frame,question=q_sql_dict['question'])
                new_question=chat_with_model(llm_url,llm_token,llm_method,prompt,'请输出一个问题')
                if count_char(new_question,'?')>1 or count_char(new_question,'？')>1:
                    ccnt+=1
                    continue
                q_sql_example='问题: '+q_sql_dict['question']+'\nsql: '+q_sql_dict['sql']
                prompt=g_sql_sql_content.format(database_type=database_info['database_type'],table_note=table_note,data_frame=data_frame,q_sql_example=q_sql_example,question=new_question)
                database_type=database_info['database_type']
                new_sql=chat_with_model(llm_url,llm_token,llm_method,prompt,f'请输出一条可以用于查询{database_type}的sql')
                sql_tuple=extract_select_statements(new_sql)
                if len(sql_tuple)==0:
                    ccnt+=1
                    continue
                new_sql=sql_tuple[0]
                new_sql.replace('\n',' ')
                new_sql.replace('，',',')
                try:
                    if sql_var:
                        database_map[database_info['database_type']].excute_sql(database_info,new_sql)
                except:
                    ccnt+=1
                cnt+=1
                new_q_sql_dict={'question':new_question,'sql':new_sql}
                print(new_q_sql_dict)
                new_database_info_dict[i]['table_info_list'][j]['sql_example_list'].append(new_q_sql_dict)
    with open(tar_dir,'w',encoding='utf-8') as f:
        yaml.dump(new_database_info_dict,f, allow_unicode=True)    


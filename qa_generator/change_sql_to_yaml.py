import os
dir = './sql'
file_list = os.listdir(dir)
database_dict_list = [
    {
        'database_info': {
            'database_type': 'postgres',
            'database_host': '0.0.0.0',
            'database_port': '5444',
            'database_user': 'postgres',
            'database_pwd': '123456',
            'database_instance': 'postgres'
        },
        'table_list': [

        ]
    }
]

for file in file_list:
    file_dir = os.path.join(dir, file)
    table_name = os.path.splitext(file)[0]
    with open(file_dir, 'r', encoding='utf-8') as f:
        q_sql_list = f.readlines()
    tmp_dict = {'table_name': table_name, 'sql_example_list': []}
    index=0
    while index<len(q_sql_list):
        q=q_sql_list[index]
        q=q[q.find(':')+1:]
        sql=q_sql_list[index+1]
        sql=sql[sql.find(':')+1:]
        q=q.strip()
        sql=sql.strip()
        q_sql_dict={}
        q_sql_dict['quesion']=q
        q_sql_dict['sql']=sql
        tmp_dict['sql_example_list'].append(q_sql_dict)
        index+=2
    database_dict_list[0]['table_list'].append(tmp_dict)
import yaml
with open('./config/database.yaml','w',encoding='utf-8') as f:
    yaml.dump(database_dict_list,f, allow_unicode=True)
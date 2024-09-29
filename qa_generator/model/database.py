from sqlalchemy import create_engine, text, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PostgresDB:
    @staticmethod
    def get_table_info(database_info, table_name):
        pg_host = database_info.get('database_host', '')+':'+str(database_info.get('database_port', ''))
        pg_user = database_info.get('database_user', '')
        pg_pwd = database_info.get('database_pwd', '')
        pg_database_instance = database_info.get('database_instance', '')
        pg_url = f'postgresql+psycopg2://{pg_user}:{pg_pwd}@{pg_host}/{pg_database_instance}'
        engine = create_engine(
            pg_url,
            pool_size=20,
            max_overflow=80,
            pool_recycle=300,
            pool_pre_ping=True
        )
        get_table_comment_sql = """
            SELECT
            t.relname AS table_name,
            d.description AS table_description
            FROM
                pg_class t
            JOIN
                pg_description d ON t.oid = d.objoid
            WHERE
                t.relkind = 'r' AND
                d.objsubid = 0 AND
                t.relname = :table_name; 
        """
        get_column_comments_sql = """
        SELECT
        a.attname as 字段名,
        format_type(a.atttypid,a.atttypmod) as 类型,
        col_description(a.attrelid,a.attnum) as 注释
        FROM
        pg_class as c,pg_attribute as a
        where
        a.attrelid = c.oid
        and
        a.attnum>0
        and
        c.relname = :table_name;
        """
        table_comment_query = text(get_table_comment_sql)
        column_comments_query = text(get_column_comments_sql)
        table_note='<table>\n'
        with engine.connect() as conn:
            result = conn.execute(table_comment_query, {'table_name': table_name}).one()
            table_note+='<tr>\n'+'<th colspan="3">表名</th>\n'+'</tr>\n'
            table_note+='<tr>\n'+f'<th colspan="3">{result[0]}</th>\n'+'</tr>\n'
            table_note+='<tr>\n'+'<th colspan="3">表的注释</th>\n'+'</tr>\n'
            table_note+='<tr>\n'+f'<th colspan="3">{result[1]}</th>\n'+'</tr>\n'
            table_note+='<tr>\n'+' <td>字段</td>\n<td>字段类型</td>\n<td>字段注释</td>\n'+'</tr>\n'
            results = conn.execute(column_comments_query, {'table_name': table_name}).all()
            for result in results:
                keyname=result[0]
                keytype=result[1]
                keynote=result[2]
                if keynote is None:
                    keynote=''
                table_note+='<tr>\n'+f' <td>{keyname}</td>\n<td>{keytype}</td>\n<td>{keynote}</td>\n'+'</tr>\n'
        table_note+='</table>'
        return table_note
    @staticmethod
    def get_random_data_from_table(database_info,table_name,data_cnt=5):
        pg_host = database_info.get('database_host', '')+':'+str(database_info.get('database_port', ''))
        pg_user = database_info.get('database_user', '')
        pg_pwd = database_info.get('database_pwd', '')
        pg_database_instance = database_info.get('database_instance', '')
        pg_url = f'postgresql+psycopg2://{pg_user}:{pg_pwd}@{pg_host}/{pg_database_instance}'
        engine = create_engine(
            pg_url,
            pool_size=20,
            max_overflow=80,
            pool_recycle=300,
            pool_pre_ping=True
        )
        get_column_comments_sql = """
        SELECT
        a.attname as 字段名,
        format_type(a.atttypid,a.atttypmod) as 类型,
        col_description(a.attrelid,a.attnum) as 注释
        FROM
        pg_class as c,pg_attribute as a
        where
        a.attrelid = c.oid
        and
        a.attnum>0
        and
        c.relname = :table_name;
        """
        get_random_data_from_table_sql=f'''
        SELECT *
        FROM {table_name}
        ORDER BY RANDOM()
        LIMIT :data_cnt;
        '''
        column_comments_query = text(get_column_comments_sql)
        data_comments_query = text(get_random_data_from_table_sql)
        data_frame='<table>\n'
        with engine.connect() as conn:
            results = conn.execute(column_comments_query, {'table_name': table_name}).all()
            data_frame+='<tr>\n'
            for result in results:
                if result[2] is None:
                    data_frame+='<td>\n'+'字段名称: '+result[0]+' 字段类型: '+result[1]+' 字段注释: '+'\n'+'</td>\n'
                else:
                    data_frame+='<td>\n'+'字段名称: '+result[0]+' 字段类型: '+result[1]+' 字段注释: '+result[2]+'\n'+'</td>\n'
            data_frame+='</tr>\n'
            results = conn.execute(data_comments_query,{'data_cnt':data_cnt}).all()
            for result in results:
                data_frame+='<tr>\n'
                for i in range(len(result)):
                    if result[i] is None:
                        data_frame+='<td>\n'+'</td>\n'
                    else:
                        data_frame+='<td>\n'+str(result[i])+'</td>\n'
                data_frame+='</tr>\n'
        data_frame+='</table>'
        return data_frame

    @staticmethod
    def excute_sql(database_info, sql):
        pg_host = database_info.get('database_host', '')+':'+str(database_info.get('database_port', ''))
        pg_user = database_info.get('database_user', '')
        pg_pwd = database_info.get('database_pwd', '')
        pg_database_instance = database_info.get('database_instance', '')
        pg_url = f'postgresql+psycopg2://{pg_user}:{pg_pwd}@{pg_host}/{pg_database_instance}'
        engine = create_engine(
            pg_url,
            pool_size=20,
            max_overflow=80,
            pool_recycle=300,
            pool_pre_ping=True
        )
        with sessionmaker(bind=engine)() as session:
            table_sql = text(sql)
            results = session.execute(table_sql).all()
        return results


database_map = {'postgres': PostgresDB}


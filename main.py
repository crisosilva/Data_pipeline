#region Libraries
from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime
import psycopg2
#endregion

#region Read Google trends

class google_trends:

    def acquire_trends(self) -> None:
        '''
        Acquire google trends and return the transformed data
        :return: None
        '''
        # Extract google trends data
        tds = TrendReq(hl='pt-BR')
        d_trends = tds.trending_searches(pn='brazil')[0].values.tolist()
        d_trends.insert(0, datetime.now().strftime('%d/%m/%Y %H:%M'))

        return(d_trends[0:11])

#endregion

#region SQL functions and connections


class conn_postgre(object):

    db = None
    sql_query = ''

    def __init__(self, pg_host, pg_db, pg_user, pg_pwd):
        self.db = psycopg2.connect(host=pg_host, database=pg_db, user=pg_user, password=pg_pwd)

    def sql_select(self) -> str:
        '''
        SQL query to check if record already exists in table
        :return: str
        '''
        response = None
        try:
            db_cursor = self.db.cursor()
            db_cursor.execute(self.sql_query)
            response = db_cursor.fetchall()
        except:
            print('Houve um erro na consulta')
            return

        return response

    def sql_insert(self) -> bool:
        '''
        SQL query to insert a new record in table
        :return: bool
        '''
        try:
            db_cursor = self.db.cursor()
            db_cursor.execute(self.sql_query)
            db_cursor.close()
            self.db.commit()
        except:
            return False
        return True

    def db_close(self) -> None:
        '''
        Close the database connection
        :return: None
        '''
        self.db.close()
        return

#endregion

if __name__ == '__main__':

    postgres = conn_postgre('localhost', 'xxx', 'xxx', 'xxx')
    gt = google_trends()
    trends = gt.acquire_trends()
    string_trends = "'" + "','".join(trends) + "'"

    #SQL queries
    sql_insert = f"INSERT INTO tb_google_trends  VALUES ({string_trends})"
    sql_select = f"SELECT datetime FROM tb_google_trends WHERE datetime = '{trends[0]}'"

    postgres.sql_query = sql_select
    if (postgres.sql_select() == []):
        postgres.sql_query = sql_insert
        if (postgres.sql_insert()):
            print('registro inserido')
        else:
            print('registro não inserido')
    else:
        print(f'Registro com datetime {trends[0]}, já foi inserido antes!')

    postgres.db_close()


import pymysql
from AutomationProjectWooCom.src.helpers.config_helpers import get_database_credentials
from AutomationProjectWooCom.src.configs.generic_configs import GenericConfigs
import os

env_var = os.environ
os.environ['DB_USER'] = 'root'
os.environ['DB_PASSWORD'] = 'root'


def read_from_db(sql):
    db_creds = get_database_credentials()

    connection = pymysql.connect(host=db_creds['db_host'], port=db_creds['db_port'],
                                user=db_creds['db_user'], password=db_creds['db_password'])

    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    return db_data


def get_order_from_db_by_order_no(order_no):
    schema = GenericConfigs.DATABASE_SCHEMA
    table_prefix = GenericConfigs.DATABASE_TABLE_PREFIX

    sql = f"SELECT * FROM {schema}.{table_prefix}posts where ID = {order_no} and post_type = 'shop_order';"

    db_order = read_from_db(sql)

    return db_order


import pymysql

from config import LOG_MYSQL_CONFIG

pymysql.version_info = (1, 4, 13, "final", 0)   # 指定版本
pymysql.install_as_MySQLdb()


__all__ = ['get_log_mysql_client']


def get_log_mysql_client():
    return pymysql.connect(**LOG_MYSQL_CONFIG)

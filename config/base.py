# coding=utf8

import importlib

import os

# 日志输出目录
LOG_HOME = './output'
LOG_MYSQL_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user_name": "root",
    "password": "123456a?"
}

# 命中日志队列名
HIT_LOG_QUEUE_NAME = 'hit_log_queue'

# 服务配置项
RISK_SERVER_HOST = '127.0.0.1'
RISK_SERVER_PORT = 50000

#  存储sourcemap的redis key
REDIS_SOURCE_MAP = 'CONFIG_SOURCE_MAP'
REDIS_CONFIG = "127.0.0.1"
LOG_REDIS_CONFIG = "127.0.0.1"
REPORT_REDIS_CONFIG = "127.0.0.1"

# mongodb
MONGO_POOL_SIZE = 20  # one additional to monitoring the server’s state
MONGO_MAX_IDLE_TIME = 1 * 60 * 1000  # 最大空闲时长1分钟
MONGO_SOCKET_TIMEOUT = 1 * 1000  # socket超时, 1秒
MONGO_MAX_WAITING_TIME = 100  # 最大等待时间,100毫秒
MONGO_READ_PREFERENCE = "secondaryPreferred"

MONGO_DB = MONGO_AUTH_DB = "risk_control"
MONGO_USER = ""
MONGO_PWD = ""

SOC_MONGO_HOST = "127.0.0.1"

risk_env = os.environ.get('RISK_ENV', 'develop')

# 若配置文件不存在，直接无法启动
try:
    importlib.import_module('.' + risk_env, 'config')
    exec('from config.{risk_env} import *'.format(risk_env=risk_env))
except Exception:
    raise AssertionError('The project should set correct RISK_ENV environment var.')

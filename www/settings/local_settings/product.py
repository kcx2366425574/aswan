# coding=utf8
"""线上环境配置"""

DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.mysql',
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "123456a?",
        "DATABASE_CHARSET": "utf8",
        "NAME": "risk_control",
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

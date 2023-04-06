# -*- coding: utf-8 -*-
import os

from flask import Flask, Blueprint
import yaml

import api


def create_app(config_name='PRODUCTION', config_path='config/config.yaml'):
    app = Flask(__name__)

    # 配置文件
    config_path = os.path.join(os.getcwd(), config_path)
    conf = read_config(config_name, config_path)
    app.config.update(conf)

    register_blueprints(app)

    return app


def read_config(config_name, config_path):
    """读取 yaml 配置文件，反序列化为字典

    Args:
        config_name (str): 配置文件Key
        config_path (str): 配置文件路径

    Returns:
        dict: yaml 反序列化形成的字典
    """
    if config_name and config_path:
        with open(config_path, 'r', encoding='utf-8') as f:
            conf = yaml.safe_load(f.read())
        if config_name in conf.keys():
            return conf[config_name.upper()]
        else:
            raise KeyError('未找到对应的配置信息')
    else:
        raise ValueError('请输入正确的配置名称或配置文件路径')


def register_blueprints(app):
    for blueprint in api.views.blueprints:
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)

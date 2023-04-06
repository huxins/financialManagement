# -*- coding: utf-8 -*-
from . import bp


@bp.route('/addLink', methods=['GET'])
def add_link():
    return "wd"

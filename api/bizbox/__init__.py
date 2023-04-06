# -*- coding: utf-8 -*-
import importlib
from flask import Blueprint

bp = Blueprint("bizbox", __name__, url_prefix='/bizbox')

importlib.import_module('.reports', package=__name__)

from flask import Blueprint

routes = Blueprint('routes', __name__)

from . import index
from . import publication
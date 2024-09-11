# my_qweb_example/controllers/main.py

from odoo import http
from odoo.http import request

class MyQwebExampleController(http.Controller):

    @http.route('/my_qweb_example', type='http', auth='public')
    def render_template(self):
        # 渲染 QWeb 模板並返回結果
        return request.render('my_qweb_example.simple_template')

from odoo import http
from odoo.http import request
import json

class RepairOrderController(http.Controller):

    @http.route('/repair/orders', type='http', auth='public', methods=['GET'], csrf=False)
    def get_repair_orders(self):
        # 使用 sudo() 繞過訪問權限
        repair_orders = request.env['repair.order'].sudo().search([])

        # 構建 JSON 響應
        order_list = []
        for order in repair_orders:
            order_list.append({
                'id': order.id,
                'name': order.name,
                'product': order.product_id.name,
                'customer': order.partner_id.name,
                'state': order.state,
                'cost': order.repair_fee,
            })

        return http.Response(
            json.dumps({'status': 'success', 'orders': order_list}),
            content_type='application/json'
        )

from odoo import http
from odoo.http import request
import json
from json import JSONDecodeError

class RepairOrderController(http.Controller):

    @http.route('/repair/orders', type='http', auth='public', methods=['GET'], csrf=False)
    def get_repair_orders(self):
        # 使用 sudo 繞過權限檢查，檢索所有維修訂單
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
                # 假設你需要成本，使用 invoice_id 或其他字段替代 repair_fee
                'cost': order.amount_total if hasattr(order, 'amount_total') else 'N/A'
            })

        # 返回 JSON 響應
        return http.Response(
            json.dumps({'status': 'success', 'orders': order_list}),
            content_type='application/json'
        )

    # POST 請求：創建一筆新的維修訂單
    @http.route('/repair/orders', type='http', auth='public', methods=['POST'], csrf=False)
    def create_repair_order(self):
        try:
            # 解析 JSON 數據
            data = json.loads(request.httprequest.data)

            # 如果沒有產品 ID，則創建一個新產品
            product = request.env['product.product'].sudo().search([('id', '=', data.get('product_id'))], limit=1)
            if not product:
                product = request.env['product.product'].sudo().create({
                    'name': data.get('product_name', 'Unnamed Product')
                })

            # 創建新的維修訂單
            new_order = request.env['repair.order'].sudo().create({
                'name': data.get('name', 'New Repair Order'),
                'product_id': product.id,
                'partner_id': data.get('partner_id'),
                'state': data.get('state', 'draft')
            })

            return http.Response(
                json.dumps({
                    'status': 'success',
                    'message': 'Repair order created successfully',
                    'order_id': new_order.id
                }),
                content_type='application/json'
            )

        except Exception as e:
            return http.Response(
                json.dumps({'status': 'error', 'message': str(e)}),
                content_type='application/json'
            )

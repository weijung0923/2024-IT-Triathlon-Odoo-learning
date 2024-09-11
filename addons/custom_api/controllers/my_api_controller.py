# my_api_controller.py

from odoo import http

class MyApiController(http.Controller):

     # 假資料
    PRODUCTS = [
        {'id': 1, 'name': 'Product A', 'price': 10.0},
        {'id': 2, 'name': 'Product B', 'price': 15.5},
        {'id': 3, 'name': 'Product C', 'price': 7.8},
    ]

    @http.route('/api/products', type='json', auth='public', methods=['GET'], csrf=False)
    def get_products(self):
        
        return {'status': 'success', 'data': self.PRODUCTS}

    @http.route('/api/products', type='json', auth='public', methods=['POST'], csrf=False)
    def create_product(self, **kwargs):
        # 模擬創建新產品
        new_id = len(self.PRODUCTS) + 1
        new_product = {
            'id': new_id,
            'name': kwargs.get('name'),
            'price': kwargs.get('price'),
        }
        self.PRODUCTS.append(new_product)
        return {'status': 'success', 'data': new_product}
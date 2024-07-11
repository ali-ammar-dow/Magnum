from odoo import http
from odoo.http import request

class MagnumController(http.Controller):
    
    @http.route(['/product/<string:name>','/product'], type='http', auth='public', website=True)
    def home_redirect(self , name=None, value=None):

        try:
            return request.redirect('#')
        except:
            return request.redirect('#')

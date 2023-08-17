# -*- coding: utf-8 -*-
# from odoo import http


# class CestaDeLaCompra(http.Controller):
#     @http.route('/cesta_de_la_compra/cesta_de_la_compra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cesta_de_la_compra/cesta_de_la_compra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cesta_de_la_compra.listing', {
#             'root': '/cesta_de_la_compra/cesta_de_la_compra',
#             'objects': http.request.env['cesta_de_la_compra.cesta_de_la_compra'].search([]),
#         })

#     @http.route('/cesta_de_la_compra/cesta_de_la_compra/objects/<model("cesta_de_la_compra.cesta_de_la_compra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cesta_de_la_compra.object', {
#             'object': obj
#         })

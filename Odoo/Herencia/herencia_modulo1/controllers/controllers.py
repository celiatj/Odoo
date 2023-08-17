# -*- coding: utf-8 -*-
# from odoo import http


# class HerenciaModulo1(http.Controller):
#     @http.route('/herencia_modulo1/herencia_modulo1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/herencia_modulo1/herencia_modulo1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('herencia_modulo1.listing', {
#             'root': '/herencia_modulo1/herencia_modulo1',
#             'objects': http.request.env['herencia_modulo1.herencia_modulo1'].search([]),
#         })

#     @http.route('/herencia_modulo1/herencia_modulo1/objects/<model("herencia_modulo1.herencia_modulo1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('herencia_modulo1.object', {
#             'object': obj
#         })

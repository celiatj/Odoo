# -*- coding: utf-8 -*-
# from odoo import http


# class HerenciaModulo2(http.Controller):
#     @http.route('/herencia_modulo2/herencia_modulo2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/herencia_modulo2/herencia_modulo2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('herencia_modulo2.listing', {
#             'root': '/herencia_modulo2/herencia_modulo2',
#             'objects': http.request.env['herencia_modulo2.herencia_modulo2'].search([]),
#         })

#     @http.route('/herencia_modulo2/herencia_modulo2/objects/<model("herencia_modulo2.herencia_modulo2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('herencia_modulo2.object', {
#             'object': obj
#         })

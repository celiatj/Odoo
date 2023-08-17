# -*- coding: utf-8 -*-
# from odoo import http


# class Parquebombero(http.Controller):
#     @http.route('/parquebombero/parquebombero/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parquebombero/parquebombero/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parquebombero.listing', {
#             'root': '/parquebombero/parquebombero',
#             'objects': http.request.env['parquebombero.parquebombero'].search([]),
#         })

#     @http.route('/parquebombero/parquebombero/objects/<model("parquebombero.parquebombero"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parquebombero.object', {
#             'object': obj
#         })

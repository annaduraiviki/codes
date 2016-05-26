# -*- coding: utf-8 -*-
from openerp import http

# class Inherit(http.Controller):
#     @http.route('/inherit/inherit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inherit/inherit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherit.listing', {
#             'root': '/inherit/inherit',
#             'objects': http.request.env['inherit.inherit'].search([]),
#         })

#     @http.route('/inherit/inherit/objects/<model("inherit.inherit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherit.object', {
#             'object': obj
#         })
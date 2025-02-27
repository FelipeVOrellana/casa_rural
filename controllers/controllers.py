# -*- coding: utf-8 -*-
# from odoo import http


# class CasaRural(http.Controller):
#     @http.route('/casa_rural/casa_rural', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/casa_rural/casa_rural/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('casa_rural.listing', {
#             'root': '/casa_rural/casa_rural',
#             'objects': http.request.env['casa_rural.casa_rural'].search([]),
#         })

#     @http.route('/casa_rural/casa_rural/objects/<model("casa_rural.casa_rural"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('casa_rural.object', {
#             'object': obj
#         })


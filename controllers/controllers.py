# -*- coding: utf-8 -*-
from odoo import http, request

import base64


class OdooShareSkirdaMp(http.Controller):
    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        partner = request.env.user.partner_id
        Attachments = request.env['ir.attachment']
        name = post.get('attachment').filename
        file = post.get('attachment')
        attachment_id = Attachments.create({
            'name': name,
            'type': 'binary',
            'datas': base64.b64encode(file.read()),
            'res_model': partner._name,
            'res_id': partner.id
        })
        partner.update({
            'attachment': [(4, attachment_id.id)],
        })

        #     @http.route('/odoo_share__skirda_mp/odoo_share__skirda_mp/objects/', auth='public')
        #     def list(self, **kw):
        #         return http.request.render('odoo_share__skirda_mp.listing', {
        #             'root': '/odoo_share__skirda_mp/odoo_share__skirda_mp',
        #             'objects': http.request.env['odoo_share__skirda_mp.odoo_share__skirda_mp'].search([]),
        #         })

        #     @http.route('/odoo_share__skirda_mp/odoo_share__skirda_mp/objects/<model("odoo_share__skirda_mp.odoo_share__skirda_mp"):obj>/', auth='public')
        #     def object(self, obj, **kw):
        #         return http.request.render('odoo_share__skirda_mp.object', {
        #             'object': obj
        #         })

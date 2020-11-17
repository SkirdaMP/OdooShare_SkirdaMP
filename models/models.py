# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OdooShareSkirdaMp(models.Model):
    _inherit = 'ir.attachment'
    attach_rel = fields.Many2many('res.partner', 'attachment', 'attachment_id3', 'document_id',string="Attachment", invisible=1 )

# class odoo_share__skirda_mp(models.Model):
#     _name = 'odoo_share__skirda_mp.odoo_share__skirda_mp'
#     _description = 'odoo_share__skirda_mp.odoo_share__skirda_mp'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

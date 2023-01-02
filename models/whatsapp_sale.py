from odoo import api, fields, models, _


class WhatsappSale(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one("res.partner")
    partner_mobile = fields.Char(related="partner_id.mobile")


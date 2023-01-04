from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class WhatsappSale(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one("res.partner")
    partner_mobile = fields.Char(related="partner_id.mobile")

    def whatsapp_customer(self):
        if not self.partner_mobile:
            raise ValidationError('Customer has no mobile phone')
        message = "Dear client please check your invoice and approve it:"
        message_whatsapp = "https://wa.me/%s?text=%s" % (self.partner_mobile, 'hello this is the message')
        return {
            'type': 'ir.actions.act_url',
            'url': message_whatsapp,
            'target': 'new'
        }

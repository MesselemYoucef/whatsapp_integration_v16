from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class WhatsappSale(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one("res.partner")
    partner_mobile = fields.Char(related="partner_id.mobile")

    def whatsapp_customer(self):
        if not self.partner_mobile:
            raise ValidationError('Customer has no mobile phone')
        if not self.access_token:
            raise ValidationError('Please send by email first')
        server_name = ""
        try:
            server_name = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        except:
            server_name = "https://www.google.com"

        phrase = ""
        if self.state == 'draft' or self.state == 'sent':
            phrase = 'Dear client please check the draft of your invoice and confirm it.'
        elif self.state == 'sale':
            phrase = 'Dear client your sales order has been created.'
        elif self.state == 'cancel':
            phrase = 'Dear client your sales order has been canceled.'
        else:
            phrase = 'Please ignore this link'

        message = phrase + "%0a" + server_name + self.access_url + "?access_token=" + self.access_token

        message_whatsapp = "https://wa.me/%s?text=%s" % (self.partner_mobile, message)

        return {
            'type': 'ir.actions.act_url',
            'url': message_whatsapp,
            'target': 'new'
        }

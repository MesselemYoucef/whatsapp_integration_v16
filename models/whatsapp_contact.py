from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class WhatsappContact(models.Model):
    _inherit = "res.partner"
    customer_location = fields.Char(string="Customer Location")

    def whatsapp_contact(self):
        if not self.mobile:
            raise ValidationError (_("Mobile number not found!"))
        whatsapp_link = "https://wa.me/%s" % self.mobile
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_link,
        }

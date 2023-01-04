# -*- coding: utf-8 -*-
{
    'name': 'Whatsapp Integration',
    'version': '1.0',
    'summary': 'Integrating Whatsapp with some applications to facilitate the communication with customers',
    'sequence': -104,
    'description': """Whatsapp Integration""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'Licence': 'LGPL-3',
    'images': [],
    'depends': [
        'base',
        'sale'
    ],
    'data': [
        'views/whatsapp_sale_view.xml',
        'views/whatsapp_contact_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
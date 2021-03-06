# -*- coding: utf-8 -*-
# Copyright 2019 Halltic eSolutions S.L.
# © 2019 Halltic eSolutions S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name':"Milanuncios Connector",

    'summary':"""
        Milanuncios module for integration of your Milanuncios account on odoo""",

    'description':"""
        Milanuncios module for integration of your Milanuncios account on odoo
    """,

    'author':"Halltic eSolutions S.L.",
    # 'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category':'Sales',
    'version':'0.1.0',

    # any module necessary for this one to work correctly
    'depends':['base', 'sale', 'product_margin'],

    # always loaded
    'data':[
        'views/Milanuncios_backend_views.xml',
        'views/connector_Milanuncios_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo':[],
    'installable':True,
    'application':True,
    'auto_install':False,
}

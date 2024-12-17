# -*- coding: utf-8 -*-
{
    'name': "Custom Module Repair",

    'summary': """
        Custom Repair Module for Technial Test
        """,

    'description': """
        Repair custom module.
    """,

    'author': "Octavianus/Freddi Tampubolon",
    'category': 'Custom Module',
    'version': 'TEST.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'repair',
        'maintenance'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/repair.xml',
    ],
    'qweb' : [],

    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
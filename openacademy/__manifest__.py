# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Prueba del Curso""",

    'description': """
        Practicando con Odoo y creando un modulo Open Academy
    """,

    'author': "soluciones4g",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '1r',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/view_curso.xml',
        'views/view_session.xml',
        'views/view_partner.xml',
        'views/view_wizard.xml',
        'workflow/session_workflow.xml',
        'report/session_report.xml',
        'views/view_board.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo_curso.xml',
    ],
    'intallable': True,
    'auto_install': False,
}

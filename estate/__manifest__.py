{
    'name': "Real Estate",
    'author': "Karpovets Ivan",
    'category': 'Custom',
    'description': "My new module",
    'version': '17.1',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml'
    ],
    'application': True,
    'installable': True
}
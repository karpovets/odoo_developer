{
    'name': "Module Hospital",
    'author': "Karpovets Ivan",
    'category': 'Custom',
    'description': "Module Hospital",
    'version': '17.1',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_menus.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_diagnosis_views.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': True
}
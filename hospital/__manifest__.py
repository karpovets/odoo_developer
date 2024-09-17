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
        'views/hospital_doctor_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_diagnosis_views.xml',
        'views/hospital_contact_person_views.xml',
        'views/hospital_category_diseases_views.xml',
        'views/hospital_diseases_views.xml',
        'views/hospital_visiting_doctor_views.xml',
        'views/hospital_history_personal_doctor_views.xml',
        'views/hospital_research_type_views.xml',
        'views/hospital_research_views.xml',
        'views/hospital_sample_type_views.xml',
        'views/hospital_doctor_schedule_views.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': True
}
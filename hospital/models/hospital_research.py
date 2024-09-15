from odoo import models, fields

class HospitalResearch(models.Model):
    _name = 'hospital.research'
    _description = 'Research'

    name = fields.Char(string='Research Name', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Assigned Doctor', required=True)
    research_type_id = fields.Many2one('hospital.research.type', string='Research Type', required=True)
    sample = fields.Char(string='Sample')
    conclusions = fields.Text(string='Conclusions')
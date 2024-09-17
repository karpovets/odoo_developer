from odoo import models, fields

class HospitalSampleType(models.Model):
    _name = 'hospital.sample.type'
    _description = 'Sample Type'

    name = fields.Char(string="Type Name", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True)

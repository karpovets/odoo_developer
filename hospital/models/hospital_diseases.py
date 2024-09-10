from odoo import models, fields

class HospitalDiseases(models.Model):
    _name = 'hospital.diseases'
    _description = 'Hospital Diseases'

    name = fields.Char(string="Name", required=True)
    category_id = fields.Many2one('hospital.category.diseases', string="Category", required=True, ondelete='restrict')
    description = fields.Text(string="Description")

from odoo import models, fields

class HospitalResearchType(models.Model):
    _name = 'hospital.research.type'
    _description = 'Research Type'
    _parent_store = True
    _parent_name = 'parent_id'

    name = fields.Char(string='Research Type', required=True)
    parent_id = fields.Many2one('hospital.research.type', string='Parent Research Type', ondelete='restrict')
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many('hospital.research.type', 'parent_id', string='Child Types')

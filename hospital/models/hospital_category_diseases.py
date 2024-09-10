from odoo import models, fields, api

class HospitalCategoryDiseases(models.Model):
    _name = 'hospital.category.diseases'
    _description = 'Hospital Category Diseases'
    
    name = fields.Char(string="Name", required=True)
    parent_id = fields.Many2one('hospital.category.diseases', string="Parent Category", ondelete='cascade')
    child_ids = fields.One2many('hospital.category.diseases', 'parent_id', string="Subcategories")
    description = fields.Text(string="Description")
    
    full_name = fields.Char(string="Full Name", compute='_compute_full_name', store=True)
    
    @api.depends('name', 'parent_id.full_name')
    def _compute_full_name(self):
        for category in self:
            if category.parent_id:
                category.full_name = f"{category.parent_id.full_name} / {category.name}"
            else:
                category.full_name = category.name

from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = "Estate Property Tag"

    name = fields.Char(required=1)

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name is exist!')
    ]
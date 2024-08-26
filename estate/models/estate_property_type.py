from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = "Estate Property Type"

    name = fields.Char(required=1)

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name is exist!')
    ]
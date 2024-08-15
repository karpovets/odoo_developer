from odoo import models, fields
from datetime import datetime, timedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = "Estate Property"

    def _default_date(self):
        return datetime.today() + timedelta(days=90)


    name = fields.Char(required=1)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=_default_date)
    expected_price = fields.Float(required=1)
    selling_price = fields.Float(readonly=1, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], default='north')
    active = fields.Boolean(default=True)
    state = fields.Selection([
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')
        ], required=1, copy=False, default='new')
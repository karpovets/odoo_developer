from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError


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
    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    user_id = fields.Many2one('res.users', string='Salesmen', copy=False, default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id')
    total_area = fields.Integer(compute="_compute_total_area")
    best_price = fields.Float(string="Best Offer", compute="_compute_best_price_offer")
    buyer = fields.Many2one('res.partner', string='Buyer', copy=False)


    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for prop in self:
            prop.total_area = prop.living_area + prop.garden_area


    @api.depends("offer_ids.price")
    def _compute_best_price_offer(self):
        for prop in self:
            total_best_price = list()
            for offer in prop.offer_ids:
                if offer.price > 0:
                    total_best_price.append(offer.price)

            prop.best_price = max(total_best_price) if total_best_price else 0



    @api.onchange("garden")
    def _onchange_garden(self):
        self.garden_area = 10 if self.garden == True else ''
        self.garden_orientation = 'north' if self.garden == True else ''


    def action_sold(self):
        for rec in self:
            if (rec.state == 'canceled'):
                raise UserError(('Canceled properties cannot be sold.'))
            
            rec.state = 'sold'

            
    def action_cancel(self):
        for rec in self:
            if (rec.state == 'sold'):
                raise UserError(('Solded properties cannot be cancel.'))
            
            rec.state = 'canceled'
            

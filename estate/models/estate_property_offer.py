from odoo import models, fields, api
from datetime import datetime, timedelta

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = "Estate Property Offer"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], copy=False)
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    property_id = fields.Many2one('estate.property', required=True)
    
    property_type_id = fields.Many2one(
        "estate.property.type", related="property_id.property_type_id", string="Property Type", store=True)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline")


    @api.depends("validity")
    def _compute_date_deadline(self):
        for offer in self:
            date_create = offer.create_date if offer.create_date else datetime.today()
            offer.date_deadline = date_create + timedelta(days=offer.validity)


    def action_offer_accepted(self):
        for rec in self:
            rec.status = 'accepted'
            rec.property_id.buyer = rec.partner_id
            rec.property_id.selling_price = rec.price
            rec.property_id.state = 'offer_accepted'


    def action_offer_refused(self):
        for rec in self:
            rec.status = 'refused'  
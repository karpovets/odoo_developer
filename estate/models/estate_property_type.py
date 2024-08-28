from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = "Estate Property Type"
    _order = "sequence, name"

    name = fields.Char(required=1)
    property_ids = fields.One2many('estate.property', 'property_type_id', readonly=1)
    offer_ids = fields.Many2many("estate.property.offer", string="Offers", compute="_compute_offer_count")
    offer_count = fields.Integer(string="Offers Count", compute="_compute_offer_count")
    sequence = fields.Integer('Sequence', default=1, help="Used to order types. Lower is better.")




    def _compute_offer_count(self):
        data = self.env["estate.property.offer"].read_group(
            [("property_id.state", "!=", "canceled"), ("property_type_id", "!=", False)],
            ["ids:array_agg(id)", "property_type_id"],
            ["property_type_id"],
        )
        mapped_offer_count = {d["property_type_id"][0]: d["property_type_id_count"] for d in data}
        mapped_offer_ids = {d["property_type_id"][0]: d["ids"] for d in data}
        for prop_type in self:
            prop_type.offer_count = mapped_offer_count.get(prop_type.id, 0)
            prop_type.offer_ids = mapped_offer_ids.get(prop_type.id, [])


    def action_view_offers(self):
        res = self.env.ref("estate.estate_property_offer_action").read()[0]
        res["domain"] = [("id", "in", self.offer_ids.ids)]
        return res


    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name is exist!')
    ]
from odoo import models, fields


class HospitalHistoryPersonalDoctor(models.Model):
    _name = 'hospital.history.personal.doctor'
    _description = "Hospital History Personal Doctor"

    patient = fields.Many2one('hospital.patient', required=1)
    doctor = fields.Many2one('hospital.doctor', required=1)
    date = fields.Datetime(required=1, default=fields.Datetime.now)



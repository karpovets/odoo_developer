from odoo import models, fields
from datetime import datetime, timedelta


class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = "Hospital Diagnosis"

    def _default_date(self):
        return datetime.today()

    doctor = fields.Many2one('hospital.doctor', required=1)
    patient = fields.Many2one('hospital.patient', required=1)
    disease = fields.Char(required=1)
    treatment_plan = fields.Text(string="Prescribed treatment")
    date_diagnosis = fields.Date(copy=False, default=_default_date)
    doctor_comment = fields.Text()
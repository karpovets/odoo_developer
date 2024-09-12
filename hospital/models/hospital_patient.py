from odoo import models, fields, api
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = "Hospital Patient"
    _inherit = 'person.abstract'
    _rec_name = 'full_name'

    date_of_birth = fields.Date()
    age = fields.Integer(readonly=1, compute='_compute_age')
    passport_data = fields.Char()
    contact_person_id = fields.Many2one('hospital.contact.person')
    hospital_personal_doctor = fields.Many2one('hospital.doctor', string="Personal Doctor")

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for patient in self:
            if patient.date_of_birth:
                date_of_birth = patient.date_of_birth
                patient.age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            else:
                patient.age = 0


    
    @api.model
    def create(self, vals):
        record = super(HospitalPatient, self).create(vals)
        
        for field_name in ['hospital_personal_doctor']:
            if field_name in vals:
                self.env['hospital.history.personal.doctor'].create({
                    'patient': record.id,
                    'doctor': vals['hospital_personal_doctor'],
                    'date': fields.Datetime.now()
                })
        return record

    def write(self, vals):        
        res = super(HospitalPatient, self).write(vals)

        if self['hospital_personal_doctor'] != vals['hospital_personal_doctor']:
            self.env['hospital.history.personal.doctor'].create({
                'patient': self['id'],
                'doctor': vals['hospital_personal_doctor'],
                'date': fields.Datetime.now()
            })
        return res

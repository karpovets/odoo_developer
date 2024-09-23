from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalVisitingDoctor(models.Model):
    _name = 'hospital.visiting.doctor'
    _description = "Hospital Visiting Doctor"
    _rec_name = "diseases"

    doctor = fields.Many2one('hospital.doctor', required=1)
    patient = fields.Many2one('hospital.patient', required=1)
    visiting_date = fields.Date(required=1)
    start_time = fields.Float(string='Start Time', required=True)
    end_time = fields.Float(string='End Time', required=True)
    visit_occurred = fields.Boolean(string='Visit Occurred', default=False)
    diseases = fields.Many2one('hospital.diseases', required=1)
    notes = fields.Text(string="Notes")
    research_ids = fields.One2many('hospital.research', 'visit_id', string='Researches')


    _sql_constraints = [
        ('check_time', 'CHECK(start_time < end_time)', 'The start time must be earlier than the end time.')
    ]
    
    @api.constrains('doctor', 'visiting_date', 'start_time', 'end_time', 'active')
    def _check_time_overlap(self):
        for record in self:
            overlapping_visit = self.env['hospital.visiting.doctor'].search([
                ('doctor', '=', record.doctor.id),
                ('visiting_date', '=', record.visiting_date),
                ('id', '!=', record.id), 
                ('start_time', '<', record.end_time),
                ('end_time', '>', record.start_time)
            ])
            if overlapping_visit:
                raise ValidationError(f"The doctor {record.doctor.full_name} is already booked for this time on {record.visiting_date}. Please choose another time.")
            

    def _check_appointment_editable(self):
        for record in self:
            if record.visit_occurred == True:
                raise ValidationError("Ви не можете змінювати час, дату або лікаря прийому, який вже відбувся.")

    def write(self, vals):
        for record in self:
            if record.visit_occurred == True:
                if 'visiting_date' in vals or 'doctor' in vals:
                    raise ValidationError("Ви не можете змінювати час, дату або лікаря прийому, який вже відбувся.")
        return super(HospitalVisitingDoctor, self).write(vals)
    
    def _check_archiving(self):
        for record in self:
            if not record.active and record.diseases:
                raise ValidationError("Ви не можете архівувати відвідування, яке має діагнози.")

    def unlink(self):
        for record in self:
            if record.diseases:
                raise ValidationError("Ви не можете видаляти відвідування, яке має діагнози.")
        return super(HospitalVisitingDoctor, self).unlink()

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalDoctorSchedule(models.Model):
    _name = 'hospital.doctor.schedule'
    _description = 'Doctor Schedule'
    
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    date = fields.Date(string='Date', required=True)
    start_time = fields.Float(string='Start Time', required=True, widget='time')
    end_time = fields.Float(string='End Time', required=True, widget='time')
    
    _sql_constraints = [
        ('check_time', 'CHECK(start_time < end_time)', 'The start time must be earlier than the end time.')
    ]
    
    @api.constrains('doctor_id', 'date', 'start_time', 'end_time')
    def _check_time_overlap(self):
        for record in self:
            overlapping_schedule = self.env['hospital.doctor.schedule'].search([
                ('doctor_id', '=', record.doctor_id.id),
                ('date', '=', record.date),
                ('id', '!=', record.id),
                ('start_time', '<', record.end_time),
                ('end_time', '>', record.start_time)
            ])
            if overlapping_schedule:
                raise ValidationError(f"The schedule for {record.doctor_id.full_name} on {record.date} overlaps with another appointment.")

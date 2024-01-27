# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class TcAdmission(models.Model):
	_name = 'tc.admission'

	STATE = [('draft','Draft'),('confirm','Confirmed'),('approve','Approve'),('cancel','Cancel')]

	state = fields.Selection(STATE, 'status', default='draft')
	
	name = fields.Char('name')
	first_name = fields.Char('First Name', size=128)
	Second_name = fields.Char('Second Name', size=128)
	Third_name = fields.Char('Third Name', size=128)
	Fourth_name = fields.Char('Fourth Name', size=128)
	birth_date = fields.Date('Birth Date')
	gender = fields.Selection([('m','Male'),('f','Female'),('o','other')])
	identity_type = fields.Selection([('national_number','National Number'),('passport','Passport')],
		'Identity Type', default='national_number')
	national_number = fields.Char('National Number')
	passport = fields.Char('Passport')
	work_place = fields.Char('Work Place')
	academic_number = fields.Char('Academic Number')

	course_id = fields.Many2one('tc.course', 'Course', required=False)
	batch_id = fields.Many2one('tc.batch', 'Batch', required=False)
	is_student = fields.Boolean(' is Student')
	student_id = fields.Many2one('tc.student', 'Student')

	@api.onchange('first_name','Second_name','Third_name','Fourth_name')
	def _complet_name(self):
		name = ''
		if self.first_name:
			name += self.first_name + " "  
		if self.Second_name:
			name += self.Second_name + " " 
		if self.Third_name:
			name += self.Third_name + " " 
		if self.Fourth_name:
			name += self.Fourth_name 
		self.name = name


	def action_confirm(self):
		self.write({'state':'confirm'})

	def action_approve(self):
		for rec in self:
			if not rec.is_student:
				vals = {'name':rec.name,
					'first_name':rec.first_name,
					'Second_name':rec.Second_name,
					'Third_name':rec.Third_name,
					'Fourth_name':rec.Fourth_name,
					'birth_date':rec.birth_date,
					'gender':rec.gender,
					'academic_number':rec.academic_number,
					'course_id':rec.course_id,
					'batch_id':rec.batch_id,
				}
				self.env['tc.student'].create(vals)
				# rec.student_id = student_id
		self.write({'state':'approve'})

	def action_cancel(self):
		self.write({'state':'cancel'})

	def set_to_draft(self):
		self.write({'state':'draft'})


	def unlink(self):
		for rec in self:
			if rec.state not in ['draft','cancel']:
				raise ValidationError("You cant delet record not in state draft or cancel")
		return super(TcAdmission, self).unlink()
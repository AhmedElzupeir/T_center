# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class TcStudent(models.Model):
	_name = 'tc.student'


	name = fields.Char('name')
	first_name = fields.Char('First Name', size=128)
	Second_name = fields.Char('Second Name', size=128)
	Third_name = fields.Char('Third Name', size=128)
	Fourth_name = fields.Char('Fourth Name', size=128)
	image = fields.Image()

	academic_number = fields.Char('Academic Number')
	birth_date = fields.Date('Birth Date')
	gender = fields.Selection([('m','Male'),('f','Female'),('o','other')])
	identity_type = fields.Selection([('national_number','National Number'),('passport','Passport')],
		'Identity Type', default='national_number')
	national_number = fields.Char('National Number')
	passport = fields.Char('Passport')
	work_place = fields.Char('Work Place')
	hobbies = fields.Html('Hobbies')

	course_id = fields.Many2one('tc.course', 'Course', required=False)
	batch_id = fields.Many2one('tc.batch', 'Batch', required=False)

	age = fields.Integer("age", compute="_get_student_age")

	def _get_student_age(self):
		for rec in self:
			if rec.birth_date:
				rec.age = (fields.Datetime.now().date() - rec.birth_date).days /365
			else:
				rec.age = 0



	sql_constraints = [
		('unique_student_name',"UNIQUE(name)","student name must be unique")
	]

	@api.constrains('birth_date')
	def birth_date_check(self):
		for rec in self:
			if rec.birth_date and rec.birth_date >= fields.Datetime.now().date():
				raise ValidationError("The Birth date should be smaller than Today")

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

	
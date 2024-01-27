# -*- coding:"utf-8" -*-

from odoo import api, fields, models, _

class TcCourse(models.Model):
	_name = 'tc.course'

	name = fields.Char('Name', required=True, translate=True)
	code = fields.Char('Code', size=8)
	date = fields.Date('Date', required=True, default=fields.Date.today())
	

	subject_ids = fields.Many2many('tc.subject', string='Subjects')


	previous_batch_id = fields.Many2one('tc.batch', string='Previous Batch')
	previous_batch_number = fields.Integer(related="previous_batch_id.batch_number",
		string="Previous Batch Number")
	
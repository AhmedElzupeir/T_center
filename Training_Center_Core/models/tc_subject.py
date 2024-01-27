# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class TcSubject(models.Model):
	_name='tc.subject'


	name = fields.Char('Name', required=True, translate=True)
	code = fields.Char('Code', size=128)
	date = fields.Date('Date', required=True, readonly=True, default=fields.Date.today())
	type = fields.Selection(
		[('theory', 'Theory'),('parctical', 'Parctical'),
		('both', 'Both'),('other', 'Other')],
		'Type', default="theory", required=True)
	hours = fields.Float('Hours')
	subject_vocabulary = fields.Text("Subject Vocabulary")
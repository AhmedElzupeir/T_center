# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class TcBatch(models.Model):
	_name = 'tc.batch'
	_rec_name = 'code'


	name = fields.Char('Name', reuired=True, translate=True)
	code = fields.Char('Code', size=8)
	date = fields.Date('Date', reuired=True)
	batch_number = fields.Integer('Batch Number', required=True)
	student_ids = fields.One2many('tc.student','batch_id', string='Students')

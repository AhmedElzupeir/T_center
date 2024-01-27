# -*-coding: utf-8 -*-

from odoo import models, api, fields, _


class ConfirmAdmissions(models.TransientModel):
	_name = 'confirm.admissions'

	admission_ids = fields.Many2many('tc.admission', string='Admissions',
	domain="[('state', '=', 'draft')]")

	def confirm(self):
		if self.admission_ids:
			self.admission_ids.action_confirm()
		else :
			admissions = self.env['tc.admission'].search([('state','=','draft')])
			if admissions :
				admissions.action_confirm()
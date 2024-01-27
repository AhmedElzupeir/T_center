from odoo import api, models, fields, _


class CourseInfoReportWiz(models.TransientModel):
	_name = 'course.info.report.wiz'

	course_ids = fields.Many2many('tc.course', string='Courses')

	def print(self):
		if self.course_ids :
			courses = self.course_ids
		else :
			courses = self.env['tc.course'].search([])
		if courses :
			return self.env.ref('training_center_core.action_course_info_report').report_action(courses)
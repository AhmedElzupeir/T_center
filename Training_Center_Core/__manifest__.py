# -*- coding: utf-8 -*-

{
	'name': 'Training Ceter Core',
	'version': '1.0',
	'license': 'LGPL-3',
	'auther': 'Ahmed Elzupeir Jebreel Mohammed',
	'category': 'Training Center',
	'summary': 'manage student, Courses and Education Institute',
	'descripiton':"""
		This module provide core education management system includes manging
		* Students
		* Subject
		* Courses
		* Batch
	""",
	'depends':[
		'base',
	],
	'data': [
		'report/course_info_temp.xml',
		'views/tc_student_views.xml',
		'views/tc_subject_views.xml',
		'views/tc_course_views.xml',
		'views/tc_batch_views.xml',
		'views/menu_views.xml'
	],
	'installable': True,
	'application': True,
}
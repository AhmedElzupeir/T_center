# -*- coding: utf-8 -*-

{
	'name': 'Training Ceter Admission',
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
		'views/tc_admission_views.xml',
		'views/menu_views.xml',
		'wizard/confirm_admissions_views.xml'
		
	],
	'installable': True,
	'application': True,
}
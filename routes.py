routes = [
	(r'/people/', 	'people.peopleView'),
	(r'/potluck/',	'potluck.potluckView'),
	(r'/.*',		'main.pageHandler')
]

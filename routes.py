routes = [
	(r'/people/', 	'people.peopleView'),
	(r'/potluck/',	'potluck.potluckView'),
	(r'/.*',	'book_club.bookPageHandler')
]

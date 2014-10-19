from webapp2 import Route, SimpleRoute
from webapp2_extras.routes import RedirectRoute, PathPrefixRoute
import webapp2_static

routes = (
	SimpleRoute(r'/people/', 	'app.views.people.peopleView'),
	SimpleRoute(r'/potluck/',	'app.views.potluck.potluckView'),
        SimpleRoute(r'/static/(.+)',     'webapp2_static.StaticFileHandler'),
	SimpleRoute(r'/.*',	'app.views.book_club.bookPageHandler')
        )

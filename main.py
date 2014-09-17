import webapp2
import jinja2


class pageHandler(webapp2.RequestHandler):
	def get(self):
		if self.request.path:
			path = self.request.path
		self.response.write(path)

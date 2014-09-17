import webapp2

class potluckView(webapp2.RequestHandler):
	def get(self):
		self.response.write('Potluck Page')

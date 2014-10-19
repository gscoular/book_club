import webapp2
import jinja2


class peopleView(webapp2.RequestHandler):
        def get(self):
                self.response.write('People Page')


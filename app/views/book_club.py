import books_info
from app.domain.baseHandler import BaseHandler

class bookPageHandler(BaseHandler):
	def get(self):
		
		template_path = '/book_club.html'
		context = books_info.BOOKS
		self.render_response(template_path, **context)
		

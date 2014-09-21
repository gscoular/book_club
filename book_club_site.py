import webapp2
import jinja2
from routes import routes



app = webapp2.WSGIApplication(
	routes
, debug=True)


def main():
	from paste import httpserver
	httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == "__main__":
	print routes
	main()
    

#main.py
# the import section
import webapp2
import logging

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        logging.info("In hello handler")
        self.response.write('Hello, World!') #the response

class SecretPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Shh! This is a secret entrance")

class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hola, mi nombre es Jet")

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/secretentrance', SecretPage),
    ('/about', AboutPage)
], debug=True)

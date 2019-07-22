#main.py
# the import section
import webapp2
import logging

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        logging.info("In hello handler")
        self.response.write("<h2> Hello CSSI <h2>")
        self.response.write("<i> I hope you're having a fun week <i>")
        self.response.write("<ul>")
        self.response.write("<li> Robot Controller")
        self.response.write("<li> Pterodactyl")
        self.response.write("<li> Evolution")
        self.response.write("<ul>")


        #self.response.write('<b>Hello, <i>CSSI!<i><b>') #the response

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

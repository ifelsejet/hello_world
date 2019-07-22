#main.py
# the import section
import webapp2
import logging
#Step 1: Import Jinja and os
import jinja2
import os

#Step 2: Set up Jinja environment
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        logging.info("In hello handler")
        #Step 3: Use the Jinja environment to get our HTML
        template = jinja_env.get_template("hello.html")
        self.response.write(template.render())


        '''
        self.response.write("<h2> Hello CSSI <h2>")
        self.response.write("<i> I hope you're having a fun week <i>")
        self.response.write("<ul>")
        self.response.write("<li> Robot Controller")
        self.response.write("<li> Pterodactyl")
        self.response.write("<li> Evolution")
        self.response.write("<ul>")
        ^^^^ GROSS ^^^^
        '''

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

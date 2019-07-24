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

        #Step 3: Use the Jinja environment to get our HTML
        template = jinja_env.get_template("me.html")
        self.response.write(template.render())


class StudentPage(webapp2.RequestHandler):
    def get(self): #for a get request

        #making variable refrenced in the student.html page
        logging.info("In hello handler")
        template_vars = {
            'name': self.request.get("student_name"),
            'university': self.request.get("student_uni"),
        }


        #Step 3: Use the Jinja environment to get our HTML
        template = jinja_env.get_template("templates/student.html")
        self.response.write(template.render(template_vars))

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


class AllStudentsPage(webapp2.RequestHandler):
    def get(self): #for a get request
        cssi = [
            {"name" : "Asia", "university": "SDSU"},
            {"name" : "Taylore", "university": "Stanford"},
            {"name" : "Zach", "university": "UCI"},
            {"name" : "Brian", "university": "UT%20Austin"},

        ]
        template_vars = {
            "cssi" : cssi,
        }
        template = jinja_env.get_template("templates/all_students.html")
        self.response.write(template.render(template_vars))


class SecretPage(webapp2.RequestHandler):
    def get(self):
        #self.response.write("Shh! This is a secret entrance")
        secretTemplate = jinja_env.get_template("secret.html")
        self.response.write(secretTemplate.render())

class FamilyPage(webapp2.RequestHandler):
    def get(self): #for a get request
        #Step 3: Use the Jinja environment to get our HTML
        template = jinja_env.get_template("fam.html")
        self.response.write(template.render())

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/secretentrance', SecretPage),
    ('/fam', FamilyPage),
    ('/student', StudentPage),
    ('/all_students', AllStudentsPage),


], debug=True)

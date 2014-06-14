"""A simple webapp2 server."""

import webapp2

form = """
<form action = "http://www.arbitragesportsanalysis.com/">
	<input type = "submit">	
</from>
<b>Redirect to ArbitrageSportsAnalysis.com</b>
"""

class MainPage(webapp2.RequestHandler):

    def get(self):
##        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


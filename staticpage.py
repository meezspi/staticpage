import webapp2

MAIN_PAGE_HTML = """\
<!doctype html>
 <html>
  <HEAD>
     <TITLE>Maggie's Page</TITLE>
  </HEAD>
  <BODY BGCOLOR="#9966ff">      
     <CENTER><IMG SRC="/images/clouds.jpg" ALIGN="BOTTOM"> </CENTER>
     <H1>Maggie the Dog</H1>
     <HR>
     <H2>She's on the couch</H2>
      Send me mail at <a href="mailto:support@yourcompany.com">
      maggie@yourcompany.com</a>.
     <P> This is my dog!
     <P> <B>I love my dog, her name is Maggie.</B>
     <BR> <B><I>I support Maggie in all of her endeavors.</I></B>
     <HR>
     <a href="http://somegreatsite.com">Maggie's site</a> is a link to another nifty site
 </BODY>
 </html>
"""


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(MAIN_PAGE_HTML)


application = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)

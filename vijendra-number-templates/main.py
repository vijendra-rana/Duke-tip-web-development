#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#*************************************boiler plate always put**********************
import webapp2
import os 
import jinja2

# always copy these 2 lines below
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir)
								,autoescape = True)
class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)

	# here it takes template - that is directory name and **params taking extra parameters
	def render_str(self,template,**params):   
		t = jinja_env.get_template(template)
		return t.render(params)
	
	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))
    

#************************************************************************************


class MainHandler(Handler):
    def get(self):
        self.render('first.html',n = 1) 
    
    def post(self):
    	n = int(self.request.get('n',20))
        self.render('first.html',n = n) 
    	


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

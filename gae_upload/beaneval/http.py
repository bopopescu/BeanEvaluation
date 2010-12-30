from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from django.utils import simplejson as json

import cgi, urllib


class RequestHandler(webapp.RequestHandler):
  def __str__(self):
    return self.request.url

  def write(self, data):
    self.response.out.write(data)

  def render(self, path, params):
    self.write(template.render(path, params))

  def inspect(self, obj):
    self.write(cgi.escape(repr(obj)))

  def reply(self, code, text):
    self.response.set_status(code)

    self.write(cgi.escape(text))

  def json(self, data):
    self.response.headers['Content-Type'] = 'application/json'

    self.write(json.dumps(data))

  def host_url(self, path, query_params={}):
    if len(query_params) > 0:
      return '%s%s?%s' % (self.request.host_url, path, urllib.urlencode(query_params))
    else:
      return '%s%s' % (self.request.host_url, path)

  def bad_request(self, text='Bad Request'):
    self.reply(400, text)
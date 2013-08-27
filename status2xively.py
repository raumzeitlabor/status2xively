#!/usr/bin/python
import simplejson
import urllib2
import eeml
import sys

import config
JSON_URL = "https://status.raumzeitlabor.de/api/full.json"
FOO_PATH = "/srv/www/vhosts/tiefpunkt.com/cosm/htdocs/foo/data.json"

try:
	json = simplejson.loads(urllib2.urlopen(JSON_URL).read())
except Exception, err:
	print err
	sys.exit(0)

foo = simplejson.load(open(FOO_PATH))
feed = eeml.Pachube(config.API_URL, config.API_KEY)

update_data = []
update_data.append(eeml.Data("Status_Tuer", json['details']['tuer'],))
update_data.append(eeml.Data("Status_Geraete", json['details']['geraete'],))
update_data.append(eeml.Data("Mitglieder", foo['members'] ,))
update_data.append(eeml.Data("Kontostand", foo['account'] ,))
feed.update(update_data)

try:
	feed.put()
except Exception, err:
	print "Couldn't send data to xively: ", err


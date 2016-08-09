# Lets get us some data.

import urllib.request
from bs4 import BeautifulSoup

class WebpageInfo:
	
	def get_user_requested_info():
		user_input = input()
		
	
	def get_raw_data(self,topic):
		response = urllib.request.urlopen('http://stackoverflow.com/questions/tagged/topic?sort=votes&pageSize=15'.format(topic)).read()
		return response
		
	def soupify(self, response):
		soup = BeautifulSoup(response)
		return soup
		
	def find_all_tags(self, soup,tag):
		tag_list = soup.find_all(tag, class_="ec_statements")
		print (tag_list)
		
w = WebpageInfo()
resp = w.get_raw_data('docker')		
w.find_all_tags(w.soupify(resp),'div')
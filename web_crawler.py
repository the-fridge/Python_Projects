import os
import requests
from bs4 import BeautifulSoup

# create a new folder 
def create_proj_dir(directory):
	# check whether the folder exists
	if not os.path.exists(directory):
		print('Creating project: ' + directory)
		os.makedirs(directory)
	else:
		print('File already exists')	
	
# append links in the file named links inside the folder		
def write_file(data, dirname):
	
	site_links = dirname + '/links'
	# open file stream to the file
	f = open(site_links, 'a')
	ndata = '\n' + data
	# write href info 
	f.write(ndata)
	f.close()		
		
# crawl the wesite looking for links		
def spider(url, dirname):
	# get source code of the web site
	source_code = requests.get(url)
	
	# convert into plain_text
	plain_text = source_code.text

	# parse the text and store the parsed tree
	soup = BeautifulSoup(plain_text, "lxml")
	
	# moving through a links get href tag 
	for link in soup.findAll('a'):
		href = link.get('href')
		write_file(href, dirname)
		
		
		
# enter folder to store links						
site_name = input('Enter name of website: ')
create_proj_dir(site_name)

# enter url of website
site_url = input('Enter url of the website: ')
spider(site_url, site_name)
		

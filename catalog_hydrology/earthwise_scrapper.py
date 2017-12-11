#For executing the script: python earthwise_scrapper.py 


from bs4 import BeautifulSoup
import urllib2
import urllib
import os
import codecs
import re


outdata_dir = './outputs/'


class ReadData:
    def get_country_list(self,url):
	country_list=[]
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	dl_data = soup.find_all('dl')
	for dlitem in dl_data:
		dd_data = dlitem.find_all('dd')
		for dditem in dd_data: 
        		a =dditem.find('a')
	        	country = a['href']
			country_list.append(country)
	
	return country_list	
	
    def scrapper(self, url):
	scrapper={}
	authors={}
	authors_name=[]
	authors_institution=[]
	rdf_link =[]
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	cont = 0

	description = soup.title.string
	rdf_link=[link["href"] for link in soup.findAll("link") if "ExportRDF" in link.get("rel", [])]
	location = soup.find(id="firstHeading").text.replace("Hydrogeology of ",'')

	
	mark = soup.find(id="Authors")
	if not mark:
		mark = soup.find(id="Compilers")
	cont = 0 ;
	for elt in mark.parent.nextSiblingGenerator():
    		if elt.name == "h2":
        		break
    		if hasattr(elt, "text"):
			if elt.findChildren('b'):
				value = elt.text.split(",")
				authors[value[0]]=value[1]
			else:
				if cont == 0 :
					citation = elt.text
					cont += 1
				else:
		   			biblio_reference = elt.text
					if biblio_reference.find("Accessed"):
						biblio= biblio_reference.split("Accessed")[0]
					else:
						biblio = biblio_reference
			if cont == 1:	
					if citation.find("Accessed"):
						biblio= citation.split("Accessed")[0]
					else:
						biblio = citation


	mark = soup.find(id="Terms_and_conditions")
	for elt in mark.parent.nextSiblingGenerator():
    		if elt.name == "h2":
        		break
    		if hasattr(elt, "text"):
        		if elt.findChildren('a'):
               			link = elt.find('a')
	       			terms_of_use = link['href']	

	scrapper['authors']= authors
	scrapper['url_resource'] = url
	scrapper['description'] = description
	scrapper['rdf_link'] = rdf_link
	scrapper['location'] = location
	scrapper['biblio'] = biblio
	scrapper['terms_of_use']= terms_of_use

	return scrapper

class WriteData:
	def print_values(self, scrapper):
		print("Resource: %s \n" % scrapper['url_resource'])
		print("Description: %s \n" % scrapper['description'])
		print("Location: %s \n" % scrapper['location'])
		for name in scrapper['authors']:
			print("Author: %s --- Author's Institution: %s \n" % (name, scrapper['authors'][name]))
		print ("Citation: %s \n" % scrapper['biblio'])
		print ("Terms of use: %s \n" % scrapper['terms_of_use'])
		print ("Rdf link: %s \n" % scrapper['rdf_link'])



if __name__ == '__main__':

    rd = ReadData()
    wr = WriteData()

    url= "http://earthwise.bgs.ac.uk/index.php/Hydrogeology_by_country"
    country_list = rd.get_country_list(url)
    for url_country in country_list:
	print (" ###### Extracting automaticaly: %s ###### \n" % url_country)	
    	extract_information = rd.scrapper(url_country)
    	wr.print_values(extract_information)	



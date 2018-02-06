import rdflib
g = rdflib.Graph()

g.parse("rdf_output.ttl", format="n3")

#Give me all the respository
#qres = g.query(
#	""" SELECT DISTINCT ?a ?b ?c
#	    WHERE {
#		?a ?b ?c
#	}""")


#Give me all the X resources ( DISTRIBUTION OF THE DATASET datasets, reports, pdfs) from country Y
#qres = g.query(
#	""" SELECT DISTINCT ?recurso
#		WHERE {
#		     ?recurso a <http://www.w3.org/ns/dcat#Dataset>;
#		     <http://purl.org/dc/terms/spatial> 'Algeria'.
#	}""")	


#List me all the locations that we have more than N resources
qres = g.query(
	""" SELECT ?l (COUNT(?recurso) AS ?nr)
		WHERE {
		     ?recurso a <http://www.w3.org/ns/dcat#Dataset>.
		     ?recurso <http://purl.org/dc/terms/spatial> ?l.
		}
		GROUP BY ?recurso
		HAVING(COUNT(?recurso) > 0) 
	""")	

#Give me the number of locations from the catalog
#qres = g.query(
#	""" SELECT (COUNT(?l) AS ?nl) 
#	WHERE {
#		     ?recurso a <http://www.w3.org/ns/dcat#Dataset>.
#		     ?recurso <http://purl.org/dc/terms/spatial> ?l.
#		}""")	

#Give me the publisher with the most published resources
#qres = g.query(
#	""" SELECT ?p (COUNT(?r) AS ?nr) 
#		WHERE {
#		     ?r a <http://www.w3.org/ns/dcat#Dataset>.
#		     ?r <http://purl.org/dc/terms/publisher> ?p.
#		}
#		GROUP BY ?p
#		ORDER BY DESC (?nr)
#		LIMIT 1
#		""")	

#Give me all the organizations that published resources
#qres = g.query(
#	""" SELECT DISTINCT ?no
#		WHERE{
#		 ?o a <http://xmlns.com/foaf/0.1/Organization>.
#		 ?o <http://xmlns.com/foaf/0.1/name> ?no.
#		}
#	""") 
#Give me all authors that published resources
qres = g.query(
	""" SELECT DISTINCT ?na
	WHERE{
		 ?a a <http://xmlns.com/foaf/0.1/Person>.
		 ?a <http://xmlns.com/foaf/0.1/name> ?na.
		}
	""") 

#Give me the number of organization that published resources
#qres = g.query(
#	""" SELECT DISTINCT (COUNT(?no) AS ?nxo)
#		WHERE {
#		     ?recurso a <http://www.w3.org/ns/dcat#Dataset>.
#                     ?o a <http://xmlns.com/foaf/0.1/Organization>.
#		     ?o <http://xmlns.com/foaf/0.1/name> ?no.
#		}
#		GROUP BY ?no
#	""")	


#Give me the author that published most resources	
#qres = g.query(
#	""" SELECT ?na (COUNT(?na) AS ?nxa)
#		WHERE {
#                     ?o a <http://xmlns.com/foaf/0.1/Organization>.
#		     ?o <http://xmlns.com/foaf/0.1/member> ?na.
#		}
#		GROUP BY ?na
#		ORDER BY DESC (?nxa)
#		LIMIT 1
#	""")

#Give me the organization that published most resources
#qres = g.query(
#	""" SELECT ?o ?no 
#		WHERE {
#                     ?o a <http://xmlns.com/foaf/0.1/Organization>.
#		     ?o <http://xmlns.com/foaf/0.1/name> ?no.
#		}
#		GROUP BY ?no
#		ORDER BY DESC (?nxo)
#	""")
	

#Give me all the authors from organization BGS

for row in qres:
   #print("%s %s %s"  % row)
   print("%s"  % row)

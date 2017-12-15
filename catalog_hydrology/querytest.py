import rdflib
g = rdflib.Graph()

g.parse("rdf_output.ttl", format="n3")

# Give me all the respository
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
#qres = g.query(
#	""" SELECT ?l (COUNT(?recurso) AS ?nr)
#		WHERE {
#		     ?recurso a <http://www.w3.org/ns/dcat#Dataset>.
#		     ?recurso <http://purl.org/dc/terms/spatial> ?l.
#		}
#		GROUP BY ?recurso
#		HAVING(COUNT(?recurso) > 0) 
#	""")	

#Give the number of locations from the catalog
#qres = g.query(
#	""" SELECT (COUNT(?l) AS ?nl) 
#	WHERE {
#		     ?recurso a <http://www.w3.org/ns/dcat#Dataset>.
#		     ?recurso <http://purl.org/dc/terms/spatial> ?l.
#		}""")	
#Give the publisher with the most published resources
qres = g.query(
	""" SELECT ?p (COUNT(?r) AS ?nr) 
		WHERE {
		     ?r a <http://www.w3.org/ns/dcat#Dataset>.
		     ?r <http://purl.org/dc/terms/publisher> ?p.
		}
		GROUP BY ?p
		ORDER BY DESC (?nr)
		LIMIT 1
		""")	
		



for row in qres:
   print("%s %s" % row)

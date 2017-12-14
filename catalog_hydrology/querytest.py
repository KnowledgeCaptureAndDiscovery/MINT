import rdflib
g = rdflib.Graph()

g.parse("rdf_output.ttl", format="n3")

qres = g.query(
	""" SELECT DISTINCT ?a ?b ?c
	    WHERE {
		?a ?b ?c
	}""")

for row in qres:
	print("%s %s %s" % row)

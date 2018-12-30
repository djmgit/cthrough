from lambda_func import handler

import json

doc1 = {"name":"test1.txt", "content": "I love burgers. Burger king is good for burgers. Whopper is best"}
doc2 = {"name":"test2.txt", "content": "I love burgers too. Burger king is good but McDonalds is better. It has got lots of options"}
doc3 = {"name":"test3.txt", "content": "I do not like burgers. I love pizzas. Dominos pizzas are great. I just love them"}
doc4 = {"name":"test4.txt", "content": "I love cheese burst pizzas. Dominos and smokin joe are great pizza shops."}
doc5 = {"name":"test5.txt", "content": "I do not like fast food. I like to eat home made food more."}

def make_request(data):
	print (data.get("operation"))
	print (json.dumps(data, indent=4))
	print ('\n')
	response = handler(data, None)
	print (json.dumps(response, indent=4))

make_request({"operation": 'find_sim_between_two', 'doc1': doc1.get("content"), 'doc2': doc2.get("content")})
make_request({"operation": 'find_similar_docs', 'primary_doc': doc1, 'list_of_docs': [doc2, doc3, doc4, doc5]})
make_request({"operation": 'find_similarity_pairs', 'list_of_docs': [doc1, doc2, doc3, doc4, doc5]})
make_request({"operation": 'cluster_docs', 'list_of_docs': [doc1, doc2, doc3, doc4, doc5], 'threshold': 0.4})


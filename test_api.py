import requests
import json
import base64

doc1 = {"name":"test1.txt", "content": "I love burgers. Burger king is good for burgers. Whopper is best"}
doc2 = {"name":"test2.txt", "content": "I love burgers too. Burger king is good but McDonalds is better. It has got lots of options"}
doc3 = {"name":"test3.txt", "content": "I do not like burgers. I love pizzas. Dominos pizzas are great. I just love them"}
doc4 = {"name":"test4.txt", "content": "I love cheese burst pizzas. Dominos and smokin joe are great pizza shops."}
doc5 = {"name":"test5.txt", "content": "I do not like fast food. I like to eat home made food more."}

def make_request(url, data):
	print (url)
	#print (json.dumps(data, indent=4))
	print ('\n')
	response = requests.request("POST", url, json=data)
	print (response.status_code)
	print (json.dumps(response.json(), indent=4))

#make_request('https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-sim-between-two', {'doc1': doc1.get("content"), 'doc2': doc2.get("content")})
#make_request('https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-similar-docs', {'primary_doc': doc1, 'list_of_docs': [doc2, doc3, doc4, doc5], "threshold": 0.4})
#make_request('https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-similar-pairs', {'list_of_docs': [doc1, doc2, doc3, doc4, doc5]})
#make_request('https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/cluster-docs', {'list_of_docs': [doc1, doc2, doc3, doc4, doc5], 'threshold': 0.4})
doc6 = {"name": "test6.txt", "content": "A human loves skate boarding. I too have a skateboard at my house. I often use it in my garden while playing."}
doc7 = {"name": "test7.txt", "content": "i love burgers very much."}
with open('/home/deep/cthrough/skate.jpg', 'rb') as image1:
	img1 = base64.b64encode(image1.read()).decode()
with open('/home/deep/cthrough/basket.jpg', 'rb') as image2:
	img2 = base64.b64encode(image2.read()).decode()
with open('/home/deep/cthrough/skate.jpg', 'rb') as image3:
	img3 = base64.b64encode(image3.read()).decode()

img1 = {"name": "img1", "content": img1}
img2 = {"name": "img2", "content": img2}
img3 = {"name": "img3", "content": img3}

print (type(img1))
#make_request('https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-sim-between-two-images', {'img1': img1, 'img2': img2})
#make_request('https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-sim-between-image-text', {'img': img.get("content"), 'doc': doc6})
#make_request('https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-images-similar-to-doc', {'primary_doc': doc6, 'list_of_images': [img1, img2, img3], "threshold": 0.3})
#make_request('https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-docs-similar-to-image', {'primary_image': img1, 'list_of_docs': [doc6, doc7], "threshold": 0.3})
make_request('https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/cluster-images', {'list_of_images': [img1, img2, img3], "threshold": 0.3})

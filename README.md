## What is Ctrough API

Cthrough is a web based API to calculate similarity between text documents. It can find similarity (score between 0 to 1) between
any two given text documents. Also from a given group of text documents it can find documenst which are most similar (depending on
a customisable threshold) to a particular given document. Not only can it compare text document with text documen,it can also compare text with image and generate similairty between them. It can also be used to cluster images and texts. Find all the use cases of Cthrough in details below.

Cthrough also comes with a CLI tool : https://github.com/djmgit/cthrough_cli

### Technologies used
- Amazon Comprehend
- Amazon Rekognition
- AWS Lambda
- AWS API Gateway
- Boto3
- Python3

### What all can Cthrough do
- Determine Similarity between any two given document.
- Given a aprticular document, determine the documents (from a given list of documents) which are most similar to that document
- Among a list of documents, determine similarity score for every pair of document.
- Separate a list of documents into cluster depending on a customisable threshold.
- Determine similarity between two images
- Determine similarity between a image and a text document
- Given an image, from a list of documents, filter all those documents which are most similar to the given image
- Given a text document, from a list of images, filter all those images which are most similar to the given document
- Separate given images into clusters.

### How it works
Cthrough uses **Amazon Comprehend** to find out the entities and keywords resent in a given text document. In order to calculate
the similarity between two text documents, it first finds out a set of keywords + entities from both the text documents. Once
it has go the two lists of keywords, it calculates **Cosine** similarity between them. Cosine similairty is a method of determining similairity between two documents and is based on occurence of words and returns a value between **0 and 1**
In order to calculate similarity between images, it first extracts entities from the images using **Amazon Rekognition**. Once the
entities are extracted for both the image, then we again use cosine similarity to determine the similarity between both the images.
Same methodology is also used for determining similarity between images and texts.
The core functionalities are deployed as a lambda function which is exposed as a REST API via **Amazon API Gateway**

### API Usage
The API consists of various endpoints which are described below:

The base API endpoint us **https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging**

#### /find-sim-between-two
```
  POST /find-sim-between-two
  Request body:
  {
    "doc1" : 'content of document 1 as string'
    "doc2" : 'content of document 2 as string'
  }
  
  Response:
  {
    "status": "OK",
    "data": {
        "score": 0.6674238124719146
    }
}

```
**Example in python**
```
  import requests
  doc1 = "I love burgers. Burger king is good for burgers. Whopper is best"
  doc2 = "I love burgers too. Burger king is good but McDonalds is better. It has got lots of options"
  url = "https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-sim-between-two"
  data = {
    "doc1": doc1,
    "dco2": doc2
  }
  response = requests.request("POST", url, json=data)
  print (response.json())
  
```

### /find-similar-docs
This endpoint find docs (from a list of docs) which are most similar to a given doc depending on the given threshold.
**Threshold must be between 0 and 1**
```
POST /find-similar-docs
request body:
{
  "primary_doc:{
    "name": "name of the file",
    "content": "content of the file"
  },
  "list_of_docs":[
    {
      "name": "name of the file",
      "content": "content of the file"
    },
    {
      "name": "name of the file",
      "content": "content of the file"
    },
    .
    .
    .
    .
  ],
  "threshold": "Desired threshold between 0 and 1"
}
```
**Example in python**

```

import requests
doc1 = {"name":"test1.txt", "content": "I love burgers. Burger king is good for burgers. Whopper is best"}
doc2 = {"name":"test2.txt", "content": "I love burgers too. Burger king is good but McDonalds is better. It has got lots of options"}
doc3 = {"name":"test3.txt", "content": "I do not like burgers. I love pizzas. Dominos pizzas are great. I just love them"}
doc4 = {"name":"test4.txt", "content": "I love cheese burst pizzas. Dominos and smokin joe are great pizza shops."}

data = {
  "primary_doc": doc1,
  "list_of_docs": [
    doc2,
    doc3,
    doc4,
    doc5
  ],
  "threshold": 0.4
}

url = 'https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-similar-docs'

response = requests.request("POST", url, json=data)
print (response.json())

Response:
200
{
    "status": "OK",
    "data": [
        {
            "name": "test2.txt",
            "score": 0.6674238124719146
        }
    ]
}

```

### /find-similar-pairs
This endpoint finds the similarity score between every pair of documents in the given list

```
  POST /find-similar-pairs
  Request body:
  {"list_of_docs":[
    {
      "name": "name of the file",
      "content": "content of the file"
    },
    {
      "name": "name of the file",
      "content": "content of the file"
    },
    .
    .
    .
    .
    ]
  }
```
**Example in python**
```
import requests
  
doc1 = {"name":"test1.txt", "content": "I love burgers. Burger king is good for burgers. Whopper is best"}
doc2 = {"name":"test2.txt", "content": "I love burgers too. Burger king is good but McDonalds is better. It has got lots of options"}
doc3 = {"name":"test3.txt", "content": "I do not like burgers. I love pizzas. Dominos pizzas are great. I just love them"}
doc4 = {"name":"test4.txt", "content": "I love cheese burst pizzas. Dominos and smokin joe are great pizza shops."}
doc5 = {"name":"test5.txt", "content": "I do not like fast food. I like to eat home made food more."}

url = "https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-similar-pairs"
data = {
  "list_of_docs": [
      doc1,
      doc2,
      doc3,
      doc4,
      doc5
    ]
}

response = requests.request("POST", url, json=data)
print (response.json())

200
{
    "status": "OK",
    "data": [
        {
            "docs": [
                "test1.txt",
                "test2.txt"
            ],
            "score": 0.6674238124719146
        },
        {
            "docs": [
                "test1.txt",
                "test3.txt"
            ],
            "score": 0.30151134457776363
        },
        {
            "docs": [
                "test1.txt",
                "test4.txt"
            ],
            "score": 0.0
        },
        {
            "docs": [
                "test1.txt",
                "test5.txt"
            ],
            "score": 0.0
        },
        {
            "docs": [
                "test2.txt",
                "test3.txt"
            ],
            "score": 0.21081851067789195
        },
        {
            "docs": [
                "test2.txt",
                "test4.txt"
            ],
            "score": 0.0
        },
        {
            "docs": [
                "test2.txt",
                "test5.txt"
            ],
            "score": 0.0
        },
        {
            "docs": [
                "test3.txt",
                "test4.txt"
            ],
            "score": 0.6030226891555273
        },
        {
            "docs": [
                "test3.txt",
                "test5.txt"
            ],
            "score": 0.0
        },
        {
            "docs": [
                "test4.txt",
                "test5.txt"
            ],
            "score": 0.0
        }
    ]
}

```

### /cluster-docs
This endpint can be used to separae a given list of documents into clusters of similar documents. A threshold is required,
based on which the clustering is done.

```
POST /cluster-docs
Request body:
{
  "list_of_docs":[
    {
      "name": "name of the file",
      "content": "content of the file"
    },
    {
      "name": "name of the file",
      "content": "content of the file"
    },
    .
    .
    .
    .
  ],
  "threshold": "Desired threshold between 0 and 1"
}
```
**Example in python**
```

import requests
  
doc1 = {"name":"test1.txt", "content": "I love burgers. Burger king is good for burgers. Whopper is best"}
doc2 = {"name":"test2.txt", "content": "I love burgers too. Burger king is good but McDonalds is better. It has got lots of options"}
doc3 = {"name":"test3.txt", "content": "I do not like burgers. I love pizzas. Dominos pizzas are great. I just love them"}
doc4 = {"name":"test4.txt", "content": "I love cheese burst pizzas. Dominos and smokin joe are great pizza shops."}
doc5 = {"name":"test5.txt", "content": "I do not like fast food. I like to eat home made food more."}

url = "https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/cluster-docs"

data = {
  "list_of_docs": [
      doc1,
      doc2,
      doc3,
      doc4,
      doc5
    ],
    "threshold": 0.4
}

response = requests.request("POST", url, json=data)
print (response.json())

response:
200
{
    "status": "OK",
    "data": [
        [
            "test1.txt",
            "test2.txt"
        ],
        [
            "test3.txt",
            "test4.txt"
        ],
        [
            "test5.txt"
        ]
    ]
}

```
### /find-sim-between-two-images
This endpoint can be used to determine similarity between two images. It is to be notes that, images should be sent as
base64 encoded strings. Please follow the below given example to know how to make a request in python.

```
  POST /find-sim-between-two-images
  Request body:
  {
    "img1": "base64 encoded image string",/find-sim-between-two-images
    "img2": base64 encoded image string
  }
  
```
**Example in python**
```
import requests
import base64

with open('image1.jpg', 'rb') as image1:
	img1 = base64.b64encode(image1.read()).decode()
with open('image2.jpg', 'rb') as image2:
	img2 = base64.b64encode(image2.read()).decode()

data = {
  "img1": img1,
  "img2": img2
}

url = "https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-sim-between-two-images"
response = requests.request("POST", url, json=data)
print (response.json())

Response:

200
{
    "status": "OK",
    "data": {
        "score": 0.21773242158072692
    }
}

```
### /find-sim-between-image-text
This endpoint can be used to determine similarity between an image and a text document.

```
POST /find-sim-between-image-text
Request body:
{
    "img": "base64 encoded image string",
    "doc": "document content"
}
```

**Example in python**
```
import requests
import base64

with open('image1.jpg', 'rb') as image1:
	img1 = base64.b64encode(image1.read()).decode()
doc = "A human loves skate boarding. I too have a skateboard at my house. I often use it in my garden while playing."

data = {
  "img1": img1,
  "doc": doc
}

url = "https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-sim-between-image-text"
response = requests.request("POST", url, json=data)
print (response.json())

Reponse:
200
{
    "status": "OK",
    "data": {
        "score": 0.3794733192202055
    }
}

```
### /find-images-similar-to-doc
This endpoint can be used  to find images which are most similar to a given document. A threshold must be provided which will be
used to filter the images based on the similarity score which they obtain with the given text.

```
POST /find-images-similar-to-doc
Request body:
{
  "primary_doc:{
    "name": "name of the file",
    "content": "content of the file"
  },
  "list_of_images":[
    {
      "name": "name of the image",
      "content": "base64 encoded content of the image"
    },
    {
      "name": "name of the image",
      "content": "base64 encoded content of the image"
    },
    .
    .
    .
    .
  ],
  "threshold": "Desired threshold between 0 and 1"
}

```
**Example in python**
```
import requests
import base64

doc = {"name": "test6.txt", "content": "A human loves skate boarding. I too have a skateboard at my house. I often use it in my garden while playing."}

with open('image1.jpg', 'rb') as image1:
	img1 = base64.b64encode(image1.read()).decode()
with open('image2.jpg', 'rb') as image2:
	img2 = base64.b64encode(image2.read()).decode()
with open('image3.txt', 'rb') as image3:
	img3 = base64.b64encode(image3.read()).decode()
	
data = {
    "primary_doc": doc,
    "list_of_images": [
    	img1,
	img2,
	img3
    ],
    "threshold": 0.3
}

url = "https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-images-similar-to-doc"
response = requests.request("POST", url, json=data)
print (response.json())

Response

{
    "status": "OK",
    "data": [
        {
            "name": "img1",
            "score": 0.48989794855663565
        },
        {
            "name": "img3",
            "score": 0.48989794855663565
        }
    ]
}

```
### /find-docs-similar-to-image
This api can be used to ind the documents which are most similar to a given image. A threshold must be provided based on which
the images will be filtered.

```
POST /find-docs-similar-to-image
Request body:
{
  "primary_image:{
    "name": "name of the image",
    "content": "base64 encoded image string"
  },
  "list_of_docs":[
    {
      "name": "name of the doc",
      "content": "content of the doc"
    },
    {
      "name": "name of the doc",
      "content": "content of the doc"
    },
    .
    .
    .
    .
  ],
  "threshold": "Desired threshold between 0 and 1"
}

```
**Example in python**
```
import request
import base64

with open('image.png', 'rb') as image:
	img = base64.b64encode(image.read()).decode()
doc6 = {"name": "test6.txt", "content": "A human loves skate boarding. I too have a skateboard at my house. I often use it in my garden while playing."}
doc7 = {"name": "test7.txt", "content": "i love burgers very much."}

data = {
    "primary_image": img,
    "list_of_docs": [
        doc6,
	doc7
    ],
    "threshold": 0.3
}

url = "https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/find-docs-similar-to-image"
response = requests.request("POST", url, json=data)
print (response.json())

Reponse:
200
{
    "status": "OK",
    "data": [
        {
            "name": "test6.txt",
            "score": 0.48989794855663565
        }
    ]
}

```
### /cluster-images
This is endpoint can be used to separate images into cluster depending on the similary scores among them and the threshold
value provided.

```
POST /cluster-images
{
    "list_of_images":[
    {
      "name": "name of the image",
      "content": "base64 encoded content of the image"
    },
    {
      "name": "name of the image",
      "content": "base64 encoded content of the image"
    },
    .
    .
    .
    .
  ],
  "threshold": "Desired threshold between 0 and 1"
}

```
**Example in python**

```
import requests
import base64

with open('image1.jpg', 'rb') as image1:
	img1 = base64.b64encode(image1.read()).decode()
with open('image2.jpg', 'rb') as image2:
	img2 = base64.b64encode(image2.read()).decode()
with open('image3.jpg', 'rb') as image3:
	img3 = base64.b64encode(image3.read()).decode()
	
data = {
    "list_of_images": [
    	img1,
	img2,
	img3
    ],
    "threshold": 0.3
}

url = "https://nwqhr5fk8c.execute-api.us-east-1.amazonaws.com/staging/cluster-images"
response = requests.request("POST", url, json=data)
print (response.json())

Response:
200
{
    "status": "OK",
    "data": [
        [
            "img1",
            "img3"
        ],
        [
            "img2"
        ]
    ]
}

```

### Source code structure

- **knowledge_extractor.py**: Extracts entities and keywords from text using Amazon comprehend
- **imageinfo_extractor.py**: Extracts entities from image
- **simib.py**: Core module which implements cosine similarity using above two modules.
- **csim.py**: Uses simlib.py to implement features like determining similarity between texts and images and clustering.
- **lambda_func.py**: Lambda handler and handler functions for individual operations
- **main.py**: A test flask application for bare-metal deployment
- **update_lambda.py**: Update the deployed lambda function, do not forget to change function name.
- **insdep.sh**: Install dependencies after creating virtualenv
- **packdep.sh**: Package the entire app, create a bundle zip and deploy it to lambda.

### Cthrough CLI

Cthrough API can also be accessed over a python based CLI tool - https://github.com/djmgit/cthrough_cli





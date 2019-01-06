## What is Ctrough API

Cthrough is a web based API to calculate similarity between text documents. It can find similarity (score between 0 to 1) between
any two given text documents. Also from a given group of text documents it can find documenst which are most similar (depending on
a customisable threshold) to a particular given document. Not only can it compare text document with text documen,it can also compare text with image and generate similairty between them. It can also be used to cluster images and texts. Find all the use cases of Cthrough in details below.

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
```POST /find-sim-between-two
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



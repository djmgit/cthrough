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

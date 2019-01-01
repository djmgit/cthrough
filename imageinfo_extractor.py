import boto3
import json

class ImageInfoExtractor:
	def __init__(self, img=""):
		self.rekognition = boto3.client(service_name='rekognition')
		self.response = {}

		if img:
			self.img = img
			self.extract_imageinfo()

	def set_img(self, img):
		self.img = img

	def set_img_and_extract(self, img):
		self.img = img
		self.extract_imageinfo()

	def extract_labels(self):
		label_data = self.rekognition.detect_labels(Image={"Bytes": self.img})
		return label_data

	def extract_text(self):
		text_data = self.rekognition.detect_text(Image={"Bytes": self.img})
		return text_data

	def extract_imageinfo(self):
		self.response = {
			"label_data": self.extract_labels(),
			"text_data": self.extract_text()
		}

	def get_response(self):
		return self.response

if "__name__" == "__main__":
	imageFile = "/home/deep/cthrough/skate.jpg"

	with open(imageFile, 'rb') as image:
		imageinfo_extractor = ImageInfoExtractor(image)
		response = imageinfo_extractor.get_response()

	print (json.dumps(response, indent=4))

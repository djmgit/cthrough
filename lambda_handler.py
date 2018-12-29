'''
 This is the handler method for aws lambda
'''

import json
from csim import Csim
from util import *



def handler(event, context):
	operation = event.get("operation")

	if not is_valid_op(operation):
		return build_response("FAILED", "INVALID_OPERATION")

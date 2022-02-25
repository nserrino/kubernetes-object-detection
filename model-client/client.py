import pathlib
import numpy as np
import requests
import json
from PIL import Image
import tensorflow as tf

requests.packages.urllib3.disable_warnings()
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


test_image_path = pathlib.Path('../test-images/image1.jpg')

# Note that Tensorflow serving requires images sent in the same request to be the same dimensions.
images = []
image_np = np.array(Image.open(test_image_path))
images.append(image_np.tolist())  

data = json.dumps({"instances": images})

for i in range(100):
  headers = {"content-type": "application/json"}
  json_response = requests.post('http://localhost:8501/v1/models/object-detection:predict', data=data, headers=headers)

  print(f"Request {i}/100: received {len(json_response.text)} bytes from the server")
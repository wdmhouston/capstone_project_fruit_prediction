import unittest
from modules.model import model

model1 = model()
image_path = "/app/project/data/test/apple/Image_1.jpg"
print(model1.predict(image_path))


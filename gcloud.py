PROJECT_ID = '104366821765554226769' # @param {type:"string"}
LOCATION = 'us-west1 '  # @param {type:"string"}

import vertexai
from vertexai.vision_models import ImageTextModel, Image

vertexai.init(project=PROJECT_ID, location=LOCATION)
model = ImageTextModel.from_pretrained("imagetext@001")

source_image = Image.load_from_file(location='./static/uploads/TestPhoto.png')

captions = model.get_captions(
    image=source_image,
    # Optional:
    number_of_results=1,
    language="en",
)
print(captions[0])

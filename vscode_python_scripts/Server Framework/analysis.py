from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification
from transformers import AutoModelForImageClassification, AutoConfig, AutoImageProcessor
from transformers import pipeline


def analyze_image(image_file):
    # Load the image
    image = Image.open(image_file)
    # Get the image size
    width, height = image.size
    # Count the number of pixels
    num_pixels = width * height

    return {'num_pixels': num_pixels}

def melanoma(image_file):

    print('melanoma')

    processor = AutoImageProcessor.from_pretrained("Oppoizer/Output-prova_melanoma")
    model = AutoModelForImageClassification.from_pretrained("Oppoizer/Output-prova_melanoma")

    image = Image.open(image_file)
    inputs = processor(images=image, return_tensors="pt")

    outputs = model(**inputs)
    predictions = outputs.logits.argmax(dim=-1)

    message = "The image that the user uploaded is classified as: "
    class_label = "malignant" if predictions == 0 else "benign"

    result = message+class_label

    return {'result analysis': class_label}


def radio(image_file):

    classifier = pipeline(model="lxyuan/vit-xray-pneumonia-classification")
    result = classifier(image_file)[0]
    print(result)
    return result
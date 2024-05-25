from transformers import pipeline

classifier = pipeline(model="lxyuan/vit-xray-pneumonia-classification")

# image taken from https://www.news-medical.net/health/What-is-Viral-Pneumonia.aspx
result = classifier(r"C:\Users\User\OneDrive\Escritorio\Social Inovation\Server Framework\uploads\image.jpg")

print(result)
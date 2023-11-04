import openai

openai.api_key = "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"

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="512x512"
)
image_url = response['data'][0]['url']

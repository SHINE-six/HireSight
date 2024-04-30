import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

generation_config = {
    "max_output_tokens": 328,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

text1 = """# Formal and Appropriate Attire: 1/5 marks
# Evaluates: The candidate dress formally and appropriately for the interview context.
# Grooming and Tidiness: 1/5 marks
# Evaluates: The candidate attention to personal grooming and tidiness, reflects their professionalism.
# Make a executive summary and take a mark 1 to 5 base on the criterion. 
# Please only generate the mark of the Formal and "Appropriate Attire" and "Grooming and Tidiness" then one executive summary do not add any other information."""


with open("HireSight\\backend\\image.png", "rb") as image_file:
  encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

image1 = Part.from_data(data = base64.b64decode(encoded_image), mime_type="image/png")
model = GenerativeModel("gemini-1.5-pro-preview-0409")



def generate():
  vertexai.init(project="civic-surge-420016", location="asia-southeast1")
  model = GenerativeModel("gemini-1.5-pro-preview-0409")
  responses = model.generate_content(
      [image1, text1],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )
  response_str = ""
  for response in responses:
    # Extract the text from the response
    for candidate in response.candidates:
        for part in candidate.content.parts:
            response_str += part.text

    # Format the response string
  response_str = response_str.replace("#", "")
  response_str = response_str.replace("*", "")
  response_str = response_str.replace("Evaluation:\n", "")
  response_str = response_str.replace(" Grooming", "Grooming")
  response_str = response_str.replace(" Executive Summary:\n", "Executive Summary:")
  response_str = response_str.replace("/5", ".0")
  response_str = response_str.strip()
  print(response_str)


generate()



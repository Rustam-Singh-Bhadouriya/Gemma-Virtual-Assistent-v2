# To run this code you need to install the following dependencies:
# pip install google-genai
# generate response

from modules import *

with open("API.json") as Key:
    api = json.load(Key)

API_KEY = api['API']

def generate(promt, lang):
    client = genai.Client(
        api_key=API_KEY,
    )

    model = "gemini-2.5-flash" # You can edit it model at https://www.aistudio.google.com
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""You are a virtual voice assistent Gemma and response language={lang} and answer in enter language and explain your answer Prompt={promt}"""), # Giving promt
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        # print(chunk.text, end="")
        print(promt)
        return chunk.text

if __name__ == "__main__":
    generate()

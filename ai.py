

import google.generativeai as genai
import os


API_KEY="AIzaSyCAvW1p7MDq8Iqe7nd6YIvAOcRaMJH8-0Y";

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash');    
response = model.generate_content("you have to create a one sharyari based on food & you have to use language as a English")
print(response.text)

# change the response "according to your requment "
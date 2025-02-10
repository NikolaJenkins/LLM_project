# Ensure your VertexAI credentials are configured

from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatVertexAI(model="gemini-1.5-flash")
messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

response = model.invoke(messages)
print(response)

# import vertexai
# from vertexai.generative_models import GenerativeModel
#
# # TODO(developer): Update and un-comment below line
# PROJECT_ID = "inductive-arena-449800-u8"
# vertexai.init(project=PROJECT_ID, location="us-west1")
#
# model = GenerativeModel("gemini-1.5-flash-002")
#
# response = model.generate_content(
#     "What's a good name for a flower shop that specializes in selling bouquets of dried flowers?"
# )
#
# print(response.text)
# # Example response:
# # **Emphasizing the Dried Aspect:**
# # * Everlasting Blooms
# # * Dried & Delightful
# # * The Petal Preserve
# # ...

import openai
from openai import AzureOpenAI
import httpx

# Set your OpenAI API Key
httpx_client = httpx.Client(http2=True, verify=False)

OPENAI_API_KEY = ""
AZURE_ENDPOINT = ""
OPENAI_API_TYPE = "azure"
AZURE_CHAT_DEPLOYMENT = "gpt-4o"
OPENAI_API_VERSION = "2024-08-01-preview"
openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = AZURE_ENDPOINT
openai_client = AzureOpenAI(api_key=OPENAI_API_KEY,azure_endpoint=AZURE_ENDPOINT,azure_deployment=AZURE_CHAT_DEPLOYMENT,api_version=OPENAI_API_VERSION, http_client=httpx_client)



def query_gpt4(system_prompt, prompt):
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": system_prompt,
                    },
                    {
                        "type": "text",
                        "text": prompt,
                    }
                ],
            }
        ],
        max_tokens=3000,
        temperature=0.7
    )
    return response.choices[0].message.content

def read_persona_prompts(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        prompts = []
        current_prompt = ""
        for line in lines:
            current_prompt += line
        prompts.append(current_prompt)
        prompts = "".join(prompts)
    return prompts

def write_to_file(file_path, content):
    with open(file_path, "a") as file:
        file.write("\n\n"+content + "\n\n")

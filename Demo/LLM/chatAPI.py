from openai import OpenAI
from dotenv import load_dotenv
import os
import time
from tavily import TavilyClient

def get_response(userInput):
    load_dotenv()
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    tavily_key = os.getenv("TAVILYKEY_API_KEY")

    # client = OpenAI()
    tavily = TavilyClient(api_key=tavily_key)


    response = tavily.get_search_context(query=userInput,search_depth="advanced",max_tokens=16385)
    print(response)
    response = get_report(response)
    print(response)
    return response


def get_speech():
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input="Hello world! This is a streaming test. tell me something fun about NVIDIA",
    )
    
    storage_dir = "storage"
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)

    file_path = os.path.join(storage_dir, "output.mp3")

    # Save the response to the specified path
    response.stream_to_file(file_path)


def get_report(data):
    # Construct the system prompt
    system_prompt = f"""
    your are a Financial Analyst Expert, your name is Tavily Financial News Analyst Expert,
    you analysis company trending base on given data.
    If the data source has number, You need to emphasize it to the user.
    your data source is from here: {data}.
    you answer should include urls at end if data provided
    """
    client = OpenAI()
    # Make the API call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": system_prompt
        }],
        temperature=0.8,
        max_tokens=2000
    )
    response = response.choices[0].message.content

    response = response.strip()
    # Return the API response
    return response


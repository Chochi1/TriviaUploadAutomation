import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use the API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def create_youtube_description(hook, body):
    try:
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
              {
                  'role': 'system',
                  'content': 'I need your help in creating description for a YouTube short. I want you to keep the YouTube SEO in check while writing. Description should be optimized for the SEO purpose. Do not mention people or characters in description. In one sentence.'

              },
              {
                  'role': 'user',
                  'content': f"""Here's a general idea of what the short is about:

Hook: {hook}

Body: {body}

SEO description:"""
              }
          ],
          temperature=0.5,
          max_tokens=150
        )

        seo_popis = response['choices'][0]['message']['content'].strip()

        if not seo_popis:
            print("API empty response.")
            return None

        return seo_popis

    except Exception as e:
        print(f"Error: {e}")
        return None

def create_youtube_tags(hook, body):
    try:
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=[
              {
                  'role': 'system',
                  'content': 'I need your help in creating tags for a YouTube short. I want you to keep the YouTube SEO in check while writing them. Tags should be optimized for the SEO purpose. Make sure to separate each tag with a comma. Tags I need to put there for shure are: shorts, youtubeshorts, shortschannel, trivia, quiz'

              },
              {
                  'role': 'user',
                  'content': f"""Here's a general idea of what the short is about:

Hook: {hook}

Body: {body}

Tags:"""
              }
          ],
          temperature=0.5,
          max_tokens=300
        )

        tags = response['choices'][0]['message']['content'].strip()

        if not tags:
            print("API empty response.")
            return None

        return tags

    except Exception as e:
        print(f"Error: {e}")
        return None
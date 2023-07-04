# import openai 
import aiohttp
from settings import settings
# from constants import random_headers, proxy_reader
import time
from random import choice

class GPT:
    def __init__(self):
        pass
        # print(settings.API_KEY_CHAT_GPT)
        # print(settings.URL_CHAT_GPT)
        # proxy_list = proxy_reader()
        # self.curent_proxy = choice(proxy_list)

        # openai.api_key = settings.API_KEY_CHAT_GPT

    def refactor_conversation(self, conversation, total_tokens):
        # print('hello refactor conv')

        if total_tokens >= 3800:
            conversation = conversation[:2]
            return conversation
        
        if total_tokens >= 3000:
            # print('total_tokens >= 500')
            if len(conversation) >=6:
                try:
                    begining_conv = conversation[:4]
                except:
                    begining_conv = conversation[:2]

                try:
                    conversation = begining_conv + conversation[6:] 
                except:
                    conversation = begining_conv

            else:
                try:
                    begining_conv = conversation[:2]
                except:
                    begining_conv = []

                try:
                    conversation = begining_conv + conversation[4:] 
                except:
                    try:
                        conversation = begining_conv + conversation[3:]
                    except:
                        conversation = begining_conv
        return conversation

    async def send_data_chat_gpt(self, conversation, total_tokens):

        text_gpt = None
        try:
            conversation = self.refactor_conversation(conversation, total_tokens)
        except:
            pass
        # print(conversation)
        # print(len(conversation))
        # print('The query was sent')

        async with aiohttp.ClientSession() as session:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {settings.API_KEY_CHAT_GPT}"
            }
            data = {
                "model": "gpt-3.5-turbo",
                "messages": conversation,
                "temperature": 0.7,
                # "max_tokens": 150,
                # "top_p": 1,
                # "frequency_penalty": 0.0,
                # "presence_penalty": 0.6,
            }

            for _ in range(3):
                try:
                    async with session.post(
                        settings.URL_CHAT_GPT,
                        headers=headers,
                        json=data
                    ) as resp:
                        try:
                            response_data = await resp.json()  # Await the resp.json() coroutine
                            text_gpt = response_data['choices'][0]['message']['content'].strip()
                            # text_gpt = response_data.choices[0].message.content 
                            total_tokens = response_data["usage"]["total_tokens"]
                            break
                            # return None, total_tokens, conversation
                        except Exception as ex:
                            print(f"gpt_api___85___{ex}")
                            time.sleep(3)
                            continue
                  
                except Exception as ex:
                    print(f"gpt_api___88___{ex}")
                    time.sleep(3)
                    continue

        return text_gpt, total_tokens, conversation

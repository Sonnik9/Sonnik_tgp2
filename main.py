import os
import time
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from settings import settings
import gpt_api
from io import BytesIO
from utils import Converter

class TgApi:
    def __init__(self, api_token):  
        self.total_tokens = 0 
        self.audio_path = 'audio.mp3'
        self.basic_prompt = 'Инструкция: отвечай сообщениями не более 1000 символов. На эту инструкцию не отвечай. Вся наша переписка будет ниже.'
        self.conversation = [{'role': 'user', 'content': self.basic_prompt}]  
        # print(api_token)
        self.bot = Bot(token=api_token)
        self.dp = Dispatcher(self.bot)
        self.dp.register_message_handler(self.start_command, commands=['start'])
        self.dp.register_message_handler(self.handler_text, content_types=types.ContentType.TEXT)
        self.dp.register_message_handler(self.handler_voice, content_types=types.ContentType.VOICE)
        self.assist = gpt_api.GPT()
        self.file_bytes = BytesIO()
        self.converter_inst = Converter(self.file_bytes)

    def delete_audio_files(self):
        for file in os.listdir('.'):
            if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.ogg'):
                os.remove(file)

    async def start_command(self, message: types.Message):
        self.conversation = [{'role': 'user', 'content': self.basic_prompt}]  
        try:
            await message.reply("Привет! Chat GPT теперь в твоем телеграмме! Поговори с ним, не то ему скучно! Просто напиши что-либо или отправь голосовое сообщение!")
        except:
            await message.reply("Привет! Chat GPT теперь в твоем телеграмме! Поговори с ним, не то ему скучно! Просто напиши что-либо или отправь голосовое сообщение!")

    async def handler_text(self, message: types.Message) -> None:
        # print('hello text')
        response_text = False
        try:
            current_prompt = message.text
        except:
            pass
        try:
            response_text = await self.gpt_api_handler(current_prompt)
        except:
            pass
        if response_text:
            response_text = response_text 
        elif response_text == False:
            response_text = 'Ошибка соединения или проблемы с API'            
        else:
            response_text = 'Сообщение не должно быть длиннее 500 символов! Пожалуйста, повторите попытку!'
                
        for _ in range(9):
            try:
                await message.answer(response_text)
                break       
            except Exception as ex:            
                print(f"main_56str___{ex}")
                time.sleep(12)
                continue 

    async def handler_voice(self, message: types.Message) -> None:
        recog_text = None
        response_text = None
        flagConvertToAudio = False
        try:
            self.delete_audio_files()
        except:
            pass
        # print('hello voice') 

        try:
            file_id = message.voice.file_id
            file_info = await self.bot.get_file(file_id)
            file_path = file_info.file_path
        except:
            pass
        for _ in range(3):
            try:
                await self.bot.download_file_by_id(file_id, self.file_bytes)
                break
            except:
                continue
        try:
            recog_text = self.converter_inst.main_convertor_to_text()
        except:
            pass
        if recog_text:
            try:
                response_text = await self.gpt_api_handler(recog_text)
            except:
                pass
        else:
            response_text = f'Упс! Ошибки в распознавании речи или что-то другое.\n Пожалуйста, повторите попытку!'

        if response_text:
            pass
        elif response_text == False:
            response_text = 'Ошибка соединения или проблемы с API'            
        else:
            response_text = 'Сообщение не должно быть длиннее 1000 символов! Пожалуйста, повторите попытку!'
        try:
            flagConvertToAudio = self.converter_inst.convert_text_to_audio(response_text)
        except:
            pass

        if flagConvertToAudio:
            with open(self.audio_path, 'rb') as audio:
                for _ in range(9):
                    try:
                        await self.bot.send_voice(chat_id=message.chat.id, voice=audio)
                        break 
                    except:
                        time.sleep(12)
                        continue           
        else:
            try:
                response_text = 'Упс! Ошибка конвертации'
                await self.bot.send_message(message.chat.id, response_text)
            except:
                pass
        try:
            self.delete_audio_files(self)
        except:
            pass      

        for _ in range(9):
            try:
                await self.bot.send_message(message.chat.id, response_text)
                break       
            except Exception as ex:            
                print(f"main_56str___{ex}")
                time.sleep(12)
                continue 

    async def start_bot(self):
        await self.dp.start_polling()

    async def gpt_api_handler(self, current_prompt):
        response_text = None
        try:
            if len(current_prompt) >= 1000:
                return None
        except:
            pass
        try:   
            self.conversation.append({'role': 'user', 'content': current_prompt})
            # total_tokens_by_text = sum(len(item['content'].split()) for item in self.conversation)
            response_text, self.total_tokens, self.conversation = await self.assist.send_data_chat_gpt(self.conversation, self.total_tokens)
            # print(self.conversation)
            # print(f"token_count___{self.total_tokens}")
            # print(f"total_tokens_byText___{total_tokens_by_text}")
            self.conversation.append({'role': 'assistant', 'content': response_text})
        except:
            pass

        if response_text:
            # print(f"__102{True}")
            return response_text
        else:
            # print(f"__102{False}")
            return False

def main():
    api_token = settings.API_TOKEN
    tg_api = TgApi(api_token)
    executor.start_polling(tg_api.dp, skip_updates=True)

if __name__ == '__main__':
    main()









# import openai
# from settings import settings

# class GPT:
#     def __init__(self):
#         print(settings.API_KEY_CHAT_GPT)
#         openai.api_key = settings.API_KEY_CHAT_GPT

#     def send_data_chat_gpt(self, conversation, current_prompt):
#         response_text = ""

#         for _ in range(2):
#             try:
#                 prompt_pattern = self.construct_prompt(conversation, current_prompt)
#                 prompt = [{'role': 'user', 'content': prompt_pattern}]
#                 print(prompt)
                
#                 response = openai.ChatCompletion.create(
#                     model = "gpt-3.5-turbo",
#                     messages = prompt,
#                     temperature = 0.7,
#                     max_tokens = 3950,
#                     # logprobs=True
#                 )

#                 # response = openai.Completion.create(
#                 #     engine="davinci",
#                 #     prompt=prompt,
#                 #     temperature=0.7,
#                 #     max_tokens=3950,
#                 #     # logprobs=True
#                 # )
#                 # print(response)
#                 # response_text = response.choices[0].text 
#                 response_text = response.choices[0].message.content 
#                 total_tokens = response["usage"]["total_tokens"]
#                 if total_tokens >= 3950:
#                     try:
#                         conversation = conversation[3:]
#                     except:
#                         conversation = []
#                 break

#             except Exception as ex:
#                 print(f"OpenAI API error: {ex}")
#                 try:
#                     conversation = conversation[1000:]
#                 except:
#                     conversation = []
#                 continue

#         return response_text, total_tokens

#     def construct_prompt(self, conversation, current_prompt):
#         try:            
#             context = conversation
#         except:
#             context = ''
#         print(context)

#         prompt_pattern = f"1.(Это контекст моего текущего сообщения, держи это в уме и учти при ответе на содержание пункта '2':\n {context}\n\n2. (вопрос-обращение):\n {current_prompt}"
#         # prompt = {'role': 'user', 'content': f"{prompt_pattern}"}
#         return prompt_pattern 


# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from settings import settings
# from services import gpt_api

# # Set up logging
# logging.basicConfig(level=logging.INFO)

# conversation = []

# # Create a bot instance
# bot = Bot(token=settings.API_TOKEN)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)

# # Define a command handler for the '/start' command
# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.reply("Hello! I'm an your smart personal assistent. Please, ask me for something!")

# # # Define a message handler for all other messages
# # @dp.message_handler()
# # async def respond_message(message: types.Message):
# #     assist = gpt_api.GPT()
# #     response_text = assist.send_data_chat_gpt(message["text"])
# #     # response_text = "Okay, please continue..."
# #     await message.answer(response_text)

# # Define a message handler for all other messages
# @dp.message_handler()
# async def respond_message(message: types.Message):
#     print('hello')
#     assist = gpt_api.GPT()
#     # Add user message to conversation
#     conversation.append({'role': 'user', 'content': message["text"]})
#     print(message["text"])
#     # Truncate conversation if it exceeds 4000 tokens
#     # total_tokens = sum(len(msg['content'].split()) for msg in conversation)
#     total_tokens = sum(len(msg['content']) for msg in conversation)
#     if total_tokens >= 3900:
#         conversation = []
#         conversation.append({'role': 'user', 'content': message.text})

#     # Pass the conversation to GPT
#     response_text = assist.send_data_chat_gpt(conversation)

#     # Add assistant reply to conversation
#     conversation.append({'role': 'assistant', 'content': response_text})

#     await message.answer(response_text)


# # Start the bot
# async def start_bot():
#     await dp.start_polling()

# if __name__ == '__main__':
#     import asyncio
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(start_bot())





# import logging
# from aiogram import Bot, Dispatcher, types
# # from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.utils import executor
# from settings import settings
# from services import gpt_api
# Set up logging
# logging.basicConfig(level=logging.INFO)



# # import speech_recognition as sr
# # import os
# # from gtts import gTTS
# # from pydub import AudioSegment

# # class Converterr:

# #     def text_to_speech(text, filename):
# #         tts = gTTS(text=text, lang='ru-Ru')
# #         tts.save(filename)

# #     def speech_to_text(filename):
# #         audio = AudioSegment.from_file(filename, format="wav")
# #         recognizer = sr.Recognizer()
# #         with sr.AudioFile(filename) as source:
# #             audio_data = recognizer.record(source)
# #             text = recognizer.recognize_google(audio_data)
# #             return text

# # def handle_message(message):
# #     if message.content_type == 'text':
# #         # Respond with text
# #         response_text = 'You sent a text message: ' + message.text
# #         bot.send_message(chat_id, response_text)
# #     elif message.content_type == 'audio':
# #         # Respond with audio
# #         file_info = bot.get_file(message.voice.file_id)
# #         downloaded_file = bot.download_file(file_info.file_path)
# #         with open('voice_message.wav', 'wb') as new_file:
# #             new_file.write(downloaded_file)
# #         text = speech_to_text('voice_message.wav')
# #         response_text = 'You sent an audio message: ' + text
# #         bot.send_message(chat_id, response_text)
# #         response_audio = 'voice_response.mp3'
# #         text_to_speech(response_text, response_audio)
# #         with open(response_audio, 'rb') as audio_file:
# #             bot.send_audio(chat_id, audio_file)
# #         os.remove('voice_message.wav')
# #         os.remove('voice_response.mp3')


# import speech_recognition as sr
# import pyttsx3

# # Инициализация объектов для преобразования текста в речь и речи в текст
# engine = pyttsx3.init()
# recognizer = sr.Recognizer()

# # Функция для преобразования текста в аудио
# def text_to_speech(text):
#     engine.say(text)
#     engine.runAndWait()

# # Функция для преобразования аудио в текст
# def speech_to_text(audio_file):
#     with sr.AudioFile(audio_file) as source:
#         audio = recognizer.record(source)
#     text = recognizer.recognize_google(audio, language='ru')  # Используйте свой язык, если требуется другой
#     return text

# # Функция для обработки входящих сообщений
# def process_message(message):
#     if isinstance(message, str):
#         # Входящее сообщение является текстом
#         # Выполнить обработку текста и сформировать ответ
#         response = "Вы отправили текстовое сообщение: " + message
#         # Преобразовать ответ в аудио и воспроизвести его
#         text_to_speech(response)
#     elif isinstance(message, bytes):
#         # Входящее сообщение является аудио
#         # Преобразовать аудио в текст
#         text = speech_to_text(message)
#         # Выполнить обработку текста и сформировать ответ
#         response = "Вы отправили аудио сообщение. Распознанный текст: " + text
#         # Преобразовать ответ в аудио и воспроизвести его
#         text_to_speech(response)
#     else:
#         response = "Неизвестный формат сообщения"
#         # Преобразовать ответ в аудио и воспроизвести его
#         text_to_speech(response)

# # Примеры использования

# # Преобразование текста в аудио
# text_to_speech("Привет! Как могу помочь?")

# # Преобразование аудио в текст
# audio_file = "audio_message.wav"
# # Обработка аудио и формирование ответа
# response = process_message(audio_file)

# # Преобразование текста в аудио
# text_to_speech(response)


# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
# from settings import settings
# from services import gpt_api

# class TgApi:
#     def __init__(self, api_token):
#         self.conversation = []
#         self.bot = Bot(token=api_token)
#         self.dp = Dispatcher(self.bot)
#         self.dp.register_message_handler(self.start_command, commands=['start'])
#         self.dp.register_message_handler(self.respond_message)

#     async def start_command(self, message: types.Message):
#         await message.reply("Hello! I'm your smart personal assistant. Please, ask me for something!")

#     async def respond_message(self, message: types.Message):
#         print('hello')
#         assist = gpt_api.GPT()
#         current_prompt = message.text
#         self.conversation.append({'role': 'user', 'content': current_prompt})
#         # print(current_prompt)
#         total_tokens_by_text = sum(len(item['content'].split()) for item in self.conversation)
#         response_text, token_count = assist.send_data_chat_gpt(self.conversation)
#         print(f"token_count___{token_count}")
#         print(f"total_tokens_byText___{total_tokens_by_text}")
#         self.conversation.append({'role': 'assistant', 'content': response_text})

#         await message.answer(response_text)

#     async def start_bot(self):
#         await self.dp.start_polling()

# def main():
#     api_token = settings.API_TOKEN
#     tg_api = TgApi(api_token)
#     executor.start_polling(tg_api.dp, skip_updates=True)

# if __name__ == '__main__':
#     main()


# import aiogram
# from aiogram import types
# import io
# import speech_recognition as sr

# # Инициализация бота



# import speech_recognition as sr

# def audio_to_text(audio_path):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_path) as source:
#         audio_data = recognizer.record(source)
#         text = recognizer.recognize_google(audio_data)
#         return text

# # Пример использования
# audio_path = "audio.wav"  # Путь к аудиофайлу
# recognized_text = audio_to_text(audio_path)
# print(recognized_te 

# import telebot
# import speech_recognition as sr
# import os
# os.environ["PATH"] += os.pathsep + "/usr/bin/ffmpeg"

# # Устанавливаем токен вашего Telegram бота
# bot_token = '6055997213:AAEMmTkns4BjjSFbMUhPkYwtPulWYHysgxo'
# bot = telebot.TeleBot(bot_token)

# @bot.message_handler(content_types=['voice'])
# def handle_voice_message(message):
#     # Получаем информацию о голосовом сообщении
#     file_id = message.voice.file_id
#     file_info = bot.get_file(file_id)
#     file_path = file_info.file_path

#     # Скачиваем голосовое сообщение
#     file = bot.download_file(file_path)
#     audio_path_ogg = 'audio.ogg'  # Путь для сохранения аудиофайла OGG
#     audio_path_wav = 'audio.wav'  # Путь для сохранения аудиофайла WAV
#     with open(audio_path_ogg, 'wb') as audio_file:
#         audio_file.write(file)

#     # Конвертируем OGG в WAV
#     convert_to_wav(audio_path_ogg, audio_path_wav)

#     # Преобразуем аудио в текст
#     recognized_text = audio_to_text(audio_path_wav)

#     # Отправляем текстовый ответ
#     bot.send_message(message.chat.id, recognized_text)

# def convert_to_wav(ogg_path, wav_path):
#     os.system(f'ffmpeg -i {ogg_path} -acodec pcm_s16le -ar 16000 {wav_path}')

# def audio_to_text(audio_path):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_path) as source:
#         audio = recognizer.record(source)
#     recognized_text = recognizer.recognize_google(audio, language='ru-RU')
#     return recognized_text


# bot.polling()


    # def pol_breda(self, conversation):
    #     list_full_conv = conversation[-1]['content'].split('.')
    #     len_half_conv = int(len(list_full_conv)/5)
    #     polovina_conversation = list_full_conv[:len_half_conv]
    #     polBreda = ''.join(polovina_conversation)
    #     conversation = [{'role': 'user', 'content': polBreda}]  
    #     return conversation

# import os
# os.environ["PATH"] += os.pathsep + "/usr/bin/ffmpeg"
# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# import speech_recognition as sr
# from io import BytesIO
# import subprocess
# import logging
# from utils import Converter

# # logging.disable(logging.CRITICAL)

# bot_token = '6055997213:AAEMmTkns4BjjSFbMUhPkYwtPulWYHysgxo'
# bot = Bot(token=bot_token)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)

# @dp.message_handler(content_types=types.ContentType.VOICE)
# async def handle_voice_message(message: types.Message):
#     file_bytes = BytesIO()
    

#     file_id = message.voice.file_id
#     file_info = await bot.get_file(file_id)
#     file_path = file_info.file_path


#     await bot.download_file_by_id(file_id, file_bytes)
#     converter = Converter(file_bytes)
#     recognized_text = converter.main_convertor_to_text()
#     print(recognized_text)



#     # with open(audio_path_ogg, 'wb') as audio_file:
#     #     audio_file.write(file_bytes.getvalue())

#     # # Конвертируем OGG в WAV
#     # convert_to_wav(audio_path_ogg, audio_path_wav)

#     # # Преобразуем аудио в текст
#     # recognized_text = audio_to_text(audio_path_wav)

#     # Отправляем текстовый ответ
#     await bot.send_message(message.chat.id, recognized_text)


# # def convert_to_wav(ogg_path, wav_path):
# #     os.system(f'ffmpeg -i {ogg_path} -acodec pcm_s16le -ar 16000 {wav_path}')
# # def convert_to_wav(ogg_path, wav_path):
# #     # subprocess.run(['ffmpeg', '-loglevel', 'panic', '-i', ogg_path, '-acodec', 'pcm_s16le', '-ar', '16000', wav_path])

# #     subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'panic', '-i', ogg_path, '-acodec', 'pcm_s16le', '-ar', '16000', wav_path])
# # def audio_to_text(audio_path):
    
# #     recognizer = sr.Recognizer()
# #     # recognizer.logger.disabled = True
# #     with sr.AudioFile(audio_path) as source:
# #         audio = recognizer.record(source)
# #     recognized_text = recognizer.recognize_google(audio, language='ru-RU')
# #     return recognized_text

# if __name__ == '__main__':
#     # Запускаем бота
#     executor.start_polling(dp)

# import os
# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
# import gtts
# from gtts import gTTS

# # Установка токена бота
# bot_token = '6055997213:AAEMmTkns4BjjSFbMUhPkYwtPulWYHysgxo'

# # Создание объектов бота и диспетчера
# bot = Bot(token=bot_token)
# dp = Dispatcher(bot)

# @dp.message_handler(content_types=types.ContentType.TEXT)
# async def handle_text_message(message: types.Message):
#     # Получение текстового сообщения
#     text = message.text

#     # Конвертирование текста в аудио
#     tts = gTTS(text=text, lang='ru')
#     audio_path = 'audio.mp3'
#     tts.save(audio_path)

#     # Отправка голосового сообщения
#     with open(audio_path, 'rb') as audio:
#         await bot.send_voice(chat_id=message.chat.id, voice=audio)

#     # Удаление временного аудиофайла
#     os.remove(audio_path)

# if __name__ == '__main__':
#     # Запуск бота
#     executor.start_polling(dp, skip_updates=True)

# API_KEY_CHAT_GPT = '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'
# API_KEY_CHAT_GPT = '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'
# API_KEY_CHAT_GPT = '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'
# API_KEY_CHAT_GPT = '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'
# API_KEY_CHAT_GPT = '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'
# URL_CHAT_GPT = 'https://api.openai.com/vl/completions'

# API_KEY_CHAT_GPT = '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'
# API_KEY_CHAT_GPT = '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'


    # def send_data_chat_gpt(self, conversation, total_tokens):
    #     text_gpt = None
    #     conversation = self.refactor_conversation(conversation, total_tokens)
    #     print(conversation)
    #     print(len(conversation))
    #     print('The query was sent')
    #     # print(HEADERS)
    #     for _ in range(3):
    #         HEADERS = random_headers()
    #         proxy_item = {       
    #             "https": f"http://{self.curent_proxy}"          
    #         }
    #         print(proxy_item)
    #         try:
    #             answer = openai.ChatCompletion.create(
    #                 model="gpt-3.5-turbo",
    #                 messages=conversation,
    #                 temperature=0.7,
    #                 headers=HEADERS,
    #                 # proxies = proxy_item
                  
    #             )
    #             text_gpt = answer.choices[0].message.content 
    #             total_tokens = answer["usage"]["total_tokens"]
    #             return text_gpt, total_tokens, conversation
    #         except Exception as ex:
    #             print(f"28_gpt_api{ex}")
    #             time.sleep(4)
    #             continue
    #return text_gpt, total_tokens, conversation

# sudo apt install ffmpeg
# 






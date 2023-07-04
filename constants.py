# from fake_useragent import UserAgent 
# from random import choice

# uagent = UserAgent()
# def random_headers():
#     HEADERS = {
#         'authority': 'openaiapi-site.azureedge.net',
#         'accept': '*/*',
#         'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
#         'origin': 'https://platform.openai.com',
#         'referer': 'https://platform.openai.com/',
#         # 'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#         # 'sec-ch-ua-mobile': '?0',
#         # 'sec-ch-ua-platform': '"Linux"',
#         'sec-fetch-dest': 'manifest',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'cross-site',
#         # 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#         'user-agent': uagent.random
#     } 

#     return HEADERS 

# def proxy_reader():
#     with open("proxy_gpt.txt", encoding="utf-8") as f1:    
#         prLi = ''.join(f1.readlines()).split('\n')
#         prLi= list(i.strip() for i in prLi)
#         prLi = list(filter(lambda item: item != '', prLi))
#     return prLi
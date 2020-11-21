functions = []
def obertka(func):
	...
	
	def new_func(message = None):
		
		if message is None:
			message = input()
			
		
		
		result = func(message)
		if result:
		
					print(result)
		
		
		return result
	...
	print("в конце оборачивания")
	functions.append(new_func)
	return new_func

@obertka
def author_name(message):
	if 'author' in message:
		return 'Sasha'
import os
mind = [("author","Sasha"),
		("hotel","trivago"),
		("cat","MEWO"),
		("naruto","SASUKE"),
		("sasuke","NARUTO"),

		]
for memory in mind:
	q, a = memory
	@obertka
	def author_name(message,q=q,a=a):
			if q in message:
					return a






import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
key = "5c3749b03e8c7eefd5937cc089112e75b59ff20de1583c446341f98c7b21ab858767557f8f0b01ba48434"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message):
                from random import randint
                vk.method('messages.send',
                          {'user_id': user_id,
                           "random_id":randint(1,1000) ,
                           'message': message,}
                          )

# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            for func in functions:
              if func(text):
                 send_message(user_id, func(text))
            

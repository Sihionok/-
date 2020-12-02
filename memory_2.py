import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
key = "c4cf0a0661e38f87149ffdb72f81e97ef81fd4fec7c597d196bdc4e9a10291e328b0ea49cbd92693bd805"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message, file_vk_url = None, keyboard = None):
                from random import randint
                vk.method('messages.send',
                          {'user_id': user_id,
                           "random_id":randint(1,1000) ,
                           'message': message,
                           'attachment':file_vk_url,
                           'keyboard':keyboard}
                          )
users = {} #       kryakrya

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
            if user_id in users:
                number = int(text)
                true_number = users[user_id][0]
                if number > true_number:
                    send_message(user_id,"mnoga")
                elif number < true_number:
                    send_message(user_id,"malo")
                else:
                    send_message(user_id,"угадал")
                    del users[user_id]
                
            else:
                from random import randint
                send_message(user_id,"игра началась, угадывай число")
                users[user_id] = (randint(1,10),10)

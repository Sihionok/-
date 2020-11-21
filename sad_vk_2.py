import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
key = "06f326d53bc6280e4cef98eb69e8b04a69688446cb638cf9dc208f138e03f829485f4bad35bfba226626c"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message):
                from random import randint
                vk.method('messages.send',
                          {'user_id': user_id,
                           "random_id":randint(1,1000) ,
                           'message': message,}
                          )
WHAT = """what?
supported commands:
привет
как жизнь?
игруха
го
    """

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
            print(text)

            if text == 'привет':
                send_message(user_id, 'привет')
            elif "кот" in text:
                send_message(user_id, 'мяу')
            else:
                send_message(user_id, WHAT)

            if text == 'как жизнь?':
                 send_message(user_id, 'привет,эт к создателю,но у меня норм')
            elif "го" in text:
                send_message(user_id, 'уже отправил повелителю :)')
            
            if text == 'как дела?':
              send_message(user_id, 'номана!!))')
            if text == 'как дела? как дела? ':
              send_message(user_id, 'это новый КАДИДАК!!!')
              
            

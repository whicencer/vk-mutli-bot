import vk_api
import json
import os
import time
import webbrowser


def captcha_handle(captcha):
	key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
	return captcha.try_again(key)

if(open('token.txt', 'r').read()):
	access_token = open('token.txt', 'r').read()
else:
	webbrowser.open('https://oauth.vk.com/authorize?client_id=6121396&scope=476037087&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token', new=2)
	access_token = input('Введите токен полученный по ссылке или введите существующий: ')
	open('token.txt', 'w').write(access_token)
vk_session = vk_api.VkApi(captcha_handler=captcha_handle, token=access_token)
VK = vk_session.get_api()

def send_message():
	ids = input('Введите id пользовател(я/ей):\nПример: 523606182, 130468932\n  >>> ').split(', ')
	text = input('Введите текст сообщения: ')
	os.system('cls')
	for user_id in ids:
		try:
			VK.messages.send(user_id=user_id, message=text, random_id=0)
			print('Сообщение было доставлено!')
		except:
			print('Some Error')
		time.sleep(3)

def get_profile_info():
	os.system('cls')
	response = VK.account.getProfileInfo()
	print(f"Имя: {response['first_name']}\nID: {response['id']}\nФамилия: {response['last_name']}\nСтатус: {response['status']}\nДень рождения: {response['bdate']}\nНомер телефона: {response['phone']}")

def add_like():
	obj_type = input('Введите тип объекта\nПример:\n post - запись на стене группы/пользователя;\n comment - комментарий к записи на стене;\n photo — фотография;\n audio — аудиозапись;\n video — видеозапись;\n note — заметка;\n market — товар;\n photo_comment — комментарий к фотографии;\n video_comment — комментарий к видеозаписи;\n topic_comment — комментарий в обсуждении;\n market_comment — комментарий к товару;\n\n>>> ')
	owner_id = int(input('#####\nПРИМЕЧАНИЕ: ЕСЛИ ВЫ ХОТИТЕ ПОСТАВИТЬ ЛАЙК СООБЩЕСТВУ - ВВОДИТЕ ID ВЛАДЕЛЬЦА СЛЕДУЮЩИМ ОБРАЗОМ: "-<GROUP_ID>"\nДЛЯ ПОЛЬЗОВАТЕЛЯ - "<ACCOUNT_ID>"\n#####\nВведите id владельца поста\nПример: 182308066\n>>> '))
	ids = input('Введите id объект(а/ов):\nПример: 682082\n>>> ').split(', ')
	os.system('cls')
	for item_id in ids:
		item_id = int(item_id)
		try:
			VK.likes.add(type=obj_type, item_id=item_id, owner_id=owner_id)
			print(f'Лайк на объект {item_id} был поставлен!')
		except:
			print('Some Error')
		time.sleep(3)

def add_post():
	owner_id = input('#####\nПРИМЕЧАНИЕ: ЕСЛИ ВЫ ХОТИТЕ ДОБАВИТЬ ПОСТ - ВВОДИТЕ ID СООБЩЕСТВА СЛЕДУЮЩИМ ОБРАЗОМ: "-<GROUP_ID>"\nДЛЯ ПОЛЬЗОВАТЕЛЯ - "<ACCOUNT_ID>"\n#####\nВведите id пользователя или сообщества, на стене которого должна быть опубликована запись.\nНапример: 316634413\n>>> ')
	text = input('Введите текст сообщения(поста)\n>>> ')
	request_count = input('Введите количество запросов(max: 100): ')
	os.system('cls')
	if(int(request_count)>100):
		print('Вы ввели больше 100 запросов')
	else:
		request_count = int(request_count)
		while request_count > 0:
			owner_id = int(owner_id)
			try:
				VK.wall.post(owner_id=owner_id, message=text)
				owner_id = str(owner_id).replace('-', '')
				print(f'Пост на стену https://vk.com/public{owner_id} добавлен!')
			except vk_api.exceptions.ApiError as ApiError:
				print(ApiError)
			request_count = request_count-1
			time.sleep(5)
		
def board_create_comment():
	group_id = int(input('Введите идентификатор сообщества, в котором находится обсуждение: '))
	topic_id = int(input('Введите идентификатор темы, в которой необходимо оставить комментарий: '))
	message = input('Введите текст комментария: ')
	request_count = int(input('Введите количество запросов(max: 100): '))
	os.system('cls')

	if(request_count>100):
		print('Вы ввели больше 100 запросов')
	else:
		while request_count > 0:
			try:
				VK.board.createComment(group_id=group_id, topic_id=topic_id, message=message)
				print('Комментарий добавлен!')
			except vk_api.exceptions.ApiError as ApiError:
				print(ApiError)
			request_count = request_count-1
			time.sleep(5)

def wall_create_comment():
	owner_id = int(input('#####\nПРИМЕЧАНИЕ: ЕСЛИ ВЫ ХОТИТЕ ДОБАВИТЬ КОММЕНТАРИЙ - ВВОДИТЕ ID СООБЩЕСТВА СЛЕДУЮЩИМ ОБРАЗОМ: "-<GROUP_ID>"\nДЛЯ ПОЛЬЗОВАТЕЛЯ - "<ACCOUNT_ID>"\n#####\nВведите id пользователя или сообщества, на стене которого размещена запись.\nНапример: 316634413\n>>> '))
	post_id = int(input('Введите идентификатор записи на стене: '))
	message = input('Введите текст комментария: ')
	request_count = int(input('Введите количество запросов(max: 100): '))
	os.system('cls')

	if(request_count>100):
		print('Вы ввели больше 100 запросов')
	else:
		while request_count > 0:
			try:
				VK.wall.createComment(owner_id=owner_id, post_id=post_id, message=message)
				print('Комментарий добавлен!')
			except vk_api.exceptions.ApiError as ApiError:
				print(ApiError)
			request_count = request_count-1
			time.sleep(5)

def send_friend():
	ids = input('Введите id пользовател(я/ей):\nПример: 523606182, 130468932\n  >>> ').split(', ')
	text = input('Введите текст сопроводительного сообщения: ')
	os.system('cls')
	for user_id in ids:
		try:
			VK.account.getProfileInfo(user_id=user_id, text=text)
			print('Заявка в друзья была отправлена!')
		except:
			print('Some Error')
		time.sleep(3)

def select_method():
	method = input(f'''Выберите метод:\n
[0] - Отправка сообщений\n
[1] - Отправить заявку в друзья\n
[2] - Информация о профиле\n
[3] - Поставить отметку "Нравится"\n
[4] - Создать запись на стене\n
[5] - Добавить комментарий в обсуждении сообщества\n
[6] - Добавить комментарий к записи на стене\n
>>> ''')
	
	if(method == '0'):
		send_message()
	elif(method == '1'):
		send_friend()
	elif(method == '2'):
		get_profile_info()
	elif(method == '3'):
		add_like()
	elif(method == '4'):
		add_post()
	elif(method == '5'):
		board_create_comment()
	elif(method == '6'):
		wall_create_comment()
	else:
		print('Такого метода не существует!')

select_method()

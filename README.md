# auto_generate_promo
Авто генерация промо-кодов для PW.

Перед началом работы проверьте, что у вас есть установленный Python (https://www.python.org/downloads/).

Откройте проект в ide. Я использовал Pycharm (https://www.jetbrains.com/ru-ru/pycharm/).

#Настройка файла userdata.py
В этом файле хранятся данные вашего аккаунта: логин, пароль, число промокодов для генерации.
Вставьте ваш логин и пароль от личного кабинета (https://funline.pw/lk/)

#Возможная ошибка с версией chromebrowser.exe
Прикреплённый chromebrowser.exe 95 версии.
Если при запуске main вы увидели ошибку вроде:
SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version ваша_версия.
То не пугайтеся, вам просто надо заменить chromebrowser.exe на вашей версии.
Для этого перейдите (https://chromedriver.chromium.org/downloads) и скачайте вашей_версии и поместите в корень где он раньше был (auto_generate_promo/).

Будут ошибки по типу используйте find_element() заместо других селекторов - они не критичны.

По окончанию ввода промокодов программа сообщит количество успешных введённых промокодов или вы можете посмотреть их в своём лк.

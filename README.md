# auto_generate_promo
Авто генерация промо-кодов для PW.

Перед началом работы проверьте, что у вас есть установленный [Python](https://www.python.org/downloads/).

Откройте проект в ide. Я использовал [Pycharm](https://www.jetbrains.com/ru-ru/pycharm/).

## Настройка файла userdata.py
В этом файле хранятся данные вашего аккаунта: **логин, пароль, число промокодов** для генерации.
Вставьте ваш логин и пароль от личного кабинета [Личный кабинет](https://funline.pw/lk/)

## Возможная ошибка с версией chromebrowser.exe
Прикреплённый chromebrowser.exe **95** версии.
Если при запуске __main__ вы увидели ошибку вроде:
__SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version ваша_версия__.
То не пугайтеся, вам просто надо заменить chromebrowser.exe на вашей версии.
Для этого перейдите [скачать werdriver](https://chromedriver.chromium.org/downloads) вашей_версии и поместите в корень где он раньше был __auto_generate_promo/__

Будут ошибки по типу используйте __find_element()__ заместо других селекторов - они не критичны.

По окончанию ввода промокодов программа сообщит количество успешных введённых промокодов или вы можете посмотреть их в своём [лк](https://funline.pw/lk/).

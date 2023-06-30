## Secret Santa Telegram Bot
### Описание

* Бот для игры в Тайного Санту

### Реализованные Возможности

1. #### Создание персональных комнат

- Каждый желающий может создать комнату для неограниченного количества людей.
    - При создании нужно указать:
      - **Имя комнаты**
      - **Бюджет для своей компании игроков**
      - **Свои желания**

2. #### Вход в существующую комнату по ID комнаты
3. #### Управление своим профилем
   - Бот позволяет внести и изменить такие данные как:
     - **Имя и Фамилия**
     - **Домашний Адрес**
     - **Номер Телефона**
   - Разрешено полное удаление внесенных данных
 
4. #### Управление комнатами
   - Меню управления комнатами для обычного пользователя:       
     - **Выйти из комнаты**
     - **Изменить пожелания**
   - Меню управления комнатами для владельца:
     - **Начать игру** - позволяет установить время рассылки
     - **Изменить пожелания**
     - **Настройки**
       - **Удалить комнату** 
       - **Изменить имя комнаты**
       - **Изменить владельца**
     
     ```Администратор комнаты не может выйти из нее, пока не передаст управление другому. Комната может быть только окончательно удалена.```
5. #### Коммуникация
После разыгрывания ролей в игре, в комнатах доступны 2 опции
   - **Отправка сообщения Тайному Санте**
   - **Отправка сообщения получателю**

Позволяющие коммуницировать анонимно между получателем и отправителем посредством бота.
6. - Реализована простая Веб Админка.

7. ### Не реализовано
   1. Требуется ревью информационных сообщений бота.
   2. Перенос всех ответов бота в БД.
   3. Покрытие тестами     

8. ### В планах
   3. Расширить функционал веб панели. 
   4. Упаковать проект в Doker контейнеры
  
### Стек
1. Aiogram 2
2. FastAPI
3. Jinja2
4. Tortoise ORM
5. Aerich
6. PostgreSQL
7. Redis

### Запуск Бота:
 - Установить PostgreSQL и Redis, сконфигурировать и создать БД. 
 - Redis требует включения доступа по паролю:
    ```
   sudo nano /etc/redis/redis.conf
   # requirepass foobared
   ```
 - Создать свой .env файл по шаблону .env.example
 - pip install -r requirements
 - aerich migrate
 - aerich upgrade
 - python app.py


- ### Регистрация вебхука
    Используем линк в браузере
    https://api.telegram.org/bot{telegram_token}/setWebhook?url=https://{domain_name}/bot/

    Пример:
    https://api.telegram.org/bot5473814321:AAEFDZ1A5SoRsd6RFDONysEbYkl3D_VAfss/setWebhook?url=https://e87d-5-76-101-111.ngrok-free.app/bot/


- Так же, для работы **Telegram Login Widget**, требуется зарегистрировать домен вашего сайта в **@BotFather** используя команду **/setdomain**
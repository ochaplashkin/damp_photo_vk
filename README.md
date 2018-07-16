# Скачивание всех фото из диалога

Простой скрипт, написанный на Python 3.7.10 с использованием VK API, который позволяет сгрузить все фотографии с  необходимого диалога.

## Подготовка и авторизация

Из-за высокой системы безопасности сервиса Вконтакте,  необходимо получить ***token*** и ***id*** диалога.

#### Авторизация приложения и получение токена:


- Переходим на [страницу ](https://vk.com/dev "Вконтакте для разработчиков") сервиса Вконтакте для разработчиков
- Выбираем вкладку Мои приложения и создаём приложение, без изменений параметров
- Подтверждаем действия с помощью мобильной версии или номера телефона
- Переходим во вкладку Настройки и сохраняем(например, в блокноте) ID приложения
- Переходим на страницу по URL:
```
https://oauth.vk.com/authorizeclient_id=ХХХХХХХ&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=messages&response_type=token
```

где **ХХХХХХХ** это ID вашего приложения

- После перехода, подтверждаем, что наше приложение получит доступ к данным и получаем успешное выполнение операции в виде URL, который содержит необходимое значение токена:

```https://oauth.vk.com/blank.html#access_token=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&expires_in=86400&user_id=1963743
```


#### Получение ID диалога:


- Необходимо зайти в нужный диалог
- URL будет содержать необходимое значение:
<https://vk.com/im?sel=ХХХХХХХХ>

где число из 8 цифр это и есть **id** диалога



## Установка и запуск

- Скачайте данный репозиторий либо через веб-интерфейс, либо командой:
    ```
    git clone git@github.com:ochaplashkin/damp_photo_vk.git
    ```
- Установите необходимые пакеты:
    ```
    pip3 install -r requirements.txt
    ```
- Запустите скрипт командой:
    ```
    python3 main.py your_token your_id_dialog [name_folder]
    ```
    name_folder - необязательный параметр, который задаёт имя папки для фотографий. По умолчанию - photos

## Безопасность вашего аккаунта

После использования, настоятельно рекомендуется:
- Сбросить настройки безопасности
- Изменить пароль к аккаунту
- Удалить созданное приложение

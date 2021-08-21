# Django back 

## api

* [ ] GET: http://host/bloggers/ - получение списка блогеров
```json5
{
  "bloggers": [
    {
      "id": 12345,
      "name": "Ivanov Ivan",
      "email": "some@email.com",
      "avatar": "media/avatars/...", // "" if there is no avatar
      "gender": 'm'|'w',
      "last_date_invitation": 19932451325,  
      // думаю, если блогер уже в туре - присылать его не будем
      // также не будем его показывать, если он уже был приглашён в этом месяце
      "social_networks": {
        "facebook": "link",
        "instagram": "link",
        // ... There will be more fields in the future
      }
      
    },
    // ...
  ]
}  
```
  

* [ ] DELETE: http://host/bloggers/{blogger_id}/ - удаление блогера из поиска полностью
* [ ] PUT: http://host/groups/{group_id}/bloggers/{blogger_id}/ - добавление блогера в группу
* [ ] POST: http://host/groups/{group_id}/send_invitation/ - отправка письма группе блогеров 
```json5
{
  "title": "some text",
  "body": "some text",
  "recipients": [123, 1214, 11], // ids of bloggers
  
}
```


* [ ] POST: http://host/bloggers/{blogger_id}/send_invitation/ - отправка письма одному блогеру
```json5
{
  "title": "some text",
  "body": "some text",
  "recipients": [123, 1214, 11], // ids of bloggers
  
}
```


* [ ] GET: http://host/events - получить места для посещения блогерами
```json5
// получаем следующее
{
  "points": [
    {
      "id": 1234,
      "title": "museum",
      "description": "some text",
      "address": "Samara, some street 3",
    },
    // ...
  ]
}
```
* [ ] POST: http://host/groups/ - создание группы с выбранными блогерами
```json5
{
  "bloggers": [123, 1214, 11], // ids of bloggers
}
```


* [ ] GET: http://host/groups/{group_id} - получение группы со списком блогеров
```json5
{
  "bloggers": [123, 1214, 11], // ids of bloggers
}
```


* [ ] POST: http://host/tours/ - Создание тура
```json5
{
  "title": "some text",
  "description": "some text",
  "date": "??????", 
  "events": [
    {
      "title": "some text",
      "description": "some text",
      "address": "Samara, some street 3",
      "time": 19943523452345, 
    },
    // ...
  ]
}
```

* [ ] DELETE: http://host/tours/ - Удаление тура
* [ ] PUT: http://host/tours/{tour_id} - Изменение данных тура
```json5
{
  "title": "some text",
  "description": "some text",
  "date": ""
}
```
* [ ] PUT: http://host/tours/{tour_id}/events/{event_id} - Добавление места/пункта в тур с указанием времени
* [ ] DELETE: http://host/tours/{tour_id}/events/{event_id} - Открепление места/пункта из тура

* [ ] POST: http://host/events/ - Создание even
```json5
{
  "title": "some text",
  "description": "some text",
  "address": "Samara, some street 3",
  "time": 19943523452345, 
}
```
* [ ] DELETE: http://host/events/{event_id} - Удаление event
* [ ] PUT: http://host/events/{event_id} - Изменение event
```json5
{
  "title": "some text",
  "description": "some text",
  "address": "Samara, some street 3",
  "time": 19943523452345, 
}
```
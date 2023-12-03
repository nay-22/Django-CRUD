# Django-CRUD
Django CRUD API using Django rest_framework

## Data Model
1) Artist Table
   - Name
   - User Instance (Foreign Key)
   - Work (ManyToManyField)
2) Work Table
   - Link
   - Work Type
     - Youtube(YT)
     - Instagram(IG)
     - Other(OT)
    
## API Endpoints and Usage
1) ### User registration : **api/register/**
   - Request(POST):
     ```json
     {
       "username": "luffy",
       "password": "luffy@1234"
     }
     ```
   - Response:
     ```json
     {
        "username": "luffy",
        "password": "string(encrypted)"
     }
     ```
2) ### User login (token request): **api/auth/**
   - Request(POST):
     ```json
     {
       "username": "string",
       "password": "string"
     }
     ```
   - Response:
     ```json
     {
        "token": "2ceb5e8974eaa1bff87223fa3e14918f9a18568b"
     }
     ```
3) ### Retrieve list of all works: **api/works/**
   - Request(GET)
   - Response:
     ```json
     [
        {
            "id": 1,
            "link": "https://www.instagram.com/PirateKing",
            "work_type": "IG"
        },
        {
            "id": 5,
            "link": "https://www.twitter.com/nayanlearnsdjango",
            "work_type": "OT"
        }
     ]
     ```
4) ### Retrive works list by work_type: **api/works?work_type=[work_type]**
   - Request(GET): query params - work_type=IG
   - Response
     ```json
     [
       {
         "id": 1,
         "link": "https://www.instagram.com/PirateKing",
         "work_type": "IG"
       },
       {
         "id": 6,
         "link": "https://www.instagram.com/zorojuro",
         "work_type": "IG"
        }
     ]
     ```
5) ### Retrieve works list by artist: **api/works?artist=[artist_name]**
   - Request(GET): query params - artist=potion
   - Response
     ```json
     [
       {
        "id": 2,
        "link": "https://www.youtube.com/genuinepotion",
        "work_type": "YT"
       },
       {
          "id": 3,
          "link": "https://www.youtube.com/raon",
          "work_type": "YT"
       },
       {
          "id": 4,
          "link": "https://www.youtube.com/nayan",
          "work_type": "YT"
       }
     ]
     ```
6) ### Retrieve list of all artists: **api/artists**
   - Request(GET)
   - Response
     ```json
     [
       {
        "id": 1,
        "name": "potion",
        "user": 1,
        "works": [
            2,
            3,
            4
        ]
      },
      {
          "id": 2,
          "name": "raon",
          "user": 2,
          "works": [
              5
          ]
      },
      {
          "id": 3,
          "name": "luffy",
          "user": 3,
          "works": [
              1
          ]
      }
     ]
     ```

## Local Setup
Install packages/dependencies
```bash
  pip install djangorestframework
```
Clone the project
```bash
  git clone https://github.com/nay-22/Django-CRUD.git
```

Go to the project directory
```bash
  cd artist_api
```

Run project
```bash
  python manage.py runserver
```



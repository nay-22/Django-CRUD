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
    
## API Endpoints and Usage Examples
1) ### User registration : **/api/register/**
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
2) ### User login (token request): **/api/auth/**
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
        "token": "2ceb5e8974eaa1bff87223fa3e14918f9a18568b"
     }
     ```
3) ### Retrieve list of all works: **/api/works/**
   - Request(GET): header - Authorization:Token 2ceb5e8974eaa1bff87223fa3e14918f9a18568b
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
4) ### Retrive works list by work_type: **/api/works?work_type=[work_type]**
   - Request(GET): query params - work_type=IG, header - Authorization:Token 2ceb5e8974eaa1bff87223fa3e14918f9a18568b
   - Response:
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
5) ### Retrieve works list by artist: **/api/works?artist=[artist_name]**
   - Request(GET): query params - artist=potion, header - Authorization:Token 2ceb5e8974eaa1bff87223fa3e14918f9a18568b
   - Response:
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
6) ### Retrieve list of all artists: **/api/artists**
   - Request(GET): header - Authorization:Token 2ceb5e8974eaa1bff87223fa3e14918f9a18568b
   - Response:
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
7) ### Automated Content Generation(using OpenAI): **/api/generate-description/**
   - Request(POST): header - Authorization:Token 2ceb5e8974eaa1bff87223fa3e14918f9a18568b
   - Body:
     ``` json
     {
       "product_title": "Samsung Galaxy S22"
     }
     ```
   - Response:
     ``` json
     {
       "product_description": "The Samsung Galaxy S22 is a flagship smartphone with a stunning 6.2-inch Quad HD+ Dynamic AMOLED display. Its powerful Exynos 2200 processor and 8GB of RAM ensure smooth    performance, while the 108MP triple camera system captures breathtaking photos and videos. It also features an in-display fingerprint sensor and a large 5000mAh battery.",
       "product_keywords": [
           "Samsung Galaxy S22",
           "flagship smartphone",
           "6.2-inch Quad HD+ Dynamic AMOLED display",
           "Exynos 2200 processor",
           "8GB of RAM",
           "smooth performance",
           "108MP triple camera system",
           "breathtaking photos and videos",
           "in-display fingerprint sensor",
           "large 5000mAh battery."
       ]
     }
     ```
8) ###  Image Recognition(using Amazon Rekognition): **/api/extract-text/**
   - Request(POST): header - Authorization:Token 2ceb5e8974eaa1bff87223fa3e14918f9a18568b
   - Body: **multipart/form-data**, key => image
   - Response:
     ``` json
     {
       "texts": [
           "HALLMARK",
           "FREE",
           "IMMIGRATION CONSULTANTS",
           "milestone to your success",
           "FREE IELTS",
           "PREPARATION",
           "FROM",
           "HALLMARK",
           "S",
           "Join now",
           "www.hallmarkimmigration.com",
           "+91 8872038888",
           "HALLMARK",
           "FREE",
           "IMMIGRATION",
           "CONSULTANTS",
           "milestone",
           "to",
           "your",
           "success",
           "FREE",
           "IELTS",
           "PREPARATION",
           "FROM",
           "HALLMARK",
           "S",
           "Join",
           "now",
           "www.hallmarkimmigration.com",
           "+91",
           "8872038888"
        ]
     }
     ```

## Local Setup
Install packages/dependencies
```bash
  pip install djangorestframework
```
```bash
  pip install openai
```
```bash
  pip install boto3
```
```bash
  pip install python-decouple
```
```bash
  setx OPENAI_API_KEY "Your OpenAI Key"
```
AWS setup, use AWS CLI or setup using environment variables
```bash
  aws configure
```
```bash
  AWS Access Key ID [None]: YOUR_ACCESS_KEY_ID
  AWS Secret Access Key [None]: YOUR_SECRET_ACCESS_KEY
  Default region name [None]: YOUR_REGION_NAME
  Default output format [None]: json
```
Clone the project
```bash
  git clone https://github.com/nay-22/Django-CRUD.git
```

Go to the project directory
```bash
  cd Django-CRUD
```
```bash
  cd artist_api
```

Run project
```bash
  python manage.py runserver
```



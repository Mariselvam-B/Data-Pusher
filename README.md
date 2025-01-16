# Data-Pusher

# install packeges
pip install django djangorestframework drf-yasg

# DB configurations (Maria DB {SQL})
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'datapusher',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# DB Table migration
python manage.py makemigrations
python manage.py migrate

# Run web application
 python manage.py runserver

# Test Account API
url - http://127.0.0.1:8000/api/accounts/manage_account/
method - Post
header - {"ACTION":"create"} //support(create, update, delete)
body(Json) - {
    "email": "user@example.com",
    "account_name": "strings",
    "website": "http://127.0.0.1:8000/swagger/"
}

# Test Destination API
url - http://127.0.0.1:8000/api/destinations/manage_account/
method - Post
header - {"ACTION":"create", "CL-X-TOKEN":"account token from account table"} //support(create, update, delete)
body(Json) - {
    "account_id": "your account id",
    "url": "http://127.0.0.1:8000/api/server/incoming_data",
    "http_method": "get",
    "headers": {
        "CL-X-TOKEN ": "d3716f3f-754b-4dad-b7f9-7b1c06ee0c37"
    }
}

# Test Incoming API
url - http://127.0.0.1:8000/api/incomings/manage_account/
method - Post
header - {"ACTION":"create", "CL-X-TOKEN":"account token from account table"} //support(create, update, delete)
body(Json) - {
    "destination_id": "d5e26815-1c61-4d29-aad2-78ba9b6214b5", // your destination id
    "data": "text"
}


 

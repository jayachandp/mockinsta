# MockInsta Django Web backend

REST API backend service to mock the Instagram.


### Prerequisites

The following are the required softwares for setting up the dev environment.

- Python 3.8.9
- Git 

### Creating tokens for each user
```
from rest_framework.authtoken.models import Token

token = Token.objects.create(user=...)
```
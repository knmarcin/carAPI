# Car API

API designed to connect to an external API https://vpic.nhtsa.dot.gov/api in purpose of validating if data exists, when saving it to applications database.

### Endpoints

- ```POST /cars``` 

- ```DELETE /cars/{id}```

- ```POST /rate```

- ```GET /cars```

- ```GET /popular```




### Build

- Build a ```Dockerfile```
- ```pip install requirements.txt```

### Tests
App was tested by rest_framework.test

- ```test.py``` testing endpoints and custom scenarios
- ```test_utils_connector.py``` testing if class Connector connects with external API properly
- ```test.utils_validator.py``` testing if validators works well

### Hosting
<p align="center">App is hosted on Heroku:</p>
<p align="center">https://netg-car-api.herokuapp.com/cars/</p>

<br />
<br />
<br />
<p align="center">Project created with </p>

<p align="center">
&nbsp;
<a href="https://www.python.org" target="blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a>
<a href="https://www.djangoproject.com/" target="blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="80![image](https://user-images.githubusercontent.com/33230423/131680004-0e1e5bca-6f50-4dab-a390-2a4a32454a6a.png)
" height="40"/> </a>  
<a href="https://www.django-rest-framework.org/" target="blank"> <img src="https://www.django-rest-framework.org/img/logo.png" alt="django" width="80![image](https://user-images.githubusercontent.com/33230423/131680538-e880b9fb-30fd-496c-9530-f9d3b6d85305.png)
" height="40"/> </a>
</p>

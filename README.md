## Stack used

<img src="https://skillicons.dev/icons?i=python,django,github&theme=dark" />

<br>

## Authors
[@fandredev](https://www.linkedin.com/in/devfandre/)


## Setup local environment
#### 0. Clone this repo
```
$ git clone git@github.com:fandredev/djlint-base-video-youtube.git && mv djlint-base-video-youtube djlint
```
And cd into the root folder:
```
cd djlint
```

#### 1 Start your virtualenv:
```
python -m venv venv && . venv/bin/activate
```

##### 2 Install packages:
```
pip install -r requirements.txt
```

Now, let's django migrate:
```
pipenv run ./manage.py migrate
```


Finally, create your django superuser with:
```
pipenv run ./manage.py createsuperuser
```

### 3. Run server
```
python manage.py runserver
```
It should be up and running in http://localhost:8000.
You can also access http://localhost:8000/admin.


## Feedback

If you have any feedback, please let us know via profissionalf.andre@gmail.com

## Referencies

 - [Django documentation](https://docs.djangoproject.com/en/5.0/)
 - [Python](https://www.python.org/)
 - [Djlint](https://www.djlint.com/docs/getting-started/)
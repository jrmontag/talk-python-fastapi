
# notes

- [TalkPython repo](https://github.com/talkpython/modern-apis-with-fastapi)

## Ch 3

- [HTTP status codes](https://www.webfx.com/web-development/glossary/http-status-codes/)


```
$ . venv/bin/activate
(venv) $ python ch03/main.py  
(venv) $ # then nav to localhost
```

## Ch 4

- type hints
- async/await
- wsgi vs asgi 
    - write an application in one framework e.g. flask
    - put it on heroku, run under gunicorn, etc
    - web frameworks plug into a general architecture: wsgi
        - web service gateway interface
        - expects a method e.g. request(), returns response over network
    - to avoid breaking changes for async, introduce asgi e.g. uvicorn
- pydantic classes
- rich editor support


# setup

## python install

- use pyenv on recommendation

```
$ pyenv global 3.11
$ mkcd talk-python-fastapi
$ python -m venv venv
```


## IDE

- recommend pycharm or vs code 
- install Python plugin (microsoft) 



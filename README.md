
# notes

- [TalkPython repo](https://github.com/talkpython/modern-apis-with-fastapi)

## Ch 3: a first api

- [HTTP status codes](https://www.webfx.com/web-development/glossary/http-status-codes/)


```
$ . venv/bin/activate
(venv) $ python ch03/main.py  
(venv) $ # then nav to localhost
```

## Ch 4: modern language foundations

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

## Ch 5: a realistic api
- html uses jinja templating 
    - try a vs code extension? requires different file extensions e.g. `.html.j2` or `.jinja`
- bunch of layout, css, etc - seems like just lift this content for now
    - perhaps use something like md -> html in the future
- interesting that api routers don't require `__init__.py` in directories
- initial `/weather` api path doesn't work as demonstrated in the lecture recording - requires exact path match (no extra params)
- managing secrets
    - `.gitignore` a local json file; could also use env vars
    -  don't end up part of shhgit 
- 







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



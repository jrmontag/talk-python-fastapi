
# notes
- [course site](https://training.talkpython.fm/courses/getting-started-with-fastapi)
- [course repo](https://github.com/talkpython/modern-apis-with-fastapi)

## Ch 3: a first api
- [HTTP status codes](https://www.webfx.com/web-development/glossary/http-status-codes/)

## Ch 4: modern language foundations

- type hints
    - helpful in editor, still separate from runtime
- async/await
    - mostly useful for improving scalability during i/o heavy work like db r/w
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

## Ch 6: error handling and perf
- use of async/await not well motivated yet here
- cache response in memory to start; maybe not the most elegant solution, but works
    - esp in production, likely have multiple instances/processes running and in-memory cache won't be shared 
    - alternatives might be redis, another db service, etc
- additional benefit: fewer API calls against budget
- web server app is a rare places where it's acceptable a blank exception catch (+ logging)

## Ch 7: inbound data
- to simplify, again choose an in-memory storage for reports in lieu of database
- [Postman app](https://www.postman.com/) (free + no account needed) is useful for crafting POSTs for local API
- more nuance to the 20X HTTP code -> more developer-friendly e.g. after POST request
- make a little client app with `input()` and `localhost` requests
- jinja templating is a bit unintuitive 
- OpenAPI (fka Swagger) docs are neat

## Ch 8: deployment (linux x gunicorn x nginx)
- spectrum of options for "where should I deploy my python app?"
    - Platform as a Service (PaaS) e.g. heroku: easy, and good python support; less control, can be expensive
    - Virtual Private Servier (VPS) e.g. [DigitalOcean](https://m.do.co/c/a4ad5ae8d042), [Linode](talkpython.fm/linode): lower cost; some server maintainance
        - talkpython stuff runs on Linode
    - Compute / Platform as a Service e.g. AWS: complicated and expensive
        - AWS Lightsail: new offering, lower cost, competing with DO and Linode
- follow along with DO setup
```
$ ssh root@<droplet IP>
# apt update
# apt upgrade
# reboot
```
- architecture 
    - nginx (web server, serves html/css, talks to internet)
    - gunicorn (manages app lifecycle, restart stuck apps)
    - uvicorn (+ python code; many copies of application (processes), will distribute requests appropriately)
- follow along with scripts/server_setup.sh 
    - clone from course repo to start (TODO: come back and get my copy running)
    - [] read more about the commands/programs used in server_setup.sh
    - [] read more about the weather.service configuration and systemd
    - edit weather.nginx IP mapping in-place
    - SSL setup fails as written, but would be the approach to use after pointing an owned domain to the IP address (after DNS records have updated)
- posting a report to deployed version
```
curl --header "Content-Type: application/json" \
--request POST \
--data '{"description":"Sunshine clearing away the snow","location": {"city":"Denver"}}' \
http://<deployed IP>/api/reports 
```

Update Oct 2023: moved this app to a new host; now accessible at [http://wx.jrmontag.xyz/](http://wx.jrmontag.xyz/) 


# course setup

- note that current dev machine is old so likely some brittle pieces
    - may have to skip to docker or something if things fall apart

## python install

- try out [pyenv](https://github.com/pyenv/pyenv) for this project on recommendation
    - set global to latest, point to that one for new venvs

```
$ pyenv global 3.11
$ # cd into each ch dir 
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ python main.py  
```

## IDE

- recommend pycharm or vs code 
- install Python plugin (microsoft) 


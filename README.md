# hsp-api

### Run `python -m venv venv`
### Run `venv\Scripts\activate`
### If in powershell, to change env: `$env:FLASK_ENV='development'`
### If in powershell, to change debug mode: `$env:FLASK_DEBUG=1`
### If in powershell, to app name?: `$env:FLASK_APP='hsp_app'`
### Now run: `flask run`


# How to build url
#### At the moment we are only allowing limit and offsert for members by session and members by aggregate (since they have a lot of data). Use below to build query.
- `http://127.0.0.1:5000/membersaggregate?key={your_api_key}&limit={your_limit}&offset={your_offset}`
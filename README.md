# Build a Simple CRUD App with Python, Flask, and React

This tutorial show how to build a basic CRUD (Create, Read, Update, and Delete) application using Python with Flask as the API and React for the front-end.

Please read the [Build a Simple CRUD App with Python, Flask, and React](https://developer.okta.com/blog/2018/12/20/crud-app-with-python-flask-react) to see the step-by-step instructions for creating this application.

If you'd like to simply clone this repo and configure it with your Okta settings, here's the abbreviated steps:

1. Create an [Okta developer account](https://developer.okta.com/signup) if you don't already have one.

2. Create a new **Web** app and **SPA** app on Okta with the default settings. Put your web app settings in `client_secrets.json`. For the SPA app, put your settings in `app/http/web/app/src/Main/index.js`. 

3. Start MongoDB with Docker Compose:

       docker-compose up
       export MONGO_URL=mongodb://mongo_user:mongo_secret@0.0.0.0:27017/
       
4. Start the Python backend:

       FLASK_APP=$PWD/app/http/api/endpoints.py FLASK_ENV=development pipenv run python -m flask run --port 4433

5. Start the React frontend:

       cd app/http/web/app
       npm i
       npm start

## Help

Please post any questions as comments on the [blog post](https://developer.okta.com/blog/2018/12/20/crud-app-with-python-flask-react), or visit our [Okta Developer Forums](https://devforum.okta.com/). You can also email developers@okta.com if you'd like to create a support ticket.

## License

Apache 2.0, see [LICENSE](LICENSE).

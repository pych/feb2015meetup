# Example Code to Showcase Circus

## 1. Plain circus

### Prerequites

The following python packages need to be installed

* circus
* circus-web
* chaussette

You could just run the `circus.ini` using the following command, and look at your [9999](http://localhost:9999) to see your hello world application, running.

    $ circusd --daemon circus.ini

And also have look at your [8080](http://localhost:8080), have look at the circus dashboard.

### Quit

To quit your circus daemon, just run the the following.

    $ circusctl quit

## 2. Circus running Fapp

### Prerequites

The following are the prerequisites

* Redis Server

The following python packages need to be installed

* circus
* circus-web
* chaussette
* redis
* flask

Fapp is a very basic Flask APPlication, but connects to a redis to keep a hello world counter. But to run this application you would require to quit any other circus daemons already running on your machine. Now run the application.

    (root)$ circusd --daemon fapp.ini

_NOTE: Ensure that redis-server is NOT already running._

Now point you browser to [9999](http://localhost:9999) experience the ease at which you have started your flask application and also the redis-server.





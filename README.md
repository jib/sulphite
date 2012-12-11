Sulphite
========

Sulphite is an event listener for [Supervisor][supervisor] that sends events as generated 
by Supervisor to [Graphite][graphite].

The idea behind this project is that events like restarts and backing off a continuously
failing process may be recorded in the local logfile, but they'd be far more useful if
overlayed with your other (Graphite) data like CPU usage, request per second increase or
any other resource change.

Sulphite uses the [Supervisor Events Framework][supervisor_events] and can listen and
understand any events emitted.


Installing Sulphite
-------------------

Sulphite will need the Supervisor package installed. You will probably already
have this through your package manager or own installation, but just in case:

```
$ pip install supervisor
```

To install Sulphite, you can either clone this repository and run the install script:

```
$ git clone git@github.com:jib/sulphite.git
$ cd sulphite
$ python setup.py
```

Or you can install via pip using a tarball:

```


```




[supervisor]: https://github.com/Supervisor/supervisor
[supervisor_events]: http://supervisord.org/events.html
[graphite]: https://github.com/graphite-project/graphite-web
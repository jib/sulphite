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

To install Sulphite, you can either clone this repository and run the install script:

```
$ git clone git@github.com:jib/sulphite.git
$ cd sulphite
$ python setup.py install
# OR
$ pip install -r requirements.pip
```

Or you can install via pip using the Zip archive autogenerated by Github:

```
$ pip install https://github.com/jib/sulphite/archive/master.zip
```

Configuring Sulphite
--------------------

Sulphite should run as a [Supervisor Event Listener][supervisor_events]. The simplest
configuration that makes that work is this:

```
[eventlistener:sulphite]
command=sulphite --graphite-server=graphite.example.com
events=PROCESS_STATE
numprocs=1
```

Sulphite currently only handles 'PROCESS_STATE` events, and safely ignores 'TICK'
or 'PROCESS_COMMUNICATION' events. They don't seem useful to log as graphite events,
but support for them may be added in the future.

Sulphite Options 
----------------

You can get a list of the supported options for Sulphite by running it with -h:

```
$ sulphite -h
Usage: sulphite [options]

Options:
  -h, --help            show this help message and exit
  -s GRAPHITE_SERVER, --graphite-server=GRAPHITE_SERVER
                        Graphite server address
  -p GRAPHITE_PORT, --graphite-port=GRAPHITE_PORT
                        Graphite server port
  -P GRAPHITE_PREFIX, --graphite-prefix=GRAPHITE_PREFIX
                        Prefix all graphite events with this string
  -S GRAPHITE_SUFFIX, --graphite-suffix=GRAPHITE_SUFFIX
                        Suffix all graphite events with this string
  -t GRAPHITE_TIMEOUT, --graphite-timeout=GRAPHITE_TIMEOUT
                        Timeout connection to graphite (in seconds)
  -d, --debug           Enable debug output to STDERR
```

When configuring Sulphite, you may want to supply the --debug option to
see what it's doing and then remove it when you run in production.

Sulphite Library 
----------------

You can use Sulphite as a library as well and wrap your own logic around
it's methods. It follows the convention of Python libraries and all the
CLI options can be passed to the constructor.

```python
import sulphite

object = Sulphite( ... )
```

Sulphite Events 
---------------

Sulphite will generate graphite events for every 'PROCESS_STATE' change that
is emitted by Supervisor. For example, if you start Sulphite with these options:

```
sulphite --graphite-server=graphite.example.com --graphite-prefix=events --graphite-suffix=`hostname -s`
```

And you were to restart the 'sample_service' managed by Supervisor, this is what
would be sent to graphite:

```
events.sample_service.running.process_state_stopping.my_hostname 1 1355269824
events.sample_service.stopping.process_state_stopped.my_hostname 1 1355269824
events.sample_service.stopped.process_state_starting.my_hostname 1 1355269824
events.sample_service.starting.process_state_running.my_hostname 1 1355269825
```

As you can see, the format of the events is 'ServiceName.FromState.ToState', surrounded
by the prefix & suffix we specified.

This also shows that a Supervisor restart is 4 distinct events:
* running -> stopping
* stopping -> stopped
* stopped -> starting
* starting -> started


[supervisor]: https://github.com/Supervisor/supervisor
[supervisor_events]: http://supervisord.org/events.html
[graphite]: https://github.com/graphite-project/graphite-web

#!/usr/bin/env python

import sys

from pprint     import PrettyPrinter
from optparse   import OptionParser
from sulphite   import Sulphite

PP = PrettyPrinter( indent = 4 )

### All options match the named params to Sulphite.init()
def build_parser():
    parser = OptionParser( usage="Usage: %prog [options]" )
    parser.add_option( "-s", "--graphite-server", dest="graphite_server",
                       help="Graphite server address" )
    parser.add_option( "-p", "--graphite-port", dest="graphite_port",
                       help="Graphite server port" )
    parser.add_option( "-P", "--graphite-prefix", dest="graphite_prefix",
                       help="Prefix all graphite events with this string" )
    parser.add_option( "-S", "--graphite-suffix", dest="graphite_suffix",
                       help="Suffix all graphite events with this string" )
    parser.add_option( "-t", "--graphite-timeout", dest="graphite_timeout",
                       help="Timeout connection to graphite (in seconds)" )
    parser.add_option( "-d", "--debug", dest="debug", action='store_true',
                       help="Enable debug output to STDERR" )
    return parser

def main():
    parser      = build_parser()
    opts, args  = parser.parse_args()

    #sys.stderr.write( PP.pformat( opts.__dict__ ) )

    kwargs = {}
    ### Filter out all the arguments that weren't actually passed by the user
    for k,v in vars(opts).iteritems():
        if v is not None:
            kwargs[k] = v

    #sys.stderr.write( PP.pformat( kwargs ) )
    #sys.stderr.flush()

    obj = Sulphite( **kwargs )
    obj.run()

if __name__ == '__main__':
    main()

#!/usr/bin/env python
import _env
import conf

def main():
    #from zthrift.server import server
    from utils.service import Sns
    from server.ctrl.ios import Handler

    print 'server runing ...'
    server(Sns, Handler(), ... )
    print 'done'

if __name__ == "__main__":
    main()


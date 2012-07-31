#!/usr/bin/env python
import _env

def main():
    from utils.service import Sns
    from ctrl.ios import Handler
    from utils.service import Sns

    from thrift.transport import TSocket
    from thrift.transport import TTransport
    from thrift.protocol import TBinaryProtocol
    from thrift.server import TServer

    print 'server runing ...'
    handler = Handler()
    processor = Sns.Processor(handler)
    transport = TSocket.TServerSocket(port=50042)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()


    server = TServer.TThreadedServer(processor, transport,
            tfactory, pfactory)
    server.serve()
    print 'done'

if __name__ == "__main__":
    main()


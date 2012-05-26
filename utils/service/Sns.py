#
# Autogenerated by Thrift Compiler (0.8.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def login(self, auth):
    """
    Parameters:
     - auth
    """
    pass

  def info_get(self, accessToken, id):
    """
    Parameters:
     - accessToken
     - id
    """
    pass

  def info_set(self, accessToken, userInfo):
    """
    Parameters:
     - accessToken
     - userInfo
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def login(self, auth):
    """
    Parameters:
     - auth
    """
    self.send_login(auth)
    return self.recv_login()

  def send_login(self, auth):
    self._oprot.writeMessageBegin('login', TMessageType.CALL, self._seqid)
    args = login_args()
    args.auth = auth
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_login(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = login_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.userException is not None:
      raise result.userException
    if result.systemException is not None:
      raise result.systemException
    raise TApplicationException(TApplicationException.MISSING_RESULT, "login failed: unknown result");

  def info_get(self, accessToken, id):
    """
    Parameters:
     - accessToken
     - id
    """
    self.send_info_get(accessToken, id)
    return self.recv_info_get()

  def send_info_get(self, accessToken, id):
    self._oprot.writeMessageBegin('info_get', TMessageType.CALL, self._seqid)
    args = info_get_args()
    args.accessToken = accessToken
    args.id = id
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_info_get(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = info_get_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.userException is not None:
      raise result.userException
    if result.systemException is not None:
      raise result.systemException
    if result.notFoundException is not None:
      raise result.notFoundException
    raise TApplicationException(TApplicationException.MISSING_RESULT, "info_get failed: unknown result");

  def info_set(self, accessToken, userInfo):
    """
    Parameters:
     - accessToken
     - userInfo
    """
    self.send_info_set(accessToken, userInfo)
    return self.recv_info_set()

  def send_info_set(self, accessToken, userInfo):
    self._oprot.writeMessageBegin('info_set', TMessageType.CALL, self._seqid)
    args = info_set_args()
    args.accessToken = accessToken
    args.userInfo = userInfo
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_info_set(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = info_set_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.userException is not None:
      raise result.userException
    if result.systemException is not None:
      raise result.systemException
    raise TApplicationException(TApplicationException.MISSING_RESULT, "info_set failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["login"] = Processor.process_login
    self._processMap["info_get"] = Processor.process_info_get
    self._processMap["info_set"] = Processor.process_info_set

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_login(self, seqid, iprot, oprot):
    args = login_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = login_result()
    try:
      result.success = self._handler.login(args.auth)
    except error.ttypes.UserException, userException:
      result.userException = userException
    except error.ttypes.SystemException, systemException:
      result.systemException = systemException
    oprot.writeMessageBegin("login", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_info_get(self, seqid, iprot, oprot):
    args = info_get_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = info_get_result()
    try:
      result.success = self._handler.info_get(args.accessToken, args.id)
    except error.ttypes.UserException, userException:
      result.userException = userException
    except error.ttypes.SystemException, systemException:
      result.systemException = systemException
    except error.ttypes.NotFoundException, notFoundException:
      result.notFoundException = notFoundException
    oprot.writeMessageBegin("info_get", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_info_set(self, seqid, iprot, oprot):
    args = info_set_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = info_set_result()
    try:
      result.success = self._handler.info_set(args.accessToken, args.userInfo)
    except error.ttypes.UserException, userException:
      result.userException = userException
    except error.ttypes.SystemException, systemException:
      result.systemException = systemException
    oprot.writeMessageBegin("info_set", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class login_args:
  """
  Attributes:
   - auth
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'auth', (type.ttypes.Auth, type.ttypes.Auth.thrift_spec), None, ), # 1
  )

  def __init__(self, auth=None,):
    self.auth = auth

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.auth = type.ttypes.Auth()
          self.auth.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('login_args')
    if self.auth is not None:
      oprot.writeFieldBegin('auth', TType.STRUCT, 1)
      self.auth.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class login_result:
  """
  Attributes:
   - success
   - userException
   - systemException
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (type.ttypes.AuthResponse, type.ttypes.AuthResponse.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'userException', (error.ttypes.UserException, error.ttypes.UserException.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'systemException', (error.ttypes.SystemException, error.ttypes.SystemException.thrift_spec), None, ), # 2
  )

  def __init__(self, success=None, userException=None, systemException=None,):
    self.success = success
    self.userException = userException
    self.systemException = systemException

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = type.ttypes.AuthResponse()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.userException = error.ttypes.UserException()
          self.userException.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.systemException = error.ttypes.SystemException()
          self.systemException.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('login_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.userException is not None:
      oprot.writeFieldBegin('userException', TType.STRUCT, 1)
      self.userException.write(oprot)
      oprot.writeFieldEnd()
    if self.systemException is not None:
      oprot.writeFieldBegin('systemException', TType.STRUCT, 2)
      self.systemException.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class info_get_args:
  """
  Attributes:
   - accessToken
   - id
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'accessToken', None, None, ), # 1
    (2, TType.I64, 'id', None, None, ), # 2
  )

  def __init__(self, accessToken=None, id=None,):
    self.accessToken = accessToken
    self.id = id

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.accessToken = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.id = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('info_get_args')
    if self.accessToken is not None:
      oprot.writeFieldBegin('accessToken', TType.STRING, 1)
      oprot.writeString(self.accessToken)
      oprot.writeFieldEnd()
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 2)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class info_get_result:
  """
  Attributes:
   - success
   - userException
   - systemException
   - notFoundException
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (type.ttypes.UserInfo, type.ttypes.UserInfo.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'userException', (error.ttypes.UserException, error.ttypes.UserException.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'systemException', (error.ttypes.SystemException, error.ttypes.SystemException.thrift_spec), None, ), # 2
    (3, TType.STRUCT, 'notFoundException', (error.ttypes.NotFoundException, error.ttypes.NotFoundException.thrift_spec), None, ), # 3
  )

  def __init__(self, success=None, userException=None, systemException=None, notFoundException=None,):
    self.success = success
    self.userException = userException
    self.systemException = systemException
    self.notFoundException = notFoundException

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = type.ttypes.UserInfo()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.userException = error.ttypes.UserException()
          self.userException.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.systemException = error.ttypes.SystemException()
          self.systemException.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.notFoundException = error.ttypes.NotFoundException()
          self.notFoundException.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('info_get_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.userException is not None:
      oprot.writeFieldBegin('userException', TType.STRUCT, 1)
      self.userException.write(oprot)
      oprot.writeFieldEnd()
    if self.systemException is not None:
      oprot.writeFieldBegin('systemException', TType.STRUCT, 2)
      self.systemException.write(oprot)
      oprot.writeFieldEnd()
    if self.notFoundException is not None:
      oprot.writeFieldBegin('notFoundException', TType.STRUCT, 3)
      self.notFoundException.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class info_set_args:
  """
  Attributes:
   - accessToken
   - userInfo
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'accessToken', None, None, ), # 1
    (2, TType.STRUCT, 'userInfo', (type.ttypes.UserInfo, type.ttypes.UserInfo.thrift_spec), None, ), # 2
  )

  def __init__(self, accessToken=None, userInfo=None,):
    self.accessToken = accessToken
    self.userInfo = userInfo

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.accessToken = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.userInfo = type.ttypes.UserInfo()
          self.userInfo.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('info_set_args')
    if self.accessToken is not None:
      oprot.writeFieldBegin('accessToken', TType.STRING, 1)
      oprot.writeString(self.accessToken)
      oprot.writeFieldEnd()
    if self.userInfo is not None:
      oprot.writeFieldBegin('userInfo', TType.STRUCT, 2)
      self.userInfo.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class info_set_result:
  """
  Attributes:
   - success
   - userException
   - systemException
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (type.ttypes.UserInfo, type.ttypes.UserInfo.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'userException', (error.ttypes.UserException, error.ttypes.UserException.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'systemException', (error.ttypes.SystemException, error.ttypes.SystemException.thrift_spec), None, ), # 2
  )

  def __init__(self, success=None, userException=None, systemException=None,):
    self.success = success
    self.userException = userException
    self.systemException = systemException

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = type.ttypes.UserInfo()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.userException = error.ttypes.UserException()
          self.userException.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.systemException = error.ttypes.SystemException()
          self.systemException.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('info_set_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.userException is not None:
      oprot.writeFieldBegin('userException', TType.STRUCT, 1)
      self.userException.write(oprot)
      oprot.writeFieldEnd()
    if self.systemException is not None:
      oprot.writeFieldBegin('systemException', TType.STRUCT, 2)
      self.systemException.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
#
# Autogenerated by Thrift Compiler (0.8.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class AuthResponseStatus:
  AUTH_SUCCESS = 0
  AUTH_FAIL_REASON_UNKNOWN = 1
  AUTH_FAIL_SERVER_ERROR = 2
  AUTH_FAIL_CLIENT_KEY_NOT_AUTHORIZED = 3
  AUTH_FAIL_CLIENT_SECRET_WRONG = 4
  AUTH_FAIL_ID_NOT_EXIST = 5
  AUTH_FAIL_ID_INVALID = 6
  AUTH_FAIL_PASSWORD_WRONG = 7

  _VALUES_TO_NAMES = {
    0: "AUTH_SUCCESS",
    1: "AUTH_FAIL_REASON_UNKNOWN",
    2: "AUTH_FAIL_SERVER_ERROR",
    3: "AUTH_FAIL_CLIENT_KEY_NOT_AUTHORIZED",
    4: "AUTH_FAIL_CLIENT_SECRET_WRONG",
    5: "AUTH_FAIL_ID_NOT_EXIST",
    6: "AUTH_FAIL_ID_INVALID",
    7: "AUTH_FAIL_PASSWORD_WRONG",
  }

  _NAMES_TO_VALUES = {
    "AUTH_SUCCESS": 0,
    "AUTH_FAIL_REASON_UNKNOWN": 1,
    "AUTH_FAIL_SERVER_ERROR": 2,
    "AUTH_FAIL_CLIENT_KEY_NOT_AUTHORIZED": 3,
    "AUTH_FAIL_CLIENT_SECRET_WRONG": 4,
    "AUTH_FAIL_ID_NOT_EXIST": 5,
    "AUTH_FAIL_ID_INVALID": 6,
    "AUTH_FAIL_PASSWORD_WRONG": 7,
  }

class UserLinkType:
  USER_LINK_TYPE_UNKNOWN = 0
  USER_LINK_TYPE_42QU = 1
  USER_LINK_TYPE_DOUBAN = 2
  USER_LINK_TYPE_WEIBO = 3

  _VALUES_TO_NAMES = {
    0: "USER_LINK_TYPE_UNKNOWN",
    1: "USER_LINK_TYPE_42QU",
    2: "USER_LINK_TYPE_DOUBAN",
    3: "USER_LINK_TYPE_WEIBO",
  }

  _NAMES_TO_VALUES = {
    "USER_LINK_TYPE_UNKNOWN": 0,
    "USER_LINK_TYPE_42QU": 1,
    "USER_LINK_TYPE_DOUBAN": 2,
    "USER_LINK_TYPE_WEIBO": 3,
  }

class UserPhoneType:
  USER_PHONE_TYPE_UNKNOWN = 0
  USER_PHONE_TYPE_PUBLIC = 1
  USER_PHONE_TYPE_CUSTOM = 2
  USER_PHONE_TYPE_MOBILE = 3
  USER_PHONE_TYPE_HOME = 4
  USER_PHONE_TYPE_BUSINESS = 5
  USER_PHONE_TYPE_FAX = 6

  _VALUES_TO_NAMES = {
    0: "USER_PHONE_TYPE_UNKNOWN",
    1: "USER_PHONE_TYPE_PUBLIC",
    2: "USER_PHONE_TYPE_CUSTOM",
    3: "USER_PHONE_TYPE_MOBILE",
    4: "USER_PHONE_TYPE_HOME",
    5: "USER_PHONE_TYPE_BUSINESS",
    6: "USER_PHONE_TYPE_FAX",
  }

  _NAMES_TO_VALUES = {
    "USER_PHONE_TYPE_UNKNOWN": 0,
    "USER_PHONE_TYPE_PUBLIC": 1,
    "USER_PHONE_TYPE_CUSTOM": 2,
    "USER_PHONE_TYPE_MOBILE": 3,
    "USER_PHONE_TYPE_HOME": 4,
    "USER_PHONE_TYPE_BUSINESS": 5,
    "USER_PHONE_TYPE_FAX": 6,
  }

class UserMailType:
  USER_MAIL_TYPE_UNKNOWN = 0
  USER_MAIL_TYPE_PUBLIC = 1
  USER_MAIL_TYPE_CUSTOM = 2
  USER_MAIL_TYPE_HOME = 3
  USER_MAIL_TYPE_BUSINESS = 4

  _VALUES_TO_NAMES = {
    0: "USER_MAIL_TYPE_UNKNOWN",
    1: "USER_MAIL_TYPE_PUBLIC",
    2: "USER_MAIL_TYPE_CUSTOM",
    3: "USER_MAIL_TYPE_HOME",
    4: "USER_MAIL_TYPE_BUSINESS",
  }

  _NAMES_TO_VALUES = {
    "USER_MAIL_TYPE_UNKNOWN": 0,
    "USER_MAIL_TYPE_PUBLIC": 1,
    "USER_MAIL_TYPE_CUSTOM": 2,
    "USER_MAIL_TYPE_HOME": 3,
    "USER_MAIL_TYPE_BUSINESS": 4,
  }


class Auth:
  """
  Attributes:
   - id
   - password
   - clientKey
   - clientSecret
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'id', None, None, ), # 1
    (2, TType.STRING, 'password', None, None, ), # 2
    (3, TType.STRING, 'clientKey', None, None, ), # 3
    (4, TType.STRING, 'clientSecret', None, None, ), # 4
  )

  def __init__(self, id=None, password=None, clientKey=None, clientSecret=None,):
    self.id = id
    self.password = password
    self.clientKey = clientKey
    self.clientSecret = clientSecret

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
        if ftype == TType.I64:
          self.id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.password = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.clientKey = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.clientSecret = iprot.readString();
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
    oprot.writeStructBegin('Auth')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 1)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    if self.password is not None:
      oprot.writeFieldBegin('password', TType.STRING, 2)
      oprot.writeString(self.password)
      oprot.writeFieldEnd()
    if self.clientKey is not None:
      oprot.writeFieldBegin('clientKey', TType.STRING, 3)
      oprot.writeString(self.clientKey)
      oprot.writeFieldEnd()
    if self.clientSecret is not None:
      oprot.writeFieldBegin('clientSecret', TType.STRING, 4)
      oprot.writeString(self.clientSecret)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.password is None:
      raise TProtocol.TProtocolException(message='Required field password is unset!')
    if self.clientKey is None:
      raise TProtocol.TProtocolException(message='Required field clientKey is unset!')
    if self.clientSecret is None:
      raise TProtocol.TProtocolException(message='Required field clientSecret is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AuthResponse:
  """
  Attributes:
   - status
   - id
   - name
   - accessToken
   - expireDate
   - refreshToken
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'status', None, None, ), # 1
    (2, TType.I64, 'id', None, None, ), # 2
    (3, TType.STRING, 'name', None, None, ), # 3
    (4, TType.STRING, 'accessToken', None, None, ), # 4
    (5, TType.I64, 'expireDate', None, None, ), # 5
    (6, TType.STRING, 'refreshToken', None, None, ), # 6
  )

  def __init__(self, status=None, id=None, name=None, accessToken=None, expireDate=None, refreshToken=None,):
    self.status = status
    self.id = id
    self.name = name
    self.accessToken = accessToken
    self.expireDate = expireDate
    self.refreshToken = refreshToken

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
        if ftype == TType.I32:
          self.status = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.accessToken = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.expireDate = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.refreshToken = iprot.readString();
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
    oprot.writeStructBegin('AuthResponse')
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.I32, 1)
      oprot.writeI32(self.status)
      oprot.writeFieldEnd()
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 2)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 3)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.accessToken is not None:
      oprot.writeFieldBegin('accessToken', TType.STRING, 4)
      oprot.writeString(self.accessToken)
      oprot.writeFieldEnd()
    if self.expireDate is not None:
      oprot.writeFieldBegin('expireDate', TType.I64, 5)
      oprot.writeI64(self.expireDate)
      oprot.writeFieldEnd()
    if self.refreshToken is not None:
      oprot.writeFieldBegin('refreshToken', TType.STRING, 6)
      oprot.writeString(self.refreshToken)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.accessToken is None:
      raise TProtocol.TProtocolException(message='Required field accessToken is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UserLink:
  """
  Attributes:
   - id
   - type
   - value
   - customType
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'id', None, None, ), # 1
    (2, TType.I32, 'type', None, None, ), # 2
    (3, TType.STRING, 'value', None, None, ), # 3
    (4, TType.STRING, 'customType', None, None, ), # 4
  )

  def __init__(self, id=None, type=None, value=None, customType=None,):
    self.id = id
    self.type = type
    self.value = value
    self.customType = customType

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
        if ftype == TType.I64:
          self.id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.value = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.customType = iprot.readString();
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
    oprot.writeStructBegin('UserLink')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 1)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 2)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.value is not None:
      oprot.writeFieldBegin('value', TType.STRING, 3)
      oprot.writeString(self.value)
      oprot.writeFieldEnd()
    if self.customType is not None:
      oprot.writeFieldBegin('customType', TType.STRING, 4)
      oprot.writeString(self.customType)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.type is None:
      raise TProtocol.TProtocolException(message='Required field type is unset!')
    if self.value is None:
      raise TProtocol.TProtocolException(message='Required field value is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UserPhone:
  """
  Attributes:
   - id
   - type
   - value
   - customType
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'id', None, None, ), # 1
    (2, TType.I32, 'type', None, None, ), # 2
    (3, TType.STRING, 'value', None, None, ), # 3
    (4, TType.STRING, 'customType', None, None, ), # 4
  )

  def __init__(self, id=None, type=None, value=None, customType=None,):
    self.id = id
    self.type = type
    self.value = value
    self.customType = customType

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
        if ftype == TType.I64:
          self.id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.value = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.customType = iprot.readString();
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
    oprot.writeStructBegin('UserPhone')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 1)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 2)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.value is not None:
      oprot.writeFieldBegin('value', TType.STRING, 3)
      oprot.writeString(self.value)
      oprot.writeFieldEnd()
    if self.customType is not None:
      oprot.writeFieldBegin('customType', TType.STRING, 4)
      oprot.writeString(self.customType)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.type is None:
      raise TProtocol.TProtocolException(message='Required field type is unset!')
    if self.value is None:
      raise TProtocol.TProtocolException(message='Required field value is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UserMail:
  """
  Attributes:
   - id
   - type
   - value
   - customType
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'id', None, None, ), # 1
    (2, TType.I32, 'type', None, None, ), # 2
    (3, TType.STRING, 'value', None, None, ), # 3
    (4, TType.STRING, 'customType', None, None, ), # 4
  )

  def __init__(self, id=None, type=None, value=None, customType=None,):
    self.id = id
    self.type = type
    self.value = value
    self.customType = customType

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
        if ftype == TType.I64:
          self.id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.value = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.customType = iprot.readString();
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
    oprot.writeStructBegin('UserMail')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 1)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 2)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.value is not None:
      oprot.writeFieldBegin('value', TType.STRING, 3)
      oprot.writeString(self.value)
      oprot.writeFieldEnd()
    if self.customType is not None:
      oprot.writeFieldBegin('customType', TType.STRING, 4)
      oprot.writeString(self.customType)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.type is None:
      raise TProtocol.TProtocolException(message='Required field type is unset!')
    if self.value is None:
      raise TProtocol.TProtocolException(message='Required field value is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UserInfo:
  """
  Attributes:
   - id
   - name
   - intro
   - picture
   - userLinkList
   - userPhoneList
   - userMailList
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'id', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'intro', None, None, ), # 3
    (4, TType.STRING, 'picture', None, None, ), # 4
    (5, TType.LIST, 'userLinkList', (TType.STRUCT,(UserLink, UserLink.thrift_spec)), None, ), # 5
    (6, TType.LIST, 'userPhoneList', (TType.STRUCT,(UserPhone, UserPhone.thrift_spec)), None, ), # 6
    (7, TType.LIST, 'userMailList', (TType.STRUCT,(UserMail, UserMail.thrift_spec)), None, ), # 7
  )

  def __init__(self, id=None, name=None, intro=None, picture=None, userLinkList=None, userPhoneList=None, userMailList=None,):
    self.id = id
    self.name = name
    self.intro = intro
    self.picture = picture
    self.userLinkList = userLinkList
    self.userPhoneList = userPhoneList
    self.userMailList = userMailList

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
        if ftype == TType.I64:
          self.id = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.intro = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.picture = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.userLinkList = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = UserLink()
            _elem5.read(iprot)
            self.userLinkList.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.userPhoneList = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = UserPhone()
            _elem11.read(iprot)
            self.userPhoneList.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.userMailList = []
          (_etype15, _size12) = iprot.readListBegin()
          for _i16 in xrange(_size12):
            _elem17 = UserMail()
            _elem17.read(iprot)
            self.userMailList.append(_elem17)
          iprot.readListEnd()
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
    oprot.writeStructBegin('UserInfo')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.I64, 1)
      oprot.writeI64(self.id)
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.intro is not None:
      oprot.writeFieldBegin('intro', TType.STRING, 3)
      oprot.writeString(self.intro)
      oprot.writeFieldEnd()
    if self.picture is not None:
      oprot.writeFieldBegin('picture', TType.STRING, 4)
      oprot.writeString(self.picture)
      oprot.writeFieldEnd()
    if self.userLinkList is not None:
      oprot.writeFieldBegin('userLinkList', TType.LIST, 5)
      oprot.writeListBegin(TType.STRUCT, len(self.userLinkList))
      for iter18 in self.userLinkList:
        iter18.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.userPhoneList is not None:
      oprot.writeFieldBegin('userPhoneList', TType.LIST, 6)
      oprot.writeListBegin(TType.STRUCT, len(self.userPhoneList))
      for iter19 in self.userPhoneList:
        iter19.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.userMailList is not None:
      oprot.writeFieldBegin('userMailList', TType.LIST, 7)
      oprot.writeListBegin(TType.STRUCT, len(self.userMailList))
      for iter20 in self.userMailList:
        iter20.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.id is None:
      raise TProtocol.TProtocolException(message='Required field id is unset!')
    if self.name is None:
      raise TProtocol.TProtocolException(message='Required field name is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
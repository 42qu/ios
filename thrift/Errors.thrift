enum ErrorCode {
  UNKNOWN = 1,
  BAD_DATA_FORMAT = 2,
  PERMISSION_DENIED = 3,
  INTERNAL_ERROR = 4,
  DATA_REQUIRED = 5,
  LIMIT_REACHED = 6,
  QUOTA_REACHED = 7,
  INVALID_AUTH = 8,
  AUTH_EXPIRED = 9,
  DATA_CONFLICT = 10,
  ENML_VALIDATION = 11,
  SHARD_UNAVAILABLE = 12,
  LEN_TOO_SHORT = 13,
  LEN_TOO_LONG = 14,
  TOO_FEW = 15,
  TOO_MANY = 16,
  UNSUPPORTED_OPERATION = 17
}

exception UserException {
  1:  required  ErrorCode errorCode,
  2:  optional  string parameter
}

exception SystemException {
  1:  required  ErrorCode errorCode,
  2:  optional  string message
}

exception NotFoundException {
  1:  optional  string identifier,
  2:  optional  string key
}

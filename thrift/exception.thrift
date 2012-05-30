enum ExceptionCode {
    PERMISSION_DENIED = 101,
    INNER_ERROR = 102,
    USER_VERIFY_FAILED = 103,
    USER_NOT_EXIST = 104
}

exception Exception {
  1:  optional  ExceptionCode code,
  2:  optional  string message 
}


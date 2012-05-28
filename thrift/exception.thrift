enum ExceptionCode {
  NOT_EXIST = 1,
  NO_PRIVILEGE = 2,
}


exception Exception {
  1:  optional  ExceptionCode code,
  2:  optional  string message 
}



// User
typedef i64 UserID

struct Account {
  1:  required  UserID id,
  2:  optional  string email
}

struct UserSNSAccounts {
  1:  optional  string 42qu,
  2:  optional  string douban,
  3:  optional  string weibo
  4:  optional  string renren
}

struct UserPrivateInfo {
  1:  required  string email,
  2:  required  string phone,
  3:  required  string wechat
}

struct UserInfo {
  1:  required  UserID id,
  2:  required  string nickname,
  3:  required  string introduction,
  4:  required  string picture,
  5:  required  UserSNSAccounts snsAccounts,
  6:  optional  UserPrivateInfo privateInfo
}

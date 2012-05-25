// Account
typedef i64 UserID

// ----- User Link -----

typedef i64 LinkID

enum {
  UserLinkTypeUnknown = 0,
  UserLinkType42qu,
  UserLinkTypeDouban,
  UserLinkTypeWeibo
} typedef i64 UserLinkType

struct UserLink {
  1:  required  LinkID id,
  2:  required  UserLinkType cid,
  3:  required  string rid
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
  5:  required  set<UserLink> snsAccounts,
  6:  optional  UserPrivateInfo privateInfo
}

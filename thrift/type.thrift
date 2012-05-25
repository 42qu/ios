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

typedef i64 PhoneID
enum {
  UserPhoneTypeUnknown = 0,
  UserPhoneTypePublic,
  UserPhoneTypeMobile,
  UserPhoneTypeHome,
  UserPhoneTypeBusiness,
  UserPhoneTypeFax,
  UserPhoneTypeCustom
} typedef i64 UserPhoneType

struct UserPhone {
  1:  required  PhoneID id,
  2:  required  UserPhoneType cid,
  3:  required  string rid,
  4:  optional  string customType
}

typedef i64 MailID
enum {
  UserMailTypeUnknown = 0,
  UserMailTypePublic,
  UserMailTypeHome,
  UserMailTypeBusiness,
  UserMailTypeCustom
} typedef i64 UserMailType

struct UserMail {
  1:  required  MailID id,
  2:  required  UserMailType cid,
  3:  required  string rid,
  4:  optional  string customType
}

struct UserInfo {
  1:  required  UserID id,
  2:  required  string nickname,
  3:  required  string introduction,
  4:  required  string picture,
  5:  required  list<UserLink> userLinkList,
  6:  required  list<UserPhone> userPhoneList,
  7:  required  list<UserMail> userMailList
}

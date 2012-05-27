/**
 * Autogenerated by Thrift Compiler (0.8.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

#import <Foundation/Foundation.h>

#import <TProtocol.h>
#import <TApplicationException.h>
#import <TProtocolUtil.h>
#import <TProcessor.h>


enum AuthResponseStatus {
  AuthResponseStatus_AUTH_SUCCESS = 0,
  AuthResponseStatus_AUTH_FAIL_REASON_UNKNOWN = 1,
  AuthResponseStatus_AUTH_FAIL_SERVER_ERROR = 2,
  AuthResponseStatus_AUTH_FAIL_CLIENT_KEY_NOT_AUTHORIZED = 3,
  AuthResponseStatus_AUTH_FAIL_CLIENT_SECRET_WRONG = 4,
  AuthResponseStatus_AUTH_FAIL_ID_NOT_EXIST = 5,
  AuthResponseStatus_AUTH_FAIL_ID_INVALID = 6,
  AuthResponseStatus_AUTH_FAIL_PASSWORD_WRONG = 7
};

enum UserLinkType {
  UserLinkType_USER_LINK_TYPE_UNKNOWN = 0,
  UserLinkType_USER_LINK_TYPE_42QU = 1,
  UserLinkType_USER_LINK_TYPE_DOUBAN = 2,
  UserLinkType_USER_LINK_TYPE_WEIBO = 3
};

enum UserPhoneType {
  UserPhoneType_USER_PHONE_TYPE_UNKNOWN = 0,
  UserPhoneType_USER_PHONE_TYPE_PUBLIC = 1,
  UserPhoneType_USER_PHONE_TYPE_CUSTOM = 2,
  UserPhoneType_USER_PHONE_TYPE_MOBILE = 3,
  UserPhoneType_USER_PHONE_TYPE_HOME = 4,
  UserPhoneType_USER_PHONE_TYPE_BUSINESS = 5,
  UserPhoneType_USER_PHONE_TYPE_FAX = 6
};

enum UserMailType {
  UserMailType_USER_MAIL_TYPE_UNKNOWN = 0,
  UserMailType_USER_MAIL_TYPE_PUBLIC = 1,
  UserMailType_USER_MAIL_TYPE_CUSTOM = 2,
  UserMailType_USER_MAIL_TYPE_HOME = 3,
  UserMailType_USER_MAIL_TYPE_BUSINESS = 4
};

enum EventType {
  EventType_EVENT_TYPE_DEFAULT = 0
};

typedef int64_t TimeStamp;

@interface Auth : NSObject <NSCoding> {
  NSString * __user;
  NSString * __password;
  NSString * __clientKey;
  NSString * __clientSecret;

  BOOL __user_isset;
  BOOL __password_isset;
  BOOL __clientKey_isset;
  BOOL __clientSecret_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, retain, getter=user, setter=setUser:) NSString * user;
@property (nonatomic, retain, getter=password, setter=setPassword:) NSString * password;
@property (nonatomic, retain, getter=clientKey, setter=setClientKey:) NSString * clientKey;
@property (nonatomic, retain, getter=clientSecret, setter=setClientSecret:) NSString * clientSecret;
#endif

- (id) initWithUser: (NSString *) user password: (NSString *) password clientKey: (NSString *) clientKey clientSecret: (NSString *) clientSecret;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (NSString *) user;
- (void) setUser: (NSString *) user;
- (BOOL) userIsSet;

- (NSString *) password;
- (void) setPassword: (NSString *) password;
- (BOOL) passwordIsSet;

- (NSString *) clientKey;
- (void) setClientKey: (NSString *) clientKey;
- (BOOL) clientKeyIsSet;

- (NSString *) clientSecret;
- (void) setClientSecret: (NSString *) clientSecret;
- (BOOL) clientSecretIsSet;

@end

@interface AuthResponse : NSObject <NSCoding> {
  int __status;
  int64_t __id;
  NSString * __name;
  NSString * __accessToken;
  int64_t __expireDate;
  NSString * __refreshToken;

  BOOL __status_isset;
  BOOL __id_isset;
  BOOL __name_isset;
  BOOL __accessToken_isset;
  BOOL __expireDate_isset;
  BOOL __refreshToken_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=status, setter=setStatus:) int status;
@property (nonatomic, getter=id, setter=setId:) int64_t id;
@property (nonatomic, retain, getter=name, setter=setName:) NSString * name;
@property (nonatomic, retain, getter=accessToken, setter=setAccessToken:) NSString * accessToken;
@property (nonatomic, getter=expireDate, setter=setExpireDate:) int64_t expireDate;
@property (nonatomic, retain, getter=refreshToken, setter=setRefreshToken:) NSString * refreshToken;
#endif

- (id) initWithStatus: (int) status id: (int64_t) id name: (NSString *) name accessToken: (NSString *) accessToken expireDate: (int64_t) expireDate refreshToken: (NSString *) refreshToken;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int) status;
- (void) setStatus: (int) status;
- (BOOL) statusIsSet;

- (int64_t) id;
- (void) setId: (int64_t) id;
- (BOOL) idIsSet;

- (NSString *) name;
- (void) setName: (NSString *) name;
- (BOOL) nameIsSet;

- (NSString *) accessToken;
- (void) setAccessToken: (NSString *) accessToken;
- (BOOL) accessTokenIsSet;

- (int64_t) expireDate;
- (void) setExpireDate: (int64_t) expireDate;
- (BOOL) expireDateIsSet;

- (NSString *) refreshToken;
- (void) setRefreshToken: (NSString *) refreshToken;
- (BOOL) refreshTokenIsSet;

@end

@interface UserLink : NSObject <NSCoding> {
  int64_t __id;
  int __type;
  NSString * __value;
  NSString * __label;

  BOOL __id_isset;
  BOOL __type_isset;
  BOOL __value_isset;
  BOOL __label_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=id, setter=setId:) int64_t id;
@property (nonatomic, getter=type, setter=setType:) int type;
@property (nonatomic, retain, getter=value, setter=setValue:) NSString * value;
@property (nonatomic, retain, getter=label, setter=setLabel:) NSString * label;
#endif

- (id) initWithId: (int64_t) id type: (int) type value: (NSString *) value label: (NSString *) label;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) id;
- (void) setId: (int64_t) id;
- (BOOL) idIsSet;

- (int) type;
- (void) setType: (int) type;
- (BOOL) typeIsSet;

- (NSString *) value;
- (void) setValue: (NSString *) value;
- (BOOL) valueIsSet;

- (NSString *) label;
- (void) setLabel: (NSString *) label;
- (BOOL) labelIsSet;

@end

@interface UserPhone : NSObject <NSCoding> {
  int64_t __id;
  int __type;
  NSString * __value;
  NSString * __label;

  BOOL __id_isset;
  BOOL __type_isset;
  BOOL __value_isset;
  BOOL __label_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=id, setter=setId:) int64_t id;
@property (nonatomic, getter=type, setter=setType:) int type;
@property (nonatomic, retain, getter=value, setter=setValue:) NSString * value;
@property (nonatomic, retain, getter=label, setter=setLabel:) NSString * label;
#endif

- (id) initWithId: (int64_t) id type: (int) type value: (NSString *) value label: (NSString *) label;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) id;
- (void) setId: (int64_t) id;
- (BOOL) idIsSet;

- (int) type;
- (void) setType: (int) type;
- (BOOL) typeIsSet;

- (NSString *) value;
- (void) setValue: (NSString *) value;
- (BOOL) valueIsSet;

- (NSString *) label;
- (void) setLabel: (NSString *) label;
- (BOOL) labelIsSet;

@end

@interface UserMail : NSObject <NSCoding> {
  int64_t __id;
  int __type;
  NSString * __value;
  NSString * __label;

  BOOL __id_isset;
  BOOL __type_isset;
  BOOL __value_isset;
  BOOL __label_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=id, setter=setId:) int64_t id;
@property (nonatomic, getter=type, setter=setType:) int type;
@property (nonatomic, retain, getter=value, setter=setValue:) NSString * value;
@property (nonatomic, retain, getter=label, setter=setLabel:) NSString * label;
#endif

- (id) initWithId: (int64_t) id type: (int) type value: (NSString *) value label: (NSString *) label;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) id;
- (void) setId: (int64_t) id;
- (BOOL) idIsSet;

- (int) type;
- (void) setType: (int) type;
- (BOOL) typeIsSet;

- (NSString *) value;
- (void) setValue: (NSString *) value;
- (BOOL) valueIsSet;

- (NSString *) label;
- (void) setLabel: (NSString *) label;
- (BOOL) labelIsSet;

@end

@interface UserInfo : NSObject <NSCoding> {
  int64_t __id;
  NSString * __name;
  NSString * __intro;
  NSData * __picture;
  NSArray * __userLinkList;
  NSArray * __userPhoneList;
  NSArray * __userMailList;

  BOOL __id_isset;
  BOOL __name_isset;
  BOOL __intro_isset;
  BOOL __picture_isset;
  BOOL __userLinkList_isset;
  BOOL __userPhoneList_isset;
  BOOL __userMailList_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=id, setter=setId:) int64_t id;
@property (nonatomic, retain, getter=name, setter=setName:) NSString * name;
@property (nonatomic, retain, getter=intro, setter=setIntro:) NSString * intro;
@property (nonatomic, retain, getter=picture, setter=setPicture:) NSData * picture;
@property (nonatomic, retain, getter=userLinkList, setter=setUserLinkList:) NSArray * userLinkList;
@property (nonatomic, retain, getter=userPhoneList, setter=setUserPhoneList:) NSArray * userPhoneList;
@property (nonatomic, retain, getter=userMailList, setter=setUserMailList:) NSArray * userMailList;
#endif

- (id) initWithId: (int64_t) id name: (NSString *) name intro: (NSString *) intro picture: (NSData *) picture userLinkList: (NSArray *) userLinkList userPhoneList: (NSArray *) userPhoneList userMailList: (NSArray *) userMailList;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) id;
- (void) setId: (int64_t) id;
- (BOOL) idIsSet;

- (NSString *) name;
- (void) setName: (NSString *) name;
- (BOOL) nameIsSet;

- (NSString *) intro;
- (void) setIntro: (NSString *) intro;
- (BOOL) introIsSet;

- (NSData *) picture;
- (void) setPicture: (NSData *) picture;
- (BOOL) pictureIsSet;

- (NSArray *) userLinkList;
- (void) setUserLinkList: (NSArray *) userLinkList;
- (BOOL) userLinkListIsSet;

- (NSArray *) userPhoneList;
- (void) setUserPhoneList: (NSArray *) userPhoneList;
- (BOOL) userPhoneListIsSet;

- (NSArray *) userMailList;
- (void) setUserMailList: (NSArray *) userMailList;
- (BOOL) userMailListIsSet;

@end

@interface StatusPost : NSObject <NSCoding> {
  NSString * __content;
  NSArray * __tagList;

  BOOL __content_isset;
  BOOL __tagList_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, retain, getter=content, setter=setContent:) NSString * content;
@property (nonatomic, retain, getter=tagList, setter=setTagList:) NSArray * tagList;
#endif

- (id) initWithContent: (NSString *) content tagList: (NSArray *) tagList;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (NSString *) content;
- (void) setContent: (NSString *) content;
- (BOOL) contentIsSet;

- (NSArray *) tagList;
- (void) setTagList: (NSArray *) tagList;
- (BOOL) tagListIsSet;

@end

@interface StatusComment : NSObject <NSCoding> {
  int64_t __id;
  int64_t __authorID;
  NSString * __authorName;
  TimeStamp __date;
  NSString * __content;

  BOOL __id_isset;
  BOOL __authorID_isset;
  BOOL __authorName_isset;
  BOOL __date_isset;
  BOOL __content_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=id, setter=setId:) int64_t id;
@property (nonatomic, getter=authorID, setter=setAuthorID:) int64_t authorID;
@property (nonatomic, retain, getter=authorName, setter=setAuthorName:) NSString * authorName;
@property (nonatomic, getter=date, setter=setDate:) TimeStamp date;
@property (nonatomic, retain, getter=content, setter=setContent:) NSString * content;
#endif

- (id) initWithId: (int64_t) id authorID: (int64_t) authorID authorName: (NSString *) authorName date: (TimeStamp) date content: (NSString *) content;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) id;
- (void) setId: (int64_t) id;
- (BOOL) idIsSet;

- (int64_t) authorID;
- (void) setAuthorID: (int64_t) authorID;
- (BOOL) authorIDIsSet;

- (NSString *) authorName;
- (void) setAuthorName: (NSString *) authorName;
- (BOOL) authorNameIsSet;

- (TimeStamp) date;
- (void) setDate: (TimeStamp) date;
- (BOOL) dateIsSet;

- (NSString *) content;
- (void) setContent: (NSString *) content;
- (BOOL) contentIsSet;

@end

@interface Status : NSObject <NSCoding> {
  int64_t __id;
  int64_t __authorID;
  NSString * __authorName;
  TimeStamp __date;
  NSString * __content;
  int64_t __commentCount;
  NSArray * __commentList;

  BOOL __id_isset;
  BOOL __authorID_isset;
  BOOL __authorName_isset;
  BOOL __date_isset;
  BOOL __content_isset;
  BOOL __commentCount_isset;
  BOOL __commentList_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=id, setter=setId:) int64_t id;
@property (nonatomic, getter=authorID, setter=setAuthorID:) int64_t authorID;
@property (nonatomic, retain, getter=authorName, setter=setAuthorName:) NSString * authorName;
@property (nonatomic, getter=date, setter=setDate:) TimeStamp date;
@property (nonatomic, retain, getter=content, setter=setContent:) NSString * content;
@property (nonatomic, getter=commentCount, setter=setCommentCount:) int64_t commentCount;
@property (nonatomic, retain, getter=commentList, setter=setCommentList:) NSArray * commentList;
#endif

- (id) initWithId: (int64_t) id authorID: (int64_t) authorID authorName: (NSString *) authorName date: (TimeStamp) date content: (NSString *) content commentCount: (int64_t) commentCount commentList: (NSArray *) commentList;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) id;
- (void) setId: (int64_t) id;
- (BOOL) idIsSet;

- (int64_t) authorID;
- (void) setAuthorID: (int64_t) authorID;
- (BOOL) authorIDIsSet;

- (NSString *) authorName;
- (void) setAuthorName: (NSString *) authorName;
- (BOOL) authorNameIsSet;

- (TimeStamp) date;
- (void) setDate: (TimeStamp) date;
- (BOOL) dateIsSet;

- (NSString *) content;
- (void) setContent: (NSString *) content;
- (BOOL) contentIsSet;

- (int64_t) commentCount;
- (void) setCommentCount: (int64_t) commentCount;
- (BOOL) commentCountIsSet;

- (NSArray *) commentList;
- (void) setCommentList: (NSArray *) commentList;
- (BOOL) commentListIsSet;

@end

@interface EventInfo : NSObject <NSCoding> {
  int64_t __id;
  NSString * __title;
  NSString * __intro;
  int __eventType;
  TimeStamp __startDate;
  TimeStamp __expireDate;
  UserInfo * __initiator;
  NSArray * __guestList;
  int64_t __participantAuthedCount;
  int64_t __participantUnauthedCount;
  NSArray * __participantAuthedList;
  NSArray * __participantUnauthedList;

  BOOL __id_isset;
  BOOL __title_isset;
  BOOL __intro_isset;
  BOOL __eventType_isset;
  BOOL __startDate_isset;
  BOOL __expireDate_isset;
  BOOL __initiator_isset;
  BOOL __guestList_isset;
  BOOL __participantAuthedCount_isset;
  BOOL __participantUnauthedCount_isset;
  BOOL __participantAuthedList_isset;
  BOOL __participantUnauthedList_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=id, setter=setId:) int64_t id;
@property (nonatomic, retain, getter=title, setter=setTitle:) NSString * title;
@property (nonatomic, retain, getter=intro, setter=setIntro:) NSString * intro;
@property (nonatomic, getter=eventType, setter=setEventType:) int eventType;
@property (nonatomic, getter=startDate, setter=setStartDate:) TimeStamp startDate;
@property (nonatomic, getter=expireDate, setter=setExpireDate:) TimeStamp expireDate;
@property (nonatomic, retain, getter=initiator, setter=setInitiator:) UserInfo * initiator;
@property (nonatomic, retain, getter=guestList, setter=setGuestList:) NSArray * guestList;
@property (nonatomic, getter=participantAuthedCount, setter=setParticipantAuthedCount:) int64_t participantAuthedCount;
@property (nonatomic, getter=participantUnauthedCount, setter=setParticipantUnauthedCount:) int64_t participantUnauthedCount;
@property (nonatomic, retain, getter=participantAuthedList, setter=setParticipantAuthedList:) NSArray * participantAuthedList;
@property (nonatomic, retain, getter=participantUnauthedList, setter=setParticipantUnauthedList:) NSArray * participantUnauthedList;
#endif

- (id) initWithId: (int64_t) id title: (NSString *) title intro: (NSString *) intro eventType: (int) eventType startDate: (TimeStamp) startDate expireDate: (TimeStamp) expireDate initiator: (UserInfo *) initiator guestList: (NSArray *) guestList participantAuthedCount: (int64_t) participantAuthedCount participantUnauthedCount: (int64_t) participantUnauthedCount participantAuthedList: (NSArray *) participantAuthedList participantUnauthedList: (NSArray *) participantUnauthedList;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) id;
- (void) setId: (int64_t) id;
- (BOOL) idIsSet;

- (NSString *) title;
- (void) setTitle: (NSString *) title;
- (BOOL) titleIsSet;

- (NSString *) intro;
- (void) setIntro: (NSString *) intro;
- (BOOL) introIsSet;

- (int) eventType;
- (void) setEventType: (int) eventType;
- (BOOL) eventTypeIsSet;

- (TimeStamp) startDate;
- (void) setStartDate: (TimeStamp) startDate;
- (BOOL) startDateIsSet;

- (TimeStamp) expireDate;
- (void) setExpireDate: (TimeStamp) expireDate;
- (BOOL) expireDateIsSet;

- (UserInfo *) initiator;
- (void) setInitiator: (UserInfo *) initiator;
- (BOOL) initiatorIsSet;

- (NSArray *) guestList;
- (void) setGuestList: (NSArray *) guestList;
- (BOOL) guestListIsSet;

- (int64_t) participantAuthedCount;
- (void) setParticipantAuthedCount: (int64_t) participantAuthedCount;
- (BOOL) participantAuthedCountIsSet;

- (int64_t) participantUnauthedCount;
- (void) setParticipantUnauthedCount: (int64_t) participantUnauthedCount;
- (BOOL) participantUnauthedCountIsSet;

- (NSArray *) participantAuthedList;
- (void) setParticipantAuthedList: (NSArray *) participantAuthedList;
- (BOOL) participantAuthedListIsSet;

- (NSArray *) participantUnauthedList;
- (void) setParticipantUnauthedList: (NSArray *) participantUnauthedList;
- (BOOL) participantUnauthedListIsSet;

@end

@interface typeConstants : NSObject {
}
@end

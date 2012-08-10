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


enum UserGender {
  UserGender_Unknown = 0,
  UserGender_Male = 1,
  UserGender_Female = 2
};

enum UserListType {
  UserListType_All = 0,
  UserListType_Recommend = 1,
  UserListType_Nearby = 2,
  UserListType_Following = 3,
  UserListType_Followed = 4,
  UserListType_Friends = 5
};

enum TaskStatus {
  TaskStatus_Removed = 0,
  TaskStatus_Apply = 16,
  TaskStatus_Reject = 32,
  TaskStatus_Close = 64,
  TaskStatus_Open = 128
};

enum TaskSort {
  TaskSort_ByTime = 0,
  TaskSort_ByCount = 1
};

enum TaskListType {
  TaskListType_All = 0,
  TaskListType_Recommend = 2,
  TaskListType_Nearby = 4,
  TaskListType_Following = 8
};

enum MsgType {
  MsgType_All = 0,
  MsgType_System = 1,
  MsgType_Friends = 2,
  MsgType_Stranger = 4,
  MsgType_Unread = 8
};

enum FeedType {
  FeedType_All = 0,
  FeedType_Text = 1,
  FeedType_Article = 2,
  FeedType_Pic = 3,
  FeedType_Activity = 4
};

typedef int64_t timestamp;

@interface AuthRequest : NSObject <NSCoding> {
  int64_t __client_id;
  NSString * __client_secret;

  BOOL __client_id_isset;
  BOOL __client_secret_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=client_id, setter=setClient_id:) int64_t client_id;
@property (nonatomic, retain, getter=client_secret, setter=setClient_secret:) NSString * client_secret;
#endif

- (id) initWithClient_id: (int64_t) client_id client_secret: (NSString *) client_secret;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) client_id;
- (void) setClient_id: (int64_t) client_id;
- (BOOL) client_idIsSet;

- (NSString *) client_secret;
- (void) setClient_secret: (NSString *) client_secret;
- (BOOL) client_secretIsSet;

@end

@interface AuthResponse : NSObject <NSCoding> {
  NSString * __access_token;
  timestamp __expire_in;
  int64_t __user_id;

  BOOL __access_token_isset;
  BOOL __expire_in_isset;
  BOOL __user_id_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, retain, getter=access_token, setter=setAccess_token:) NSString * access_token;
@property (nonatomic, getter=expire_in, setter=setExpire_in:) timestamp expire_in;
@property (nonatomic, getter=user_id, setter=setUser_id:) int64_t user_id;
#endif

- (id) initWithAccess_token: (NSString *) access_token expire_in: (timestamp) expire_in user_id: (int64_t) user_id;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (NSString *) access_token;
- (void) setAccess_token: (NSString *) access_token;
- (BOOL) access_tokenIsSet;

- (timestamp) expire_in;
- (void) setExpire_in: (timestamp) expire_in;
- (BOOL) expire_inIsSet;

- (int64_t) user_id;
- (void) setUser_id: (int64_t) user_id;
- (BOOL) user_idIsSet;

@end

@interface UserBasic : NSObject <NSCoding> {
  int64_t __id;
  NSString * __name;
  int __gender;
  NSString * __org;
  NSString * __job;
  NSString * __avator;

  BOOL __id_isset;
  BOOL __name_isset;
  BOOL __gender_isset;
  BOOL __org_isset;
  BOOL __job_isset;
  BOOL __avator_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=id, setter=setId:) int64_t id;
@property (nonatomic, retain, getter=name, setter=setName:) NSString * name;
@property (nonatomic, getter=gender, setter=setGender:) int gender;
@property (nonatomic, retain, getter=org, setter=setOrg:) NSString * org;
@property (nonatomic, retain, getter=job, setter=setJob:) NSString * job;
@property (nonatomic, retain, getter=avator, setter=setAvator:) NSString * avator;
#endif

- (id) initWithId: (int64_t) id name: (NSString *) name gender: (int) gender org: (NSString *) org job: (NSString *) job avator: (NSString *) avator;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) id;
- (void) setId: (int64_t) id;
- (BOOL) idIsSet;

- (NSString *) name;
- (void) setName: (NSString *) name;
- (BOOL) nameIsSet;

- (int) gender;
- (void) setGender: (int) gender;
- (BOOL) genderIsSet;

- (NSString *) org;
- (void) setOrg: (NSString *) org;
- (BOOL) orgIsSet;

- (NSString *) job;
- (void) setJob: (NSString *) job;
- (BOOL) jobIsSet;

- (NSString *) avator;
- (void) setAvator: (NSString *) avator;
- (BOOL) avatorIsSet;

@end

@interface UserExt : NSObject <NSCoding> {
  NSString * __intro;
  NSArray * __following;
  NSArray * __followed;

  BOOL __intro_isset;
  BOOL __following_isset;
  BOOL __followed_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, retain, getter=intro, setter=setIntro:) NSString * intro;
@property (nonatomic, retain, getter=following, setter=setFollowing:) NSArray * following;
@property (nonatomic, retain, getter=followed, setter=setFollowed:) NSArray * followed;
#endif

- (id) initWithIntro: (NSString *) intro following: (NSArray *) following followed: (NSArray *) followed;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (NSString *) intro;
- (void) setIntro: (NSString *) intro;
- (BOOL) introIsSet;

- (NSArray *) following;
- (void) setFollowing: (NSArray *) following;
- (BOOL) followingIsSet;

- (NSArray *) followed;
- (void) setFollowed: (NSArray *) followed;
- (BOOL) followedIsSet;

@end

@interface User : NSObject <NSCoding> {
  UserBasic * __basic;
  UserExt * __ext;

  BOOL __basic_isset;
  BOOL __ext_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, retain, getter=basic, setter=setBasic:) UserBasic * basic;
@property (nonatomic, retain, getter=ext, setter=setExt:) UserExt * ext;
#endif

- (id) initWithBasic: (UserBasic *) basic ext: (UserExt *) ext;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (UserBasic *) basic;
- (void) setBasic: (UserBasic *) basic;
- (BOOL) basicIsSet;

- (UserExt *) ext;
- (void) setExt: (UserExt *) ext;
- (BOOL) extIsSet;

@end

@interface TaskFilter : NSObject <NSCoding> {
  int __sort;
  int __state;
  int64_t __city_id;
  int64_t __tag_id;
  int64_t __distance;
  int __sponsor_gender;
  int64_t __level;
  BOOL __reward;
  int64_t __reward_cent;

  BOOL __sort_isset;
  BOOL __state_isset;
  BOOL __city_id_isset;
  BOOL __tag_id_isset;
  BOOL __distance_isset;
  BOOL __sponsor_gender_isset;
  BOOL __level_isset;
  BOOL __reward_isset;
  BOOL __reward_cent_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=sort, setter=setSort:) int sort;
@property (nonatomic, getter=state, setter=setState:) int state;
@property (nonatomic, getter=city_id, setter=setCity_id:) int64_t city_id;
@property (nonatomic, getter=tag_id, setter=setTag_id:) int64_t tag_id;
@property (nonatomic, getter=distance, setter=setDistance:) int64_t distance;
@property (nonatomic, getter=sponsor_gender, setter=setSponsor_gender:) int sponsor_gender;
@property (nonatomic, getter=level, setter=setLevel:) int64_t level;
@property (nonatomic, getter=reward, setter=setReward:) BOOL reward;
@property (nonatomic, getter=reward_cent, setter=setReward_cent:) int64_t reward_cent;
#endif

- (id) initWithSort: (int) sort state: (int) state city_id: (int64_t) city_id tag_id: (int64_t) tag_id distance: (int64_t) distance sponsor_gender: (int) sponsor_gender level: (int64_t) level reward: (BOOL) reward reward_cent: (int64_t) reward_cent;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int) sort;
- (void) setSort: (int) sort;
- (BOOL) sortIsSet;

- (int) state;
- (void) setState: (int) state;
- (BOOL) stateIsSet;

- (int64_t) city_id;
- (void) setCity_id: (int64_t) city_id;
- (BOOL) city_idIsSet;

- (int64_t) tag_id;
- (void) setTag_id: (int64_t) tag_id;
- (BOOL) tag_idIsSet;

- (int64_t) distance;
- (void) setDistance: (int64_t) distance;
- (BOOL) distanceIsSet;

- (int) sponsor_gender;
- (void) setSponsor_gender: (int) sponsor_gender;
- (BOOL) sponsor_genderIsSet;

- (int64_t) level;
- (void) setLevel: (int64_t) level;
- (BOOL) levelIsSet;

- (BOOL) reward;
- (void) setReward: (BOOL) reward;
- (BOOL) rewardIsSet;

- (int64_t) reward_cent;
- (void) setReward_cent: (int64_t) reward_cent;
- (BOOL) reward_centIsSet;

@end

@interface TaskBasic : NSObject <NSCoding> {
  int64_t __id;
  NSString * __name;
  int64_t __sponsor;
  int64_t __tag_id;
  NSString * __intro;
  int __state;
  int64_t __area_id;
  int64_t __address_id;
  timestamp __end_time;
  NSString * __reward;
  int64_t __reward_cent;
  int64_t __apply_count;
  int64_t __invite_count;
  int64_t __accept_count;

  BOOL __id_isset;
  BOOL __name_isset;
  BOOL __sponsor_isset;
  BOOL __tag_id_isset;
  BOOL __intro_isset;
  BOOL __state_isset;
  BOOL __area_id_isset;
  BOOL __address_id_isset;
  BOOL __end_time_isset;
  BOOL __reward_isset;
  BOOL __reward_cent_isset;
  BOOL __apply_count_isset;
  BOOL __invite_count_isset;
  BOOL __accept_count_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=id, setter=setId:) int64_t id;
@property (nonatomic, retain, getter=name, setter=setName:) NSString * name;
@property (nonatomic, getter=sponsor, setter=setSponsor:) int64_t sponsor;
@property (nonatomic, getter=tag_id, setter=setTag_id:) int64_t tag_id;
@property (nonatomic, retain, getter=intro, setter=setIntro:) NSString * intro;
@property (nonatomic, getter=state, setter=setState:) int state;
@property (nonatomic, getter=area_id, setter=setArea_id:) int64_t area_id;
@property (nonatomic, getter=address_id, setter=setAddress_id:) int64_t address_id;
@property (nonatomic, getter=end_time, setter=setEnd_time:) timestamp end_time;
@property (nonatomic, retain, getter=reward, setter=setReward:) NSString * reward;
@property (nonatomic, getter=reward_cent, setter=setReward_cent:) int64_t reward_cent;
@property (nonatomic, getter=apply_count, setter=setApply_count:) int64_t apply_count;
@property (nonatomic, getter=invite_count, setter=setInvite_count:) int64_t invite_count;
@property (nonatomic, getter=accept_count, setter=setAccept_count:) int64_t accept_count;
#endif

- (id) initWithId: (int64_t) id name: (NSString *) name sponsor: (int64_t) sponsor tag_id: (int64_t) tag_id intro: (NSString *) intro state: (int) state area_id: (int64_t) area_id address_id: (int64_t) address_id end_time: (timestamp) end_time reward: (NSString *) reward reward_cent: (int64_t) reward_cent apply_count: (int64_t) apply_count invite_count: (int64_t) invite_count accept_count: (int64_t) accept_count;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) id;
- (void) setId: (int64_t) id;
- (BOOL) idIsSet;

- (NSString *) name;
- (void) setName: (NSString *) name;
- (BOOL) nameIsSet;

- (int64_t) sponsor;
- (void) setSponsor: (int64_t) sponsor;
- (BOOL) sponsorIsSet;

- (int64_t) tag_id;
- (void) setTag_id: (int64_t) tag_id;
- (BOOL) tag_idIsSet;

- (NSString *) intro;
- (void) setIntro: (NSString *) intro;
- (BOOL) introIsSet;

- (int) state;
- (void) setState: (int) state;
- (BOOL) stateIsSet;

- (int64_t) area_id;
- (void) setArea_id: (int64_t) area_id;
- (BOOL) area_idIsSet;

- (int64_t) address_id;
- (void) setAddress_id: (int64_t) address_id;
- (BOOL) address_idIsSet;

- (timestamp) end_time;
- (void) setEnd_time: (timestamp) end_time;
- (BOOL) end_timeIsSet;

- (NSString *) reward;
- (void) setReward: (NSString *) reward;
- (BOOL) rewardIsSet;

- (int64_t) reward_cent;
- (void) setReward_cent: (int64_t) reward_cent;
- (BOOL) reward_centIsSet;

- (int64_t) apply_count;
- (void) setApply_count: (int64_t) apply_count;
- (BOOL) apply_countIsSet;

- (int64_t) invite_count;
- (void) setInvite_count: (int64_t) invite_count;
- (BOOL) invite_countIsSet;

- (int64_t) accept_count;
- (void) setAccept_count: (int64_t) accept_count;
- (BOOL) accept_countIsSet;

@end

@interface TaskExt : NSObject <NSCoding> {
  NSArray * __applied;
  NSArray * __invited;
  NSArray * __accepted;

  BOOL __applied_isset;
  BOOL __invited_isset;
  BOOL __accepted_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, retain, getter=applied, setter=setApplied:) NSArray * applied;
@property (nonatomic, retain, getter=invited, setter=setInvited:) NSArray * invited;
@property (nonatomic, retain, getter=accepted, setter=setAccepted:) NSArray * accepted;
#endif

- (id) initWithApplied: (NSArray *) applied invited: (NSArray *) invited accepted: (NSArray *) accepted;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (NSArray *) applied;
- (void) setApplied: (NSArray *) applied;
- (BOOL) appliedIsSet;

- (NSArray *) invited;
- (void) setInvited: (NSArray *) invited;
- (BOOL) invitedIsSet;

- (NSArray *) accepted;
- (void) setAccepted: (NSArray *) accepted;
- (BOOL) acceptedIsSet;

@end

@interface Task : NSObject <NSCoding> {
  TaskBasic * __basic;
  TaskExt * __ext;

  BOOL __basic_isset;
  BOOL __ext_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, retain, getter=basic, setter=setBasic:) TaskBasic * basic;
@property (nonatomic, retain, getter=ext, setter=setExt:) TaskExt * ext;
#endif

- (id) initWithBasic: (TaskBasic *) basic ext: (TaskExt *) ext;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (TaskBasic *) basic;
- (void) setBasic: (TaskBasic *) basic;
- (BOOL) basicIsSet;

- (TaskExt *) ext;
- (void) setExt: (TaskExt *) ext;
- (BOOL) extIsSet;

@end

@interface TaskListRequest : NSObject <NSCoding> {
  int64_t __lastid;
  int64_t __length;
  int __type;

  BOOL __lastid_isset;
  BOOL __length_isset;
  BOOL __type_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=lastid, setter=setLastid:) int64_t lastid;
@property (nonatomic, getter=length, setter=setLength:) int64_t length;
@property (nonatomic, getter=type, setter=setType:) int type;
#endif

- (id) initWithLastid: (int64_t) lastid length: (int64_t) length type: (int) type;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) lastid;
- (void) setLastid: (int64_t) lastid;
- (BOOL) lastidIsSet;

- (int64_t) length;
- (void) setLength: (int64_t) length;
- (BOOL) lengthIsSet;

- (int) type;
- (void) setType: (int) type;
- (BOOL) typeIsSet;

@end

@interface Msg : NSObject <NSCoding> {
  int64_t __sender;
  timestamp __time;
  NSString * __text;
  int __type;

  BOOL __sender_isset;
  BOOL __time_isset;
  BOOL __text_isset;
  BOOL __type_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=sender, setter=setSender:) int64_t sender;
@property (nonatomic, getter=time, setter=setTime:) timestamp time;
@property (nonatomic, retain, getter=text, setter=setText:) NSString * text;
@property (nonatomic, getter=type, setter=setType:) int type;
#endif

- (id) initWithSender: (int64_t) sender time: (timestamp) time text: (NSString *) text type: (int) type;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) sender;
- (void) setSender: (int64_t) sender;
- (BOOL) senderIsSet;

- (timestamp) time;
- (void) setTime: (timestamp) time;
- (BOOL) timeIsSet;

- (NSString *) text;
- (void) setText: (NSString *) text;
- (BOOL) textIsSet;

- (int) type;
- (void) setType: (int) type;
- (BOOL) typeIsSet;

@end

@interface FeedMsg : NSObject <NSCoding> {
  NSString * __sender;
  timestamp __time;
  int __type;
  NSString * __content;

  BOOL __sender_isset;
  BOOL __time_isset;
  BOOL __type_isset;
  BOOL __content_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, retain, getter=sender, setter=setSender:) NSString * sender;
@property (nonatomic, getter=time, setter=setTime:) timestamp time;
@property (nonatomic, getter=type, setter=setType:) int type;
@property (nonatomic, retain, getter=content, setter=setContent:) NSString * content;
#endif

- (id) initWithSender: (NSString *) sender time: (timestamp) time type: (int) type content: (NSString *) content;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (NSString *) sender;
- (void) setSender: (NSString *) sender;
- (BOOL) senderIsSet;

- (timestamp) time;
- (void) setTime: (timestamp) time;
- (BOOL) timeIsSet;

- (int) type;
- (void) setType: (int) type;
- (BOOL) typeIsSet;

- (NSString *) content;
- (void) setContent: (NSString *) content;
- (BOOL) contentIsSet;

@end

@interface Summary : NSObject <NSCoding> {
  int64_t __unread_msg_num;
  int64_t __following_num;
  int64_t __followed_num;

  BOOL __unread_msg_num_isset;
  BOOL __following_num_isset;
  BOOL __followed_num_isset;
}

#if TARGET_OS_IPHONE || (MAC_OS_X_VERSION_MAX_ALLOWED >= MAC_OS_X_VERSION_10_5)
@property (nonatomic, getter=unread_msg_num, setter=setUnread_msg_num:) int64_t unread_msg_num;
@property (nonatomic, getter=following_num, setter=setFollowing_num:) int64_t following_num;
@property (nonatomic, getter=followed_num, setter=setFollowed_num:) int64_t followed_num;
#endif

- (id) initWithUnread_msg_num: (int64_t) unread_msg_num following_num: (int64_t) following_num followed_num: (int64_t) followed_num;

- (void) read: (id <TProtocol>) inProtocol;
- (void) write: (id <TProtocol>) outProtocol;

- (int64_t) unread_msg_num;
- (void) setUnread_msg_num: (int64_t) unread_msg_num;
- (BOOL) unread_msg_numIsSet;

- (int64_t) following_num;
- (void) setFollowing_num: (int64_t) following_num;
- (BOOL) following_numIsSet;

- (int64_t) followed_num;
- (void) setFollowed_num: (int64_t) followed_num;
- (BOOL) followed_numIsSet;

@end

@interface typeConstants : NSObject {
}
@end

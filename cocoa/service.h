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

#import "exception.h"
#import "type.h"

@protocol Sns <NSObject>
- (AuthResponse *) login_by_mail: (AuthRequestMail *) auth_request_mail;  // throws TException
- (AuthResponse *) login_by_oauth: (NSString *) client_key : (NSString *) client_secret : (NSString *) mail;  // throws TException
- (AuthResponse *) login_by_oauth2: (NSString *) client_key : (NSString *) client_secret : (NSString *) mail;  // throws TException
- (void) logout: (NSString *) access_token;  // throws TException
- (UserInfo *) user_info_get: (NSString *) access_token : (int64_t) id;  // throws TException
- (UserInfo *) user_info_set: (NSString *) access_token : (UserInfo *) user_info;  // throws TException
- (Task *) task_get: (NSString *) access_token : (int64_t) id;  // throws TException
- (int64_t) task_new: (NSString *) access_token : (Task *) task;  // throws TException
- (void) task_apply: (NSString *) access_token : (int64_t) task_id;  // throws TException
- (void) task_reject: (NSString *) access_token : (int64_t) user_id;  // throws TException
- (void) task_accept: (NSString *) access_token : (int64_t) user_id;  // throws TException
@end

@interface SnsClient : NSObject <Sns> {
  id <TProtocol> inProtocol;
  id <TProtocol> outProtocol;
}
- (id) initWithProtocol: (id <TProtocol>) protocol;
- (id) initWithInProtocol: (id <TProtocol>) inProtocol outProtocol: (id <TProtocol>) outProtocol;
@end

@interface SnsProcessor : NSObject <TProcessor> {
  id <Sns> mService;
  NSDictionary * mMethodMap;
}
- (id) initWithSns: (id <Sns>) service;
- (id<Sns>) service;
@end

@interface serviceConstants : NSObject {
}
@end

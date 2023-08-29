//
//  KNYCMSClient.h
//  Metrics
//
//  Copyright (c) 2018 Kony. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "KNYMetricsService.h"
#import "KNYCMSDefaultPersistentStore.h"

#if ! __has_feature(objc_arc)
#error This file must be compiled with ARC. Either turn on ARC for the project or use -fobjc-arc flag
#endif

/**
 KNYClient
 */
@interface KNYCMSClient : NSObject

@property (nonatomic, readonly) KNYCMSDefaultPersistentStore* dataStore;

/**
 
 @return Returns the instance of the singleton
 */
+ (instancetype)sharedClient;

- (instancetype)init;

/**
 init using service configuration
 @param serviceDoc service configuration of your application.
 @throws KNYException if appConfig is invalid.
 example of service doc:
 
 NSDictionary *dict = @{
 @"name":@"test",
 @"baseId":@"testbaseId",
 @"reportingsvc": @{
 @"custom": @"https://nut007.konycloud.com/services/CMS",
 @"session": @"https://nut007.konycloud.com/services/IST"
 } };
 
 name, baseId  and reportingsvc are mandatory parameters as part of service config.
 */
- (void)initWithServiceDoc:(NSDictionary *)serviceDoc;

/**
 Authenticates you with the Kony Mobile Fabric Service. The appKey, appSecret and serviceURLString are available in the Kony Mobile Fabric Console.
 
 @param appKey     The appkey for your application.
 @param appSecret  The appsecret for your application.
 @param serviceDoc  service configuration for your application.
 @throws KNYException if appConfig is invalid.
 
 example of service doc:
 
 NSDictionary *dict = @{
 @"name":@"test",
 @"baseId":@"testbaseId",
 @"reportingsvc": @{
    @"custom": @"https://nut007.konycloud.com/services/CMS",
    @"session": @"https://nut007.konycloud.com/services/IST"
 } };
 name, baseId and reportingsvc are mandatory parameters as part of service config.
 */
- (void)initWithAppkey:(NSString*)appKey
             appSecret:(NSString*)appSecret
            serviceDoc:(NSDictionary*)serviceDoc;

@property (nonatomic, readonly) NSString *appKey;
@property (nonatomic, readonly) NSString *appSecret;
@property (nonatomic, readonly) NSString *serviceURLString;

/**
 returns the metricsService instance.
 */
- (KNYMetricsService*)getMetricsService;

/**
 set client params (used for konystudio apps using MF backend)
 @param clientParams client params
 */
- (void)setClientParams:(NSDictionary*)clientParams;

/**
 get the sdktype
 @return the sdk type
 */
+ (NSString*)sdkType;

/**
 get the sdkVersion
 @return the sdk version
 */
+ (NSString*)sdkVersion;


@end

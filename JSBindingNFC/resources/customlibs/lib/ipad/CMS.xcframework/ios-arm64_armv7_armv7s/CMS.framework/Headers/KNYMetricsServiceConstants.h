//
//  KNYMetricsConstants.h
//  KMBaasClient
//
//  Created by KH200 on 31/03/15.
//  Copyright (c) 2015 Kony. All rights reserved.
//
#import <Foundation/Foundation.h>

#ifndef KMBaasClient_KNYMetricsConstants_h
#define KMBaasClient_KNYMetricsConstants_h

typedef NS_ENUM(NSUInteger, KNYEventType) {
    KNYEventTypeFormEntry = 0,
    KNYEventTypeFormExit = 1,
    KNYEventTypeTouch = 2,
    KNYEventTypeServiceRequest = 3,
    KNYEventTypeServiceResponse = 4,
    KNYEventTypeGesture = 5,
    KNYEventTypeOrientation = 6,
    KNYEventTypeError = 7,
    KNYEventTypeHandledException = 8,
    KNYEventTypeCrash = 9,
    KNYEventTypeCustom = 10,
    KNYEventTypeServiceCall = 11,
    KNYEventTypeAppTransition = 12,
    KNYEventTypeAppLoad = 13,
    KNYEventTypeComponent = 14
};

typedef NS_ENUM(NSUInteger, KNYEventConfigType)
{
    KNYEventConfigTypeBuffer,
    KNYEventConfigTypeInstant
};
#endif

//os version
#define IOS5 50000
#define IOS6 60000
#define IOS7 70000
#define IOS8 80000

/** iPhone/ ipod /iPad device modals */
#define DEVICEMODEL_IPHONE                @"iPhone"
#define DEVICEMODEL_IPHONE_3G            @"3G iPhone"
#define DEVICEMODEL_IPHONE_3GS            @"3GS iPhone"
#define    DEVICEMODEL_IPHONE_4G            @"4G iPhone"
#define DEVICEMODEL_IPHONE_4GS          @"4GS iPhone"
#define DEVICEMODEL_IPHONE_5G           @"5G iPhone"
#define    DEVICEMODEL_IPHONE_5C           @"iPhone 5C"
#define    DEVICEMODEL_IPHONE_5S           @"iPhone 5S"
#define    DEVICEMODEL_IPHONE_6_PLUS       @"iPhone 6 Plus"
#define    DEVICEMODEL_IPHONE_6            @"iPhone 6"
#define    DEVICEMODEL_IPHONE_6S_PLUS      @"iPhone 6S Plus"
#define    DEVICEMODEL_IPHONE_SE           @"iPhone SE"
#define    DEVICEMODEL_IPHONE_7            @"iPhone 7"
#define    DEVICEMODEL_IPHONE_7_PLUS       @"iPhone 7 Plus"
#define    DEVICEMODEL_IPHONE_8            @"iPhone 8"
#define    DEVICEMODEL_IPHONE_8_PLUS       @"iPhone 8 Plus"
#define    DEVICEMODEL_IPHONE_10           @"iPhone X"

#define    DEVICEMODEL_IPOD                @"1st Gen iPod"
#define    DEVICEMODEL_IPOD_2GEN            @"2nd Gen iPod"
#define    DEVICEMODEL_IPOD_3GEN            @"3rd Gen iPod"
#define    DEVICEMODEL_IPOD_4GEN            @"4th Gen iPod"
#define    DEVICEMODEL_IPOD_5GEN            @"5th Gen iPod"
#define    DEVICEMODEL_IPOD_6GEN            @"6th Gen iPod"
#define    DEVICEMODEL_IPHONE_SIMLUATOR    @"iPhone Simulator"
#define    DEVICEMODEL_IPAD_SIMLUATOR      @"iPad Simulator"
#define DEVICEMODEL_IPAD                @"iPad"
#define DEVICEMODEL_IPAD_2              @"iPad 2"
#define DEVICEMODEL_IPAD_3              @"iPad 3"
#define DEVICEMODEL_IPAD_4              @"iPad 4"
#define DEVICEMODEL_IPAD_MINI           @"iPad Mini"
#define DEVICEMODEL_IPAD_MINI_2         @"iPad Mini 2"
#define DEVICEMODEL_IPAD_MINI_3         @"iPad Mini 3"
#define DEVICEMODEL_IPAD_AIR            @"iPad Air"
#define DEVICEMODEL_IPAD_AIR_2          @"iPad Air 2"
#define DEVICEMODEL_IPAD_PRO            @"iPad Pro"
#define DEVICEMODEL_IPAD_PRO_9_7        @"iPad Pro 9.7"
#define DEVICEMODEL_IPAD_PRO_12_9       @"iPad Pro 12.9"
#define DEVICEMODEL_IPAD_PRO_10_5       @"iPad Pro 10.5"
#define DEVICEMODEL_IPAD_5GEN           @"iPad 5th Gen"
#define DEVICEMODEL_UNKNOWN             @"unknown"

// reporting parameter to server
FOUNDATION_EXPORT NSString *const kConfigReportingCustomURLKey;
FOUNDATION_EXPORT NSString *const kConfigReportingSessionURLKey;
FOUNDATION_EXPORT NSString *const kAppNameKey;
FOUNDATION_EXPORT NSString *const kAppIdKey;
FOUNDATION_EXPORT NSString *const kAppVersionKey;
FOUNDATION_EXPORT NSString* const METRICS_INTERACTIVE_SESSION_TYPE;

// request headers
FOUNDATION_EXPORT NSString *const X_KONY_REQUEST_ID;
FOUNDATION_EXPORT NSString *const CONTENT_TYPE_FORM_URL_ENCODED;
FOUNDATION_EXPORT NSString *const CONTENT_TYPE_KEY;

// cms database schema constants
FOUNDATION_EXPORT NSString* const DATABASE_NAME;
FOUNDATION_EXPORT NSString* const CMS_TABLE_NAME;
FOUNDATION_EXPORT NSString* const EVENT_ID;
FOUNDATION_EXPORT NSString* const EVENT_JSON;
FOUNDATION_EXPORT NSString* const EVENT_REQUEST_ID;
FOUNDATION_EXPORT NSString* const METRICS_DATABASE_DIR_NAME;
FOUNDATION_EXPORT NSString* const ORDERBY_ASCENDING;

//network related constants
FOUNDATION_EXPORT NSString* const METRICS_OPSTATUS;
FOUNDATION_EXPORT NSInteger const SERVER_RESPONSE_TIME_OUT_STATUS_CODE;
FOUNDATION_EXPORT NSInteger const OPSTATUS_SUCCESS_CODE;
FOUNDATION_EXPORT NSInteger const HTTP_STATUS_SUCCESS_CODE;
FOUNDATION_EXPORT NSString* const EVENT_SUBTYPE_PATTERN_FOR_IMAGES;

@interface KNYMetricsServiceConstants : NSObject
@end


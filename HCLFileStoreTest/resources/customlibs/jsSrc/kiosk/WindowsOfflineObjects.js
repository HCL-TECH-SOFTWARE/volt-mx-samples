var WindowsOfflineObjects = WindowsOfflineObjects || { };

WindowsOfflineObjects.statichelper_getArguments = function (arg2) 
{

var result = '{';

for (var i = 0; i < arg2.length; ++i) 
{
     if (i > 0)
       result += ', ';

     var element = arg2[i];

     result += jetro.variant.format( element );
}

result += '}';

return result;
}
WindowsOfflineObjects.setToken = function ()
{
    return WindowsOfflineObjects.setToken_variadic(arguments);
}
WindowsOfflineObjects.setToken_variadic = function (arg)
{
    var formattedArg = WindowsOfflineObjects.statichelper_getArguments(arg);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.setToken_variadic'
        + ' ' + formattedArg
    );

    return jetro.returnValue;
}

WindowsOfflineObjects.setup = function ()
{
    return WindowsOfflineObjects.setup_variadic(arguments);
}
WindowsOfflineObjects.setup_variadic = function (arg)
{
    var formattedArg = WindowsOfflineObjects.statichelper_getArguments(arg);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.setup_variadic'
        + ' ' + formattedArg
    );

    return jetro.returnValue;
}

WindowsOfflineObjects.drop = function ()
{
    return WindowsOfflineObjects.drop_variadic(arguments);
}
WindowsOfflineObjects.drop_variadic = function (arg)
{
    var formattedArg = WindowsOfflineObjects.statichelper_getArguments(arg);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.drop_variadic'
        + ' ' + formattedArg
    );

    return jetro.returnValue;
}

WindowsOfflineObjects.rollback = function ()
{
    return WindowsOfflineObjects.rollback_variadic(arguments);
}
WindowsOfflineObjects.rollback_variadic = function (arg)
{
    var formattedArg = WindowsOfflineObjects.statichelper_getArguments(arg);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.rollback_variadic'
        + ' ' + formattedArg
    );

    return jetro.returnValue;
}

WindowsOfflineObjects.reset = function ()
{
    return WindowsOfflineObjects.reset_variadic(arguments);
}
WindowsOfflineObjects.reset_variadic = function (arg)
{
    var formattedArg = WindowsOfflineObjects.statichelper_getArguments(arg);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.reset_variadic'
        + ' ' + formattedArg
    );

    return jetro.returnValue;
}

var WindowsOfflineObjects = WindowsOfflineObjects || { };
WindowsOfflineObjects.OfflineSDKObject = WindowsOfflineObjects.OfflineSDKObject || { };

WindowsOfflineObjects.OfflineSDKObject = function()
{
    this.nativeObjectUid = WindowsOfflineObjects.OfflineSDKObject.static_createNativeObject();
    if( this.nativeObjectUid < 0 )
        throw "FFI: Failed to create object of class 'OfflineObjects.FFI.ObjectSyncFFI' in Assembly 'offlineobjects.zip'";
}
WindowsOfflineObjects.OfflineSDKObject.static_createNativeObject = function ()
{
    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.OfflineSDKObject.static_createNativeObject'
    );

    return jetro.returnValue;
}
WindowsOfflineObjects.statichelper_getArguments = function (arg2) 
{

var result = '{';

for (var i = 0; i < arg2.length; ++i) 
{
     if (i > 0)
       result += ', ';

     var element = arg2[i];

     result += jetro.variant.format( element );
}

result += '}';

return result;
}
WindowsOfflineObjects.OfflineSDKObject.prototype.create = function ()
{
    return WindowsOfflineObjects.OfflineSDKObject.static_create( this.nativeObjectUid, arguments );
}
WindowsOfflineObjects.OfflineSDKObject.static_create = function (arg1, arg2)
{
    var formattedArg1 = arg1.toString();
    var formattedArg2 = WindowsOfflineObjects.statichelper_getArguments(arg2);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.OfflineSDKObject.static_create'
        + ' ' + formattedArg1
        + ' ' + formattedArg2
    );

    return jetro.returnValue;
}
WindowsOfflineObjects.OfflineSDKObject.prototype.updateByPK = function ()
{
    return WindowsOfflineObjects.OfflineSDKObject.static_updateByPK( this.nativeObjectUid, arguments );
}
WindowsOfflineObjects.OfflineSDKObject.static_updateByPK = function (arg1, arg2)
{
    var formattedArg1 = arg1.toString();
    var formattedArg2 = WindowsOfflineObjects.statichelper_getArguments(arg2);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.OfflineSDKObject.static_updateByPK'
        + ' ' + formattedArg1
        + ' ' + formattedArg2
    );

    return jetro.returnValue;
}
WindowsOfflineObjects.OfflineSDKObject.prototype.get = function ()
{
    return WindowsOfflineObjects.OfflineSDKObject.static_get( this.nativeObjectUid, arguments );
}
WindowsOfflineObjects.OfflineSDKObject.static_get = function (arg1, arg2)
{
    var formattedArg1 = arg1.toString();
    var formattedArg2 = WindowsOfflineObjects.statichelper_getArguments(arg2);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.OfflineSDKObject.static_get'
        + ' ' + formattedArg1
        + ' ' + formattedArg2
    );

    return jetro.returnValue;
}
WindowsOfflineObjects.OfflineSDKObject.prototype.deleteByPK = function ()
{
    return WindowsOfflineObjects.OfflineSDKObject.static_deleteByPK( this.nativeObjectUid, arguments );
}
WindowsOfflineObjects.OfflineSDKObject.static_deleteByPK = function (arg1, arg2)
{
    var formattedArg1 = arg1.toString();
    var formattedArg2 = WindowsOfflineObjects.statichelper_getArguments(arg2);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.OfflineSDKObject.static_deleteByPK'
        + ' ' + formattedArg1
        + ' ' + formattedArg2
    );

    return jetro.returnValue;
}
WindowsOfflineObjects.OfflineSDKObject.prototype.startSync = function ()
{
    return WindowsOfflineObjects.OfflineSDKObject.static_startSync( this.nativeObjectUid, arguments );
}
WindowsOfflineObjects.OfflineSDKObject.static_startSync = function (arg1, arg2)
{
    var formattedArg1 = arg1.toString();
    var formattedArg2 = WindowsOfflineObjects.statichelper_getArguments(arg2);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.OfflineSDKObject.static_startSync'
        + ' ' + formattedArg1
        + ' ' + formattedArg2
    );

    return jetro.returnValue;
}
WindowsOfflineObjects.OfflineSDKObject.prototype.rollback = function ()
{
    return WindowsOfflineObjects.OfflineSDKObject.static_rollback( this.nativeObjectUid, arguments );
}
WindowsOfflineObjects.OfflineSDKObject.static_rollback = function (arg1, arg2)
{
    var formattedArg1 = arg1.toString();
    var formattedArg2 = WindowsOfflineObjects.statichelper_getArguments(arg2);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.OfflineSDKObject.static_rollback'
        + ' ' + formattedArg1
        + ' ' + formattedArg2
    );

    return jetro.returnValue;
}

var WindowsOfflineObjects = WindowsOfflineObjects || { };
WindowsOfflineObjects.OfflineSDKObjectService = WindowsOfflineObjects.OfflineSDKObjectService || { };

WindowsOfflineObjects.OfflineSDKObjectService = function()
{
    this.nativeObjectUid = WindowsOfflineObjects.OfflineSDKObjectService.static_createNativeObject();
    if( this.nativeObjectUid < 0 )
        throw "FFI: Failed to create object of class 'OfflineObjects.FFI.ObjectServiceSyncFFI' in Assembly 'offlineobjects.zip'";
}
WindowsOfflineObjects.OfflineSDKObjectService.static_createNativeObject = function ()
{
    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.OfflineSDKObjectService.static_createNativeObject'
    );

    return jetro.returnValue;
}
WindowsOfflineObjects.statichelper_getArguments = function (arg2) 
{

var result = '{';

for (var i = 0; i < arg2.length; ++i) 
{
     if (i > 0)
       result += ', ';

     var element = arg2[i];

     result += jetro.variant.format( element );
}

result += '}';

return result;
}
WindowsOfflineObjects.OfflineSDKObjectService.prototype.startSync = function ()
{
    return WindowsOfflineObjects.OfflineSDKObjectService.static_startSync( this.nativeObjectUid, arguments );
}
WindowsOfflineObjects.OfflineSDKObjectService.static_startSync = function (arg1, arg2)
{
    var formattedArg1 = arg1.toString();
    var formattedArg2 = WindowsOfflineObjects.statichelper_getArguments(arg2);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.OfflineSDKObjectService.static_startSync'
        + ' ' + formattedArg1
        + ' ' + formattedArg2
    );

    return jetro.returnValue;
}
WindowsOfflineObjects.OfflineSDKObjectService.prototype.rollback = function ()
{
    return WindowsOfflineObjects.OfflineSDKObjectService.static_rollback( this.nativeObjectUid, arguments );
}
WindowsOfflineObjects.OfflineSDKObjectService.static_rollback = function (arg1, arg2)
{
    var formattedArg1 = arg1.toString();
    var formattedArg2 = WindowsOfflineObjects.statichelper_getArguments(arg2);

    window.external.notify( 'JetroCallFunction WindowsOfflineObjects.OfflineSDKObjectService.static_rollback'
        + ' ' + formattedArg1
        + ' ' + formattedArg2
    );

    return jetro.returnValue;
}


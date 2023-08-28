/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
function AS_Form_a5fc84eea94a4b999fb48e1f176d408b(eventobject) {
    var self = this;

    function INVOKE_OBJECT_SERVICE_ide_preShow_fa065fb4b629444691d5e0d6f3a46265_Callback(application) {
        self.showAppCards.call(this, application);
    }
    function INVOKE_OBJECT_SERVICE_ide_preShow_b9f488a75b104abc88822691f9fd4492_Callback(userpreference) {
        if (userpreference.httpStatusCode == 401) {
            var ntf = new voltmx.mvc.Navigation("Login");
            ntf.navigate();
        } else {
            self.getUserPreference.call(this, userpreference);
            if (application_inputparam == undefined) {
                var application_inputparam = {};
            }
            application_inputparam["serviceID"] = "JACenter$application$get";
            application_inputparam["options"] = {
                "access": "online",
                "CRUD_TYPE": "get"
            };
            var odataParams = [];
            odataParams.push("$filter=" + "((SoftDeleteFlag ne true) or (SoftDeleteFlag eq null)) and (owner eq " + username + ")");
            application_inputparam["options"]["odataurl"] = odataParams.join("&");
            var application_httpheaders = {};
            application_inputparam["httpheaders"] = application_httpheaders;
            var application_httpconfigs = {};
            application_inputparam["httpconfig"] = application_httpconfigs;
            JACenter$application$get = mfobjectsecureinvokerasync(application_inputparam, "JACenter", "application", INVOKE_OBJECT_SERVICE_ide_preShow_fa065fb4b629444691d5e0d6f3a46265_Callback);
            self.view.MainContainer.HeaderBar.userDisplayName.text = userProfile.displayname;
        }
    }
    try {
        username = userProfile.userid;
    } catch (e) {
        username = "";
    }
    if (userpreference_inputparam == undefined) {
        var userpreference_inputparam = {};
    }
    userpreference_inputparam["serviceID"] = "JACenter$userpreference$get";
    userpreference_inputparam["options"] = {
        "access": "online",
        "CRUD_TYPE": "get"
    };
    var odataParams = [];
    odataParams.push("$filter=" + "((SoftDeleteFlag ne true) or (SoftDeleteFlag eq null)) and (userid eq " + username + ")");
    userpreference_inputparam["options"]["odataurl"] = odataParams.join("&");
    var userpreference_httpheaders = {};
    userpreference_inputparam["httpheaders"] = userpreference_httpheaders;
    var userpreference_httpconfigs = {};
    userpreference_inputparam["httpconfig"] = userpreference_httpconfigs;
    JACenter$userpreference$get = mfobjectsecureinvokerasync(userpreference_inputparam, "JACenter", "userpreference", INVOKE_OBJECT_SERVICE_ide_preShow_b9f488a75b104abc88822691f9fd4492_Callback);
}
/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
function AS_Button_a9fbc5d522244de5bd8d771a0a53bbed(eventobject) {
    var self = this;

    function INVOKE_OBJECT_SERVICE_ide_onClick_b682e9b251d34723a3c8da3b4241fbbf_Callback(user) {
        errorFlag = false;
        self.getUserRecord.call(this, user);
        if (errorFlag == false) {
            var ntf = new voltmx.mvc.Navigation("Main");
            ntf.navigate();
        } else {
            self.clearLoginForm.call(this);
        }
        voltmx.application.exit();
    }
    function INVOKE_IDENTITY_SERVICE_ide_onClick_c16ca81d82604e3f85412676b9a63f54_Success(response) {
        username = self.view.LoginForm.tbxUsername.text;
        if (user_inputparam == undefined) {
            var user_inputparam = {};
        }
        user_inputparam["serviceID"] = "JACenter$user$get";
        user_inputparam["options"] = {
            "access": "online",
            "CRUD_TYPE": "get"
        };
        var odataParams = [];
        odataParams.push("$filter=" + "((SoftDeleteFlag ne true) or (SoftDeleteFlag eq null)) and (userid eq " + username + ")");
        user_inputparam["options"]["odataurl"] = odataParams.join("&");
        var user_httpheaders = {};
        user_inputparam["httpheaders"] = user_httpheaders;
        var user_httpconfigs = {};
        user_inputparam["httpconfig"] = user_httpconfigs;
        JACenter$user$get = mfobjectsecureinvokerasync(user_inputparam, "JACenter", "user", INVOKE_OBJECT_SERVICE_ide_onClick_b682e9b251d34723a3c8da3b4241fbbf_Callback);
    }
    function INVOKE_IDENTITY_SERVICE_ide_onClick_c16ca81d82604e3f85412676b9a63f54_Failure(error) {
        function SHOW_ALERT_ide_onClick_acd3f4c0f3044f0eaa1b79c628c20607_Callback() {
            SHOW_ALERT_ide_onClick_acd3f4c0f3044f0eaa1b79c628c20607_True();
        }
        voltmx.ui.Alert({
            "alertType": constants.ALERT_TYPE_ERROR,
            "message": "Login failed!  Invalid username or password.",
            "alertHandler": SHOW_ALERT_ide_onClick_acd3f4c0f3044f0eaa1b79c628c20607_Callback
        }, {
            "iconPosition": constants.ALERT_ICON_POSITION_LEFT
        });
    }
    function SHOW_ALERT_ide_onClick_acd3f4c0f3044f0eaa1b79c628c20607_True() {}
    if (login_inputparam == undefined) {
        var login_inputparam = {};
    }
    login_inputparam["serviceID"] = "UserAuthentication$login";
    login_inputparam["operation"] = "login";
    login_inputparam["userid"] = self.view.LoginForm.tbxUsername.text;
    login_inputparam["password"] = self.view.LoginForm.tbxPassword.text;
    UserAuthentication$login = mfidentityserviceinvoker("UserAuthentication", login_inputparam, INVOKE_IDENTITY_SERVICE_ide_onClick_c16ca81d82604e3f85412676b9a63f54_Success, INVOKE_IDENTITY_SERVICE_ide_onClick_c16ca81d82604e3f85412676b9a63f54_Failure);
}
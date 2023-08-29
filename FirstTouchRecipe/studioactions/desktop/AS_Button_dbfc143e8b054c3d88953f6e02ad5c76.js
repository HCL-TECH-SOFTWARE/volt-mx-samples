/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
function AS_Button_dbfc143e8b054c3d88953f6e02ad5c76(eventobject) {
    var self = this;

    function INVOKE_OBJECT_SERVICE_ide_onClick_c5c3a97feebf4c06a9654a7aba528feb_Callback(user) {
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
    function INVOKE_IDENTITY_SERVICE_ide_onClick_bb5215f47f314b459fb3889106389907_Success(response) {
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
        JACenter$user$get = mfobjectsecureinvokerasync(user_inputparam, "JACenter", "user", INVOKE_OBJECT_SERVICE_ide_onClick_c5c3a97feebf4c06a9654a7aba528feb_Callback);
    }
    function INVOKE_IDENTITY_SERVICE_ide_onClick_bb5215f47f314b459fb3889106389907_Failure(error) {
        function SHOW_ALERT_ide_onClick_a4598f151bd847349f9e449858efdf93_Callback() {
            SHOW_ALERT_ide_onClick_a4598f151bd847349f9e449858efdf93_True();
        }
        voltmx.ui.Alert({
            "alertType": constants.ALERT_TYPE_ERROR,
            "message": "Login failed!  Invalid username or password.",
            "alertHandler": SHOW_ALERT_ide_onClick_a4598f151bd847349f9e449858efdf93_Callback
        }, {
            "iconPosition": constants.ALERT_ICON_POSITION_LEFT
        });
    }
    function SHOW_ALERT_ide_onClick_a4598f151bd847349f9e449858efdf93_True() {}
    if (login_inputparam == undefined) {
        var login_inputparam = {};
    }
    login_inputparam["serviceID"] = "UserAuthentication$login";
    login_inputparam["operation"] = "login";
    login_inputparam["userid"] = self.view.LoginForm.tbxUsername.text;
    login_inputparam["password"] = self.view.LoginForm.tbxPassword.text;
    UserAuthentication$login = mfidentityserviceinvoker("UserAuthentication", login_inputparam, INVOKE_IDENTITY_SERVICE_ide_onClick_bb5215f47f314b459fb3889106389907_Success, INVOKE_IDENTITY_SERVICE_ide_onClick_bb5215f47f314b459fb3889106389907_Failure);
}
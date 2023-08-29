/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
function AS_Button_e2eb12f65f454c22b2c461babaab9136(eventobject) {
    var self = this;

    function INVOKE_OBJECT_SERVICE_ide_onClick_b30173af1efd482d8b04ccedb05104c5_Callback(user) {
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
    function INVOKE_IDENTITY_SERVICE_ide_onClick_if23813d93674dfd85cf37a250373b73_Success(response) {
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
        JACenter$user$get = mfobjectsecureinvokerasync(user_inputparam, "JACenter", "user", INVOKE_OBJECT_SERVICE_ide_onClick_b30173af1efd482d8b04ccedb05104c5_Callback);
    }
    function INVOKE_IDENTITY_SERVICE_ide_onClick_if23813d93674dfd85cf37a250373b73_Failure(error) {
        function SHOW_ALERT_ide_onClick_ie888e867c7241898beb8eb8d584a25e_Callback() {
            SHOW_ALERT_ide_onClick_ie888e867c7241898beb8eb8d584a25e_True();
        }
        voltmx.ui.Alert({
            "alertType": constants.ALERT_TYPE_ERROR,
            "message": "Login failed!  Invalid username or password.",
            "alertHandler": SHOW_ALERT_ide_onClick_ie888e867c7241898beb8eb8d584a25e_Callback
        }, {
            "iconPosition": constants.ALERT_ICON_POSITION_LEFT
        });
    }
    function SHOW_ALERT_ide_onClick_ie888e867c7241898beb8eb8d584a25e_True() {}
    if (login_inputparam == undefined) {
        var login_inputparam = {};
    }
    login_inputparam["serviceID"] = "UserAuthentication$login";
    login_inputparam["operation"] = "login";
    login_inputparam["userid"] = self.view.LoginForm.tbxUsername.text;
    login_inputparam["password"] = self.view.LoginForm.tbxPassword.text;
    UserAuthentication$login = mfidentityserviceinvoker("UserAuthentication", login_inputparam, INVOKE_IDENTITY_SERVICE_ide_onClick_if23813d93674dfd85cf37a250373b73_Success, INVOKE_IDENTITY_SERVICE_ide_onClick_if23813d93674dfd85cf37a250373b73_Failure);
}
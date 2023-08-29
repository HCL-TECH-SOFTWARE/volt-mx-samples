/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
function AS_Button_je066de0312642bf81ec787d6414752d(eventobject) {
    var self = this;

    function SHOW_ALERT_ide_onClick_dadedd2477c642188f0ba524333ad079_True() {}
    function SHOW_ALERT_ide_onClick_afef270fd8f249fd9ffd67eccfc0be45_True() {}
    function INVOKE_OBJECT_SERVICE_ide_onClick_i1f8a6a0f0644a68b7309958da8b9af3_Callback(signuprequest) {
        if (signuprequest.httpStatusCode !== 0) {
            function SHOW_ALERT_ide_onClick_afef270fd8f249fd9ffd67eccfc0be45_Callback() {
                SHOW_ALERT_ide_onClick_afef270fd8f249fd9ffd67eccfc0be45_True();
            }
            voltmx.ui.Alert({
                "alertType": constants.ALERT_TYPE_ERROR,
                "alertTitle": "Registration Error",
                "message": 'ERROR: registration request failed!' + signuprequest.errmsg,
                "alertHandler": SHOW_ALERT_ide_onClick_afef270fd8f249fd9ffd67eccfc0be45_Callback
            }, {
                "iconPosition": constants.ALERT_ICON_POSITION_LEFT
            });
        } else {
            function SHOW_ALERT_ide_onClick_dadedd2477c642188f0ba524333ad079_Callback() {
                SHOW_ALERT_ide_onClick_dadedd2477c642188f0ba524333ad079_True();
            }
            voltmx.ui.Alert({
                "alertType": constants.ALERT_TYPE_INFO,
                "alertTitle": "Registration Successful",
                "message": "SUCCESS:  Registration request received\n\nAdministration will review and respond via the provided email address\n\nThank you",
                "alertHandler": SHOW_ALERT_ide_onClick_dadedd2477c642188f0ba524333ad079_Callback
            }, {
                "iconPosition": constants.ALERT_ICON_POSITION_LEFT
            });
            self.view.SignupForm.isVisible = false;
            self.view.LoginForm.isVisible = true;
        }
    }
    if (signuprequest_inputparam == undefined) {
        var signuprequest_inputparam = {};
    }
    signuprequest_inputparam["serviceID"] = "JACenter$signuprequest$create";
    signuprequest_inputparam["options"] = {
        "access": "online",
        "CRUD_TYPE": "create"
    };
    var data = {};
    data["firstname"] = self.view.SignupForm.txtFirstName.text;
    data["lastname"] = self.view.SignupForm.txtLastName.text;
    data["displayname"] = self.view.SignupForm.txtDisplayName.text;
    data["userid"] = self.view.SignupForm.txtEmail.text;
    data["title"] = voltmx.visualizer.toString(null);
    signuprequest_inputparam["options"]["data"] = data;
    var signuprequest_httpheaders = {};
    signuprequest_inputparam["httpheaders"] = signuprequest_httpheaders;
    var signuprequest_httpconfigs = {};
    signuprequest_inputparam["httpconfig"] = signuprequest_httpconfigs;
    JACenter$signuprequest$create = mfobjectsecureinvokerasync(signuprequest_inputparam, "JACenter", "signuprequest", INVOKE_OBJECT_SERVICE_ide_onClick_i1f8a6a0f0644a68b7309958da8b9af3_Callback);
}
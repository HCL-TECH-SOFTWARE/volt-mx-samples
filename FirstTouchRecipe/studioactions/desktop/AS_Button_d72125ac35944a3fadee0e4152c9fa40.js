/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
function AS_Button_d72125ac35944a3fadee0e4152c9fa40(eventobject) {
    var self = this;

    function SHOW_ALERT_ide_onClick_f205095f49e94a2f8099e539c61a89a5_True() {}
    function SHOW_ALERT_ide_onClick_bbcd4d673c0f4e06a573a4df3fba4b1e_True() {}
    function INVOKE_OBJECT_SERVICE_ide_onClick_a0863290af89443baac59fdbb3fb0c4d_Callback(signuprequest) {
        if (signuprequest.httpStatusCode !== 0) {
            function SHOW_ALERT_ide_onClick_bbcd4d673c0f4e06a573a4df3fba4b1e_Callback() {
                SHOW_ALERT_ide_onClick_bbcd4d673c0f4e06a573a4df3fba4b1e_True();
            }
            voltmx.ui.Alert({
                "alertType": constants.ALERT_TYPE_ERROR,
                "alertTitle": "Registration Error",
                "message": 'ERROR: registration request failed!' + signuprequest.errmsg,
                "alertHandler": SHOW_ALERT_ide_onClick_bbcd4d673c0f4e06a573a4df3fba4b1e_Callback
            }, {
                "iconPosition": constants.ALERT_ICON_POSITION_LEFT
            });
        } else {
            function SHOW_ALERT_ide_onClick_f205095f49e94a2f8099e539c61a89a5_Callback() {
                SHOW_ALERT_ide_onClick_f205095f49e94a2f8099e539c61a89a5_True();
            }
            voltmx.ui.Alert({
                "alertType": constants.ALERT_TYPE_INFO,
                "alertTitle": "Registration Successful",
                "message": "SUCCESS:  Registration request received\n\nAdministration will review and respond via the provided email address\n\nThank you",
                "alertHandler": SHOW_ALERT_ide_onClick_f205095f49e94a2f8099e539c61a89a5_Callback
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
    JACenter$signuprequest$create = mfobjectsecureinvokerasync(signuprequest_inputparam, "JACenter", "signuprequest", INVOKE_OBJECT_SERVICE_ide_onClick_a0863290af89443baac59fdbb3fb0c4d_Callback);
}
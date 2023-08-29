/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
function AS_Button_a39f41b026aa44faa6a7abd1182068b3(eventobject) {
    var self = this;

    function SHOW_ALERT_ide_onClick_a72cf8ca43f84d9eb037ada18c219310_True() {}
    function SHOW_ALERT_ide_onClick_a72cf8ca43f84d9eb037ada18c219310_Callback() {
        SHOW_ALERT_ide_onClick_a72cf8ca43f84d9eb037ada18c219310_True();
    }
    voltmx.ui.Alert({
        "alertType": constants.ALERT_TYPE_INFO,
        "message": "User profile form coming next sprint!",
        "alertHandler": SHOW_ALERT_ide_onClick_a72cf8ca43f84d9eb037ada18c219310_Callback
    }, {
        "iconPosition": constants.ALERT_ICON_POSITION_LEFT
    });
}
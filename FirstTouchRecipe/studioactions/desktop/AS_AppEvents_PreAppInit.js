/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
function AS_AppEvents_PreAppInit(eventobject) {
    var self = this;
    voltmx.theme.setCurrentTheme(
    voltmx.store.getItem('theme') || 'JanusLightTheme', function() {
        return;
    }, function(err) {
        alert("Error setting theme:" + err);
    });
}
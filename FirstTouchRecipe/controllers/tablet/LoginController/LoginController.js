/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define({
  /**
   * Authorization check - get user record matching with username after login success
   *
   * data : record returned with query 'userid eq username' from user table
   */
  getUserRecord: function(data) {
    const self = this;

    if(data.records.length !== 1) {
      voltmx.ui.Alert({
        "alertType": constants.ALERT_TYPE_INFO,
        "alertTitle": "Invalid JAC Admin",
        "yesLabel": null,
        "noLabel": null,
        "alertIcon": null,
        "message": "Please contact an administrator to access the Recipe Catalog"
      }, {
        "iconPosition": constants.ALERT_ICON_POSITION_LEFT
      });
    } else {
      userProfile = data.records[0];
    }
  },

  /**
   * @function
   *
   */
  saveUserData: function() {
    const serviceName = JAC.IDENTITY_SERVICE;
    const client = voltmx.sdk.getCurrentInstance();
    const identitySvc = client.getIdentityService(serviceName);
    const forceFromServer = false;
    identitySvc.getProfile(forceFromServer, function(response) {
      if(response.userid !== userProfile.userid) {
        // TODO : pull user from object service again
      }
    }, function(error) {
      voltmx.print("Failed to fetch profile: " + JSON.stringify(error));
    });
  }
});

/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define(function() {
  return {
    constructor: function(baseConfig, layoutConfig, pspConfig) {
      this.view.btnSignin.onClick = this.userStoreLogin;
      this._MainFormName = "Main";
    },
    //Logic for getters/setters of custom properties
    initGettersSetters: function() {
            defineGetter(this, 'OAuthSvcName', () => {
                return this._OAuthSvcName;
            });
            defineSetter(this, 'OAuthSvcName', value => {
                this._OAuthSvcName = value;
            });
            defineGetter(this, 'AppTitle', () => {
                return this._AppTitle;
            });
            defineSetter(this, 'AppTitle', value => {
                this._AppTitle = value;
                this.view.lblAppTitle.text = value;
            });
            defineGetter(this, 'MainFormName', () => {
                return this._MainFormName;
            });
            defineSetter(this, 'MainFormName', value => {
                this._MainFormName = value;
            });
            defineGetter(this, 'LoginFormName', () => {
                return this._LoginFormName;
            });
            defineSetter(this, 'LoginFormName', value => {
                this._LoginFormName = value;
            });
        },

    checkSSO : function(onFailure) {
      const identityService = VMXFoundry.getIdentityService(this._OAuthSvcName);
      var isLoginPersisted = identityService.usePersistedLogin();
      if(isLoginPersisted) {
        this.getUserProfile();
      } else {
        onFailure();
      }
    },

    userStoreLogin: function() {
      if (this.oAuthLogin) {
        //for mobile
        this.oAuthLogin(this._OAuthSvcName, this.getUserProfile, this.loginFailure);
      } else {
        const identityService = VMXFoundry.getIdentityService(this._OAuthSvcName);
        identityService.login({
          loginOptions: {
            persistLoginResponse: true,
          }
        }, this.getUserProfile, this.loginFailure);
      }
    },

    getUserProfile: function() {
      const identityService = VMXFoundry.getIdentityService(this._OAuthSvcName);
      identityService.getProfile({
        persistLoginResponse: true,
        isSSOEnabled: true,
        loginOptions: {
          persistLoginResponse: true,
          isSSOEnabled: true,
        }
      }, this.loginSuccess, this.fetchUserProfileError);
    },
    /**
   * callback for login failure
   */
    loginSuccess: function(profile) {
      if (profile && profile.firstname !== 'Authenticated') {
        saveUsername(profile.firstname + ' ' + profile.lastname);
      }
      const ntf = new voltmx.mvc.Navigation(this._MainFormName);
      const form = voltmx.application.getCurrentForm();
      ntf.navigate({
        loginContext:{
          loginService: this._OAuthSvcName,
          loginFormId: form ? form.id : this._LoginFormName,
        },
        isCancel: false,
      });
    },

    fetchUserProfileError: function(e) {
      voltmx.print("Fetch user proflie exception Occured: "); 
      voltmx.print(e);
      this.loginSuccess();//ignore error.
    },
    /**
   * callback for login failure
   */
    loginFailure: function() {
      voltmx.ui.Alert({
        "alertType": constants.ALERT_TYPE_ERROR,
        "message" : "Login failed!",
      }, {
        "iconPosition": constants.ALERT_ICON_POSITION_LEFT
      }
                     );
    },

  };
});

/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define(function() {
  constants.DEFAULT_MINIMUM_CHAR_LENGTH = 8;
  constants.USERNAME_VALIDATION_MESSAGE = "Username too small";
  constants.PASSWORD_VALIDATION_MESSAGE = "Password too small";
  constants.USERNAME_PASSWORD_VALIDATION_MESSAGE = "Username and Password are too small";
  constants.EMPTY_USERNAME_VALIDATION_MESSAGE = "Username cannot be empty";
  constants.EMPTY_PASSWORD_VALIDATION_MESSAGE = "Password cannot be empty";
  constants.EMPTY_USERNAME_PASSWORD_VALIDATION_MESSAGE = "Username and Password cannot be empty";
  constants.LOGIN_SUCCESS_EVENT_MISSING_MESSAGE = "Login Success but loginSuccessEvent not defined";
  constants.LOGIN_FAILURE_EVENT_MISSING_MESSAGE = "Login Failed but loginFailureEvent not defined";
  return {
    constructor: function(baseConfig, layoutConfig, pspConfig) {
      this.view.tbxUsername.onDone = this.userStoreLogin;
      this.view.tbxPassword.onDone = this.userStoreLogin;
      this.view.btnSignin.onClick = this.userStoreLogin;
      //NEEDSWORK
      this._MainFormName = "Main";
    },
    //Logic for getters/setters of custom properties
    initGettersSetters: function() {
      defineGetter(this, 'UserStoreSvcName', () => {
        return this._UserStoreSvcName;
      });
      defineSetter(this, 'UserStoreSvcName', value => {
        this._UserStoreSvcName = value;
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
    },
    userStoreLogin: function() {
      this.validateUserId();
      this.validatePassword();
      const username = this.view.tbxUsername.text;
      this.getUserId(this._UserStoreSvcName, (profile) => {
        const storeProfile = getProfile();
        const storeUsername = getUsername();
        if (profile.userid !== storeProfile.userid || username !== storeUsername) {
          alert(`There is active session of user ${profile.userid}, please logout before login`);
        } else {
          const password = this.view.tbxPassword.text;
          this.view.tbxUsername.text = "";
          this.view.tbxPassword.text = "";
          this._userStoreLogin(username, password);
        }
      }, (err) => {
        const password = this.view.tbxPassword.text;
        this.view.tbxUsername.text = "";
        this.view.tbxPassword.text = "";
        this._userStoreLogin(username, password);
      });
    },
    _userStoreLogin: function(username, password) {
      const userid = username;
      const identityService = VMXFoundry.getIdentityService(this._UserStoreSvcName);
      const options = {
        username,
        userid,
        password,
        loginOptions: {
          isSSOEnabled: true,
        }
      };
      identityService.login(options, (res) => {
        identityService.getProfile(true, (userProfile) => {
          this.loginSuccess(username, userProfile);
        }, (err1) => {
          // fail to get session profile
        });
      }, this.loginFailure);
    },

    /**
      * @function validateUserId
      * @description Validates username entered by the user
      * @private
      * @returns {boolean} true/false
      */
    validateUserId: function() {
      try {
        if (parseInt(this._usernameMinimumChar) > this.getUsername().length) {
          this.view.tbxUsername.text = this.getUsername();
          this.view.lblError.text = constants.USERNAME_VALIDATION_MESSAGE;
          this.view.flxError.isVisible = true;
          this.view.flxError.forceLayout();
          return false;
        }
        return true;
      } catch (exception) {
        kony.print(JSON.stringify(exception));
        if(exception.type === "CUSTOM"){
          throw exception;
        }
      }
    },
    /**
      * @function validatePassword
      * @description Validates password entered by the user
      * @private
      * @returns {boolean} true/false
      */
    validatePassword: function() {
      try {
        if (parseInt(this._passwordMinimumChar) > this.getPassword().length) {
          this.view.tbxPassword.text = this.getPassword();
          this.view.lblError.text = constants.PASSWORD_VALIDATION_MESSAGE;
          this.view.flxError.isVisible = true;
          this.view.flxError.forceLayout();
          return false;
        }
        return true;
      } catch (exception) {
        kony.print(JSON.stringify(exception));
        if(exception.type === "CUSTOM"){
          throw exception;
        }
      }
    },
    /**
      * @function validateUserIdAndPassword
      * @description validates empty username and password
      * @private
      * @return {boolean} true/false
    	*/
    validateUserIdAndPassword : function() {
      var isUsernameEmpty = !this.getUsername().length;
      var isPasswordEmpty = !this.getPassword().length;
      var errorText = null;

      if(isUsernameEmpty && isPasswordEmpty) {
        errorText = constants.EMPTY_USERNAME_PASSWORD_VALIDATION_MESSAGE;
      } else if(isUsernameEmpty) {
        errorText = constants.EMPTY_USERNAME_VALIDATION_MESSAGE;
      } else if(isPasswordEmpty) {
        errorText = constants.EMPTY_PASSWORD_VALIDATION_MESSAGE;
      }

      if(!errorText) {
        var isUsernameSmall = parseInt(this._usernameMinimumChar) > this.getUsername().length;
        var isPasswordSmall = parseInt(this._passwordMinimumChar) > this.getPassword().length;
        if(isUsernameSmall && isPasswordSmall) {
          errorText = constants.USERNAME_PASSWORD_VALIDATION_MESSAGE;
        } else if(isUsernameSmall) {
          errorText = constants.USERNAME_VALIDATION_MESSAGE;
        } else if(isPasswordSmall) {
          errorText = constants.PASSWORD_VALIDATION_MESSAGE;
        }
      }
      if(errorText) {
        this.view.lblError.text = errorText;
        this.view.flxError.isVisible = true;
        this.view.flxError.forceLayout();
      } else {
        this.view.flxError.isVisible = false;
      }
    },
  /**
   * callback for login failure
   */
    loginSuccess: function(username, profile) {
      saveUsername(username);
      saveProfile(profile);
      const form = voltmx.application.getCurrentForm();
      const ntf = new voltmx.mvc.Navigation(this._MainFormName);
      ntf.navigate({
        loginContext:{
          loginService: this._UserStoreSvcName,
          loginFormId: form.id,
        },
        isCancel: false,
      });
    },
    /**
   * callback for login failure
   */
    loginFailure: function() {
      voltmx.ui.Alert({
        "alertType": constants.ALERT_TYPE_ERROR,
        "message": "Login failed! Invalid username or password.",
      }, {
        "iconPosition": constants.ALERT_ICON_POSITION_LEFT
      }
                     );
    },
    checkSessionBySerivce: function(serviceName) {
      return new Promise((resolve, reject) => {
        try {
          // check login session
          /*
          const identityService = KNYMobileFabric.getIdentityService(serviceName);
          identityService.login({
            loginOptions: {
              isSSOEnabled: true,
            },
          }, (res) => {
          */
            identityService.getProfile(true, (profile) => {
              resolve(profile);
            }, (err) => {
              reject(err);
            });
          /*
          }, (err) => {
            reject(err);
          });
          */
        } catch (e) {
          // unknown exception
        }

      });
    },
    checkSession: async function() {
      const list = [this._UserStoreSvcName];
      let profile;
      for (let i = 0 ; i < list.length ; i++) {
        try {
          const serviceName = list[i];
          if (profile === undefined) {
            profile = await this.checkSessionBySerivce(serviceName);
            this.loginSuccess(profile);
          }
        } catch (e) {
        }
      }
    },
    getUserId: function(identityServiceName, successCallback, errorCallback) {
      try {
        // check login session
        const identityService = VMXFoundry.getIdentityService(identityServiceName);
        // session valid, get session profile
        identityService.getProfile(true, (profile) => {
          successCallback(profile);
        }, (err) => {
          if (errorCallback) {
            errorCallback(err);
          }
        });
      } catch (e) {
        if (errorCallback) {
          errorCallback(e);
        }
      }
    },
  };
});

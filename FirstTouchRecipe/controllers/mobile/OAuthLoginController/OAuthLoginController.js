/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define({
  onNavigate: function() {
     this.view.OAuthLoginForm.oAuthLogin = this.onLogin;
     //redirected from session expiration
     this.closeBrowserWidget();
  },

  closeBrowserWidget: function() {
   if( this.view.defaultBrowserWidgetForOauth2 ) { 
      voltmx.application.dismissLoadingScreen();
      this.view.defaultBrowserWidgetForOauth2.width = "0%";
      this.view.defaultBrowserWidgetForOauth2.height = "0%";
   }
  },

  onLogin: function(svcName, onSuccess, onFailure) {
        if (!this.view.defaultBrowserWidgetForOauth2) {
            this.view.add(new voltmx.ui.Browser({
                "id": "defaultBrowserWidgetForOauth2",
                "left": "0dp",
                "top": "0dp",
                "width": "100%",
                "height": "100%"
            }, {}, {}));
        } else {
           //redirected from session expiration
           this.view.defaultBrowserWidgetForOauth2.width = "100%";
           this.view.defaultBrowserWidgetForOauth2.height = "100%";
        }
    
        const loginParams = {
          browserWidget: this.view.defaultBrowserWidgetForOauth2,
        };
        const identityService = VMXFoundry.getIdentityService(svcName);
        identityService.login(loginParams, onSuccess, () =>{
         this.closeBrowserWidget();
         onFailure();
        });
  }
});

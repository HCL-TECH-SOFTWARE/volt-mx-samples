/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
const STORE_PROFILE_KEY = 'userProfile';
const STORE_USERNAME_KEY = 'username';

function loginFormInit(Login, HeaderBar, FooterBar, AboutBox) {

  /*NEEDSWORK
  VMXFoundry.OfflineObjects.setup({}, (res) => {
    console.log('setup success');
  }, (err) => {
//    alert('setup failure');
  });
  */
  HeaderBar.onMenuClick = menuClickHandler(Login);
  HeaderBar.title = APP_INFO.NAME;
  HeaderBar.visible = false;
  /*
  AboutBox.appName = APP_INFO.NAME;
  AboutBox.appVersion = APP_INFO.VERSION;
  AboutBox.appLogo = APP_INFO.APP_LOGO;
  */
  FooterBar.AppVersion = APP_INFO.VERSION;
  FooterBar.AppName = APP_INFO.NAME;
}

function formInit(Main, HeaderBar, FooterBar, MenuBar, AboutBox) {
  MenuBar.setMenuItems(menuItems);
  MenuBar.closeMenu = menuClickHandler(Main, MenuBar);
  HeaderBar.onMenuClick = menuClickHandler(Main, MenuBar);
  HeaderBar.title = APP_INFO.NAME;
  HeaderBar.username = getUsername();
  HeaderBar.onClickBtnSignout = () => {
    this.userLogout();
  };
  FooterBar.onClickBtnInfo = () => { AboutBox.isVisible = true; };
  FooterBar.onTouchEndLblVersion = () => { AboutBox.isVisible = true; };
  FooterBar.onTouchEndLblAppName = () => { AboutBox.isVisible = true; };

  AboutBox.appName = APP_INFO.NAME;
  AboutBox.appRuntimeVersion = APP_INFO.RUNTIME_VERSION;
  AboutBox.appVersion = APP_INFO.VERSION;
  AboutBox.appLogo = APP_INFO.APP_LOGO;
  FooterBar.AppVersion = APP_INFO.VERSION;
  FooterBar.AppName = APP_INFO.NAME;
}


async function logout () {
    voltmx.model.ApplicationContext.showLoadingScreen('Logout in progress...');
    const { loginService, loginFormId } = GlobalState.loginContext;
    let success = false;
    try {
      await signOutUserSession(loginService);
      success = true;
    } catch (e) {
    }

    if (success) {
      const ntf = new voltmx.mvc.Navigation(loginFormId);
      ntf.navigate();
    } else {
      voltmx.ui.Alert({
        "alertType": constants.ALERT_TYPE_ERROR,
        "alertTitle": "Sign Out",
        "message": "An error occured during the sign out process.",
      }, {
        "iconPosition": constants.ALERT_ICON_POSITION_LEFT
      });
    }
    voltmx.model.ApplicationContext.dismissLoadingScreen();
}

function signOutUserSession (serviceName) {
    return new Promise((resolve, reject) => {
      try {
        // check login session
        const options = {
          slo: true,
        };
        const identityService = KNYMobileFabric.getIdentityService(serviceName);
        identityService.logout((res) => {
          resolve(res);
        }, (err) => {
          reject(err);
        }, options);
      } catch (e) {
        // unknown exception
      }
    });
  }

function menuClickHandler(Main, MenuBar) {
  return () => {
    toggleMenu(Main, MenuBar);
  };
}

function navigateToForm(formName) {
  return () => {
    try {
      const ntf = new voltmx.mvc.Navigation(formName);
      ntf.navigate();
    } catch (e) {
    }
  };
}

function saveUsername(username) {
  voltmx.store.setItem(STORE_USERNAME_KEY, username);
}

function getUsername() {
  const username = voltmx.store.getItem(STORE_USERNAME_KEY) || '';
  return username;
}

function saveProfile(profile) {
  voltmx.store.setItem(STORE_PROFILE_KEY, JSON.stringify(profile));
}

function getProfile() {
  const data = voltmx.store.getItem(STORE_PROFILE_KEY);
  const profile = JSON.parse(data ? data : '{}');
  return profile;
}

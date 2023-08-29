/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define({
  defaultTheme: 'JanusLightTheme',
  lightTheme: 'JanusLightTheme',
  darkTheme: 'JanusDarkTheme',

  /**
   * @function	getStoredTheme	returns the theme stored in client side storage
   * @returns		string reprensenting the stored theme name: JanusLightTheme, darkTheme
   */
  getStoredTheme: function() {
    return voltmx.store.getItem('theme') || null;
  },

  /**
   * @function	storeTheme	stores the theme passed in as param into client side storage
   * @param			theme			string reprensenting the theme name: lightTheme, darkTheme
   */
  storeTheme: function(theme) {
    voltmx.store.setItem('theme', theme);
  },

  /**
   * @function	storeCurrentTheme	stores the currently used theme into client side storage
   */
  storeCurrentTheme: function() {
    this.storeTheme(voltmx.theme.getCurrentTheme());
  },

  /**
   * @function	useTheme	switches to and stores the theme received as param
   * @param			theme			string reprensenting the theme name: lightTheme, darkTheme
   */
  activateTheme: function(theme) {
    const self = this;
    voltmx.theme.setCurrentTheme(
      theme,
      function() { return self.storeCurrentTheme(); },
      function(err) { alert("Error setting theme:" + err); }
    );
  },

  /**
   * @function	activateStoredTheme		switches to the stored theme (or default if none) and stores the theme received as param
   * @param			theme			string reprensenting the theme name: lightTheme, darkTheme
   */
  activateStoredTheme: function() {
    this.activateTheme(getStoredTheme() || this.defaultTheme);
  },

  /**
   * @function	toggleTheme	toggles between janus dark and light themes
   * @returns		boolean		true: theme toggled successfully
   *											false: error toggling themes
   */
  toggleTheme: function() {
    this.activateTheme( voltmx.theme.getCurrentTheme() === this.lightTheme ? this.darkTheme : this.lightTheme);
  }
});

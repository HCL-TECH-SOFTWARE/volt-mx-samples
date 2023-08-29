/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define(function() {

	return {
		constructor: function(){
        this.view.flxAppMenu.onClick = this.onClickShowMenu;
    },

    //onClick defined for flexAppMenu
    onClickShowMenu: function() {
      if (!this.view.flxMenu.isVisible) {
        this.view.parent.clearAllMenus();
        this.view.parent.addMenu(this.view.flxMenu);
        this.view.flxMenu.setVisibility(true);
      } else {
        this.view.flxMenu.setVisibility(false);
      }
    },

    onClickHideMenu: function(){
      this.view.flxMenu.setVisibility(false);
    },

    addDeleteListener: function(listener) {
      this.deleteListener = listener;
    },

    addEditListener: function(listener) {
      this.editListener = listener;
    },

    addExpandListener: function(listener) {
      this.expandListener = listener;
    },

    onClickDelete: function() {
      this.onClickHideMenu();
      this.deleteListener.call(this, this.view.appData);
    },

    onClickEdit: function() {
      this.onClickHideMenu();
      this.editListener.call(this, this.view.appData);
    },

	onClickExpand: function() {
      this.expandListener.call(this, this.view.appData);
	},
	};
});

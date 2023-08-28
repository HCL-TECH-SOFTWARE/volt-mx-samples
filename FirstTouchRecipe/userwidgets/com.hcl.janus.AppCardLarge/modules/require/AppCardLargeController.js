/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define(function() {

	return {
	/*
    addDeleteListener: function(listener) {
      this.deleteListener = listener;
    },

    addEditListener: function(listener) {
      this.editListener = listener;
    },

    onClickDelete: function() {
      this.onClickHideMenu();
      this.deleteListener.call(this, this.view.appData);
    },
    */

    onClickExEdit: function() {
      voltmx.print("Entered onClickEdit");
      //this.onClickHideMenu();
      //this.editListener.call(this, this.view.appData);
    },

	};
});

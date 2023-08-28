/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define(function() {

	return {
		constructor: function() {
          const menus = [];
          this.view.flxCards.addMenu = function(menu) {
            menus.push(menu);
          };
          this.view.flxCards.clearAllMenus = function(menu) {
            for (var i = menus.length -1; i>=0; i--) {
               menus[i].setVisibility(false);
               menus.pop();
             }
          };
        },
	};
});

/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define(function() {

	return {
      processRemoveIngredient: function(arg1, arg2) {
        const device = voltmx.os.deviceInfo().name.toLowerCase();
        const rowIndex = (device == 'android' || device == 'iphone' ) ? arg2 : arg1;
        var viewcontroller = this;
        var msg = "Are you sure you want to remove the ingredient?";


        voltmx.ui.Alert({
          message: msg,
          alertType: constants.ALERT_TYPE_CONFIRMATION,
          alertTitle: "Remove a ingredient",
          yesLabel: "Remove",
          noLabel: "Cancel",
          alertHandler: processConfirmation,
        }, {
          "iconPosition": constants.ALERT_ICON_POSITION_LEFT
        });

        function processConfirmation(isConfirmed) {
          if (isConfirmed) {
            viewcontroller.removeSelected(rowIndex);
          }
        }
      },

      removeSelected: function(rowIndex) {
        this.view.segIngredient.removeAt(rowIndex, 0);
      },

	};
});

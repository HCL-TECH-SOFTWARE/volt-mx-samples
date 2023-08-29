/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define({
  getUserPreference: function(data) {
    let userData;
    let found = false;
    for(i = 0; i < data.records.length; i++){
      if(data.records[i] !== undefined && data.records[i].userid === userid) {
        userData = data.records[i];
        found = true;
        break;
      }
    }
    if(found) {
      //TODO : render main page with userData
    }
  },

  showAppCards: function(application){
    const self = this;
    if(application.records.length === 0){
      return;
    }
    var flxAppCards = new voltmx.ui.FlexScrollContainer({
      "allowHorizontalBounce": false,
      "allowVerticalBounce": true,
      "bounces": true,
      "clipBounds": true,
      "enableScrolling": true,
      "height": "100%",
      "horizontalScrollIndicator": true,
      "id": "flxAppCards",
      "isVisible": true,
      "layoutType": voltmx.flex.FLOW_HORIZONTAL,
      "left": "0dp",
      "pagingEnabled": false,
      "scrollDirection": voltmx.flex.SCROLL_VERTICAL,
      "skin": "cardsContainer",
      "top": "0dp",
      "verticalScrollIndicator": true,
      "width": "100%",
      "zIndex": 1
    }, {}, {});
    flxAppCards.setDefaultUnit(voltmx.flex.DP);
    application.records.forEach((app)=>{
      let appCard = self.createCard(app);
      flxAppCards.add(appCard);
    });
	this.view.CardsContainer.add(flxAppCards);
  },

  createCard: function(app) {
    const tag = Date.now();
    const openApp = function(){
      voltmx.application.openURL(app[JAC.EXEC_PATH_FIELD]);
    };
    const appCard = new com.hcl.janus.AppCard({
      "autogrowMode": voltmx.flex.AUTOGROW_NONE,
      "height": "200dp",
      "id": "AppCard" + tag,
      "isVisible": true,
      "layoutType": voltmx.flex.FREE_FORM,
      "left": "0dp",
      "masterType": constants.MASTER_TYPE_DEFAULT,
      "isModalContainer": false,
      "skin": "AppTileOuterSkin",
      "top": "0dp",
      "width": "200dp",
      "zIndex": 1,
      "overrides": {
        "AppCard": {
          "isVisible": true
        },
        "lblAppTitle": {
          "text": app[JAC.TITLE_FIELD]
        },
        "flxAppImage": {
          "onClick": openApp
        },
        "imgAppIcon": {
          "src": app[JAC.ICON_PATH_FIELD]
        },
        "imgAppMenu": {
          "src": "overflow_menu__vertical.png"
        }
      }
    }, {
      "overrides": {}
    }, {
      "overrides": {}
    });
    return appCard;
  }

 });

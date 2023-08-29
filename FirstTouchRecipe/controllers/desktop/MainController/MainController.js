/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
define({
  /**
   * Initialize event handlers and display main page
   */
  onNavigate: function (context) {
    if (context) {
      GlobalState.loginContext = context.loginContext;
    }

    this.view.MainContainer.onClick = this.onClickMainContainer;
    this.view.MainContainer.HeaderBar.flxAddRecipe.onClick = this.onAddRecipeMenuClick;
    this.view.MainContainer.HeaderBar.flxCreateBanner.flxAddButton.onClick = this.onAddRecipeMenuClick;

    this.view.HeaderBar.tbxSearch.onDone = this.onSearchTextChange;
    this.view.HeaderBar.tbxSearch.onTextChange = this.onSearchTextChange;

    this.view.AppCardLarge.flxOuterCard.flxInnerCard.flxCardHeader.flxActionbarContainer.flxEdit.onClick=this.onExCardEditClick;
    this.view.AppCardLarge.flxOuterCard.flxInnerCard.flxCardHeader.flxActionbarContainer.flxDelete.onClick=this.onExCardDeleteClick;
    this.view.AppCardLarge.flxClose.onClick=this.onExCardCloseClick;

    this.view.FooterBar.btnInfo.onClick = this.onClickShowAboutBox;
    this.view.FooterBar.lblVersion.onTouchEnd = this.onClickShowAboutBox;
    this.view.FooterBar.lblAppName.onTouchEnd = this.onClickShowAboutBox;

    const username = getUsername();
    this.view.HeaderBar.userDisplayName.text = username;

    // Display recipe cards
    this.toggleRecipeFormContainer(false);
    this.toggleExpandedRecipeContainer(false);
    this.view.AlertDialog.setVisibility(false);
    this.refreshAppCards();
  },

  /**
   * Get the current user's preferences
   *
   * data: Preference data
   */
  getUserPreference: function(data) {
    let userData;
    let found = false;
    for (i = 0; data.records && i < data.records.length; i++) {
      if (data.records[i] !== undefined && data.records[i].userid === userid) {
        userData = data.records[i];
        found = true;
        break;
      }
    }
  },

  /**
   * Generate Recipe cards for the main page
   *
   * response.records: Holds the Recipe data
   */
  showAppCards: function(response) {
    const self = this;
    self.view.HeaderBar.flxSearch.isVisible = true;
    // Clear existing cards
    try {
      this.view.CardsContainer.flxCards.removeAll();
    } catch (e) {
      voltmx.print("Error: remove all cards failed");
    }

    if (response.records === undefined || response.records.length === 0) {
      return;
    }

    const count = response.records.length;
    this.view.MainContainer.HeaderBar.flxCreateBanner.lblRecipeCount.text =
      count > 1 ? `${count} Suggested Recipes` : `${count} Suggested Recipe`;

    // Get sort type
    let sort_type = voltmx.store.getItem('sort_type');
    let sort_ascending = voltmx.store.getItem('sort_ascending');

    // If no sort set, default to SORT_BY_NAME
    if (sort_type === null) {
      sort_type = JAC.SORT_BY_NAME;
      sort_ascending = true;
      this.storeSort(sort_type, sort_ascending);
    }

    // Sort Applications
    self.sortAppCards(response.records, sort_type, sort_ascending);

    // Redisplay Applications
    response.records.forEach((record) => {
      let recipeCard = self.createCard(record, self);
      this.view.CardsContainer.flxCards.add(recipeCard);
    });
  },

  /**
   * Returns the type of sort (SORT_BY_NAME or SORT_BY_CREATION_DATE)
   */
  getStoredSortType: function() {
    return voltmx.store.getItem('sort_type');
  },

  /**
   * Returns the sort order (TRUE if ascending)
   */
  getStoredSortOrder: function() {
    return voltmx.store.getItem('sort_ascending');
  },

  /**
   * storeSort saves the user's sort settings
   *
   * sort_type: The type of sort to perform (SORT_BY_NAME or SORT_BY_CREATION_DATE)
   * sort_ascending: Sort Ascending if true
   */
  storeSort: function(sort_type, sort_ascending) {
    voltmx.store.setItem('sort_type', sort_type);
    voltmx.store.setItem('sort_ascending', sort_ascending);
  },

  /**
   * Sort recipes cards by Name or Creation date
   *
   * recipes: The list of recipes
   * sort_type: The type of sort to perform (SORT_BY_NAME, SORT_BY_CREAIION_DATE)
   * sort_ascending: Sort Ascending if true
   */
  sortAppCards: function(recipes, sort_type, sort_ascending) {

    // Sort Applications
    switch (sort_type) {

      // Sort by Name
      case JAC.SORT_BY_NAME:
        recipes.sort((a,b) => a.Name > b.Name ? (sort_ascending ? 1 : -1) : b.Name > a.Name ? (sort_ascending ? -1 : 1) : 0);
        break;

      // Sort by Creation Date
      case JAC.SORT_BY_CREATION_DATE:
        recipes.sort((a,b) => a.CreatedDateTime > b.CreatedDateTime ? (sort_ascending ? 1 : -1) : b.CreatedDateTime > a.CreatedDateTime ? (sort_ascending ? -1 : 1) : 0);
        break;
    }
  },

  /**
   * Sort app cards by Name
   */
  sortByName: function() {
    const self = this;
    self.sortClick(JAC.SORT_BY_NAME);
  },

  /**
   * Sort app cards by Creation Date
   */
  sortByCreate: function() {
    const self = this;
    self.sortClick(JAC.SORT_BY_CREATION_DATE);
  },

  /**
   * Create a Recipe card
   *
   * record: Contains the Recipe data
   * targetContext: context pointer
   */
  createCard: function(record, targetContext) {
    clean(record);
    // Create a Recipe card with a unique id
    const tag = Date.now();
    const recipeCard = new com.hcl.janus.AppCard({"id": "AppCard" + tag, "masterType": constants.MASTER_TYPE_DEFAULT});

    // Fill in the Recipe card fields
    recipeCard.setVisibility(true);
    recipeCard.lblAppTitle.text = record.Name;
    recipeCard.lblAppPrep.text = "Prep Time: "+record.PrepTime+" mins";
    recipeCard.lblAppCook.text = "Cook Time: "+record.CookTime+" mins";

    const imageData = extractImageData(record.PictureRT);
    if(imageData) {
      recipeCard.flxAppImage.imgAppIcon.base64 = extractImageData(record.PictureRT);
    }
    recipeCard.addDeleteListener(targetContext.onCardDeleteClick);
    recipeCard.addEditListener(targetContext.onCardEditClick);
    recipeCard.addExpandListener(targetContext.onExCardOpenClick);
    recipeCard.appData = record;
    return recipeCard;
  },

  /**
   * Refresh the Recipe card page after a change has occurred
   */
  refreshAppCards: function() {
    kony.model.ApplicationContext.showLoadingScreen('Loading...');
    getObject(JAC.APPLICATION_OBJECT, "", this.getListsSuccessCallback, this.getListsFailureCallback);
  },

  /**
   * Refresh the Recipe card page on success
   *
   * response: list of Recipe cards
   */
  getListsSuccessCallback: function (response) {
    kony.application.dismissLoadingScreen();
    this.showAppCards(response);
  },

  /**
   * Handle errors during page refresh
   */
  getListsFailureCallback: function (error) {
    kony.application.dismissLoadingScreen();
    showError(error.errmsg);
    voltmx.print("Failed to Fetch Recipes: " + JSON.stringify(error));
  },

  /**
   * Display an error message
   *
   * msg: The message to display
   */
  showError: function(msg) {
    voltmx.ui.Alert({
      "alertType": constants.ALERT_TYPE_ERROR,
      "message": msg
    }, {
      "iconPosition": constants.ALERT_ICON_POSITION_LEFT
    });
  },

  /**
   * This function is triggered when text is changed
   * in the search box
   */
  onSearchTextChange: function () {
    const searchText = this.view.HeaderBar.tbxSearch.text.trim() || "";
    const container = this.view.CardsContainer.flxCards;
    const cards = container.widgets();

    // Perform search
    if (searchText) {
      this.getSearchResult(cards, searchText);
    }
    // Clear search
    else {
      cards.forEach((card) => {
        card.opacity = 1.0;
      });
    }
  },

  /**
   * Perform the search by graying out recipes that do not
   * match the search text
   *
   * cards: The list of recipe cards
   * searchValue: The text to search for
   */
  getSearchResult: function (cards, searchValue) {

    cards.forEach((card) => {

      var data = card.appData ;
      if (data) {

        // Fetch recipe name and ingredients
        const recipeName = (card.appData.Name || "").toLocaleLowerCase();
        const recipeIngred = (card.appData.Ingredients || "").toLocaleLowerCase();

        // Perform search
        const pattern = (searchValue || "").toLocaleLowerCase().trim();
        if (recipeName.search(pattern) !== -1 || recipeIngred.search(pattern) !== -1) {
          card.opacity = 1.0;
        }
        else {
          card.opacity = 0.2;
        }
      }
    });
  },

  /**
   * onAddRecipeMenuClick is triggered when Add Recipe is clicked
   */
  onAddRecipeMenuClick: function() {
    this.view.CardsContainer.flxCards.clearAllMenus();
    this.setRecipeFormRecord(null, false);
    this.toggleRecipeFormContainer(true);
  },

  /**
   * Configure the form for Create or Edit
   */
  setRecipeFormRecord: function(record, isEdit =false) {
    this.view.RecipeForm.isEdit = isEdit;
    this.view.RecipeForm.record = record;
    this.view.RecipeForm.saveSuccess = this.onRecipeSaveOrUpdateSuccess;
    this.view.RecipeForm.saveCancel = this.onRecipeSaveCanceled;
  },

  /**
   * Refresh when there is a new or updataed recipe
   */
  onRecipeSaveOrUpdateSuccess() {
     this.toggleRecipeFormContainer(false);
     this.refreshAppCards();
  },

  /**
   * Close the form on Cancel
   */
  onRecipeSaveCanceled: function() {
    this.toggleRecipeFormContainer(false);
  },

  /**
   * Open / close the Recipe Form
   */
  toggleRecipeFormContainer: function(show) {
    this.view.HeaderBar.flxSearch.setVisibility(!show);
    this.view.MainContainer.HeaderBar.flxCreateBanner.setVisibility(!show);
    this.view.flxRecipeFormContainer.setVisibility(show);
    this.view.flxCardsContainer.setVisibility(!show);
  },

  /**
   * Toggle Recipe menu
   */
   onClickRecipeMenu: function(){
     this.view.MainContainer.HeaderBar.flxAddRecipe.setVisibility(!this.view.MainContainer.HeaderBar.flxAddRecipe.isVisible);
   },

  /**
   * onCardEditClick is triggered on click of Edit menu on App Card
   *
   * record: data for current Recipe
   */
  onCardEditClick: function(record) {
    this.setRecipeFormRecord(record, true);
    this.toggleRecipeFormContainer(true);
  },

  /**
   * onCardDeleteClick is triggered on click of Delete menu on App Card
   *
   * record: data for current Recipe
   */
  onCardDeleteClick: function(record) {
    this.view.AlertDialog.setYesBtnText("Delete");
    this.view.AlertDialog.setNoBtnText("Cancel");
    this.view.AlertDialog.setMessage("Are you sure you want to delete this recipe?");
    const self = this;
    const deleteHandler = function() {
      self.onExCardCloseClick();
      deleteObject("Recipe", record, (response) => {
        voltmx.print("Record deleted: " + JSON.stringify(response));
        self.refreshAppCards();
      }, (error) => {
        self.showError(error.errmsg);
        voltmx.print("Error in record delete: " + JSON.stringify(error));
      });
    };
    this.view.AlertDialog.setYesBtnClickCallback(deleteHandler);
    this.view.AlertDialog.setVisibility(true);
  },

  /**
   * expandRecipeCard fills in expanded recipe card with
   * recipe data
   *
   * record: data for this recipe card
   */
  expandRecipeCard: function(record) {

    // Set up shortcuts
    const header = this.view.AppCardLarge.flxInnerCard.flxCardHeader;
    const center = this.view.AppCardLarge.flxInnerCard.flxRecipeImage;
    const centerRightContainer = center.flxCenterRightContainer;
    const recipe = this.view.AppCardLarge.flxInnerCard.flxRecipe;

    // Fill in expanded card
    header.lblRecipeName.text = record ? record.Name : "";
    if (record) {
      centerRightContainer.imgRecipePicture.base64 = extractImageData(record.PictureRT);
    }
    else {
      centerRightContainer.imgRecipePicture.base64 = "";
    }
    let ingredients = record.Ingredients ? record.Ingredients.split(JAC.INGREDIENT_SEPARATOR).join("\n") : '';
    center.flxIngredients.flxIngredientsList.richTextIngredients.text = ingredients;
    recipe.flxDirections.richTextDirections.text = record.Directions;
    const shortFieldContainer = centerRightContainer.flxShortFieldsContainer.flxShortFieldsInnerContainer;
    shortFieldContainer.flxPrepTimeContainer.lblPrepTimeValue.text = record.PrepTime.toString()+" min";
    shortFieldContainer.flxCookTimeContainer.lblCookTimeValue.text = record.CookTime.toString()+" min";
    shortFieldContainer.flxServingsContainer.lblServingsValue.text = record.Servings.toString();
    this.view.AppData = record;
  },

  /**
   * Shows / hides expanded recipe card
   *
   * show: show card if ture
   */
  toggleExpandedRecipeContainer: function(show) {
    this.view.AppCardLarge.setVisibility(show);
    this.view.CardsContainer.setVisibility(!show);
    this.view.MainContainer.HeaderBar.flxCreateBanner.setVisibility(!show);
    this.view.MainContainer.HeaderBar.flxSearch.setVisibility(!show);
  },

  /**
   * This opens the expanded Recipe card and fills
   * it with data
   */
  onExCardOpenClick: function(record) {
    this.expandRecipeCard(record);
    this.toggleExpandedRecipeContainer(true);
  },

  /**
   * This is called when Edit has been clicked on the expanded Recipe card
   */
  onExCardEditClick: function() {
    this.toggleExpandedRecipeContainer(false);
    this.onCardEditClick(this.view.AppData);
  },

  /**
   * This is called when Delete has been clicked on the expanded Recipe card
   */
  onExCardDeleteClick: function() {
    this.onCardDeleteClick(this.view.AppData);
  },

  /**
   * This closes the expanded Recipe card
   */
  onExCardCloseClick: function() {
    this.toggleExpandedRecipeContainer(false);
  },

  /**
   * Show the About box
   */
  onClickShowAboutBox: function() {
    // this.view.AboutBox.setVisibility(true);
  },

  /**
   * Clear open menus
   */
  onClickMainContainer: function() {
    this.view.CardsContainer.flxCards.clearAllMenus();
  },
});

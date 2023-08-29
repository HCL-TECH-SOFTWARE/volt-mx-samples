/***************************************************
*Licensed Materials - Property of HCL.
*(c)Copyright HCL America, Inc. 2023
***************************************************/
const JAC = {
  LOGIN_FORM: "Login",
  MAIN_FORM: "Main",
  IDENTITY_SERVICE: "UserAuthentication",
  OBJECT_SERVICE: "FirstTouchRecipesObj",
  USER_OBJECT: "user",
  PREFERENCE_OBJECT: "userpreference",
  SIGNUP_OBJECT: "signuprequest",
  APPLICATION_OBJECT: "Recipe",
  ID_FIELD: 'x_0040unid',
  INGREDIENT_SEPARATOR: '@@@',
  DEFAULT_IMAGE_ATTACHMENT_NAME: 'imageAttachment',
  // TODO : may need to refer to metadata
  USERID_FIELD: "userid",
  FIRSTNAME_FIELD: "firstname",
  LASTNAME_FIELD: "lastname",
  DISPLAYNAME_FIELD: "displayname",
  NAME_FIELD: "name",
  AVATAR_FIELD: "avatar",
  ICON_PATH_FIELD: "icon_path",
  ICON_FIELD: "icon",
  EXEC_PATH_FIELD: "exec_path",
  TITLE_FIELD: "title",
  // Sort Constants
  SORT_BY_NAME: "NAME",
  SORT_BY_LAST_UPDATE_DATE: "UPDATE",
  SORT_BY_CREATION_DATE: "CREATE",
};

JAC.ERR_MSG = {
  SESSION_EXPIRED: 'Session expired! Please login again.',
  ACCESS_DENIED: 'Access denied'
}

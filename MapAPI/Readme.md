# Map API
## Overview
The Keychain API provides your app a mechanism to store chunks of user data (such as passwords) in an encrypted database. Using the Keychain API, your app can save users' credential information in the device's keychain. Keychain API app showcases the following APIs:

- [containsLocation](https://opensource.hcltechsw.com/volt-mx-docs/docs/documentation/Iris/iris_api_dev_guide/content/voltmx_map_functions.html#voltmx.map.containsLocation)
- [distanceBetween](https://opensource.hcltechsw.com/volt-mx-docs/docs/documentation/Iris/iris_api_dev_guide/content/voltmx_map_functions.html#voltmx.map.distanceBetween)
- [searchRoutes](https://opensource.hcltechsw.com/volt-mx-docs/docs/documentation/Iris/iris_api_dev_guide/content/voltmx_map_functions.html#voltmx.map.searchRoutes)

## Import the Application
After downloading the zip file of the Iris Project from GitHub, perform the following steps to import the application to Volt MX Iris.

1. Open Volt MX Iris.
2. From the main menu select **Project** → **Import** → **Local Project** → **Open as New Project**. Select the AccelerometerAPI zipped folder and click Open.


#### Note: Add your own Map API key to the project for the searchRoutes API key to work. To add the API key, open **frmMapSearchResult** form and search for **callSearchRoutefunc** function and add the API key to the **apiKey** tag. 

## Run the Application
To run the application in Volt MX Iris, follow these steps:

1. From the main menu bar select **Build** → **Run Live Preview**. This opens the Live Preview Settings window.
2. Select iOS or Android for Mobile under Native and click **Save & Run** to build the application. This opens a Live Preview is Ready dialogbox with a QR code.

## Preview the Application
To preview the built application on your mobile device, follow these steps:

1. Open the HCL Volt MX app installed in your mobile device.
2. Select the Wi-Fi tab and click **Scan QR Code** and scan the QR code displayed along with the dialog box. This launches the application.

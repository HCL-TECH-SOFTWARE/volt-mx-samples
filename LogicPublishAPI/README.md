# Volt MX-Logic-Nodejs-Contact-Sample

This app is an example that depicts how Node.js packages work in the Volt MX Foundry ecosystem. In this case, we have created a simple Node.js package where we have built APIs to create, read, update and delete a contact object. These APIs are running on the Foundry hosted Node.js infrastructure. In addition to that, this package also depicts how Volt MX’s Foundry identity service now seamlessly works with Node.js APIs. By default, all of the APIs are public except for the delete API which has anonymous protection. These can then be changed from within the Logic tab in the Foundry console.

This or any Node.js package uploaded to the Foundry console will fetch the required npm modules dynamically based on the details in the package.json. These modules will be fetched as part of the part of the package publish process.

These APIs can be used by any Foundry app and then they can be invoked from Volt MX Iris like a standard Foundry service.

Therefore, any Volt MX application’s backend can now be entirely serviced by a Node.js package running within the Volt MX Foundry infrastructure.


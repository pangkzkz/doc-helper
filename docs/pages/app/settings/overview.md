# Overview

There are 3 kinds of settings in `dochelper_app`, geared towards different stakeholders
for different use cases:

- Developer settings. These settings are meant for very basic app customization, such as database URL, cloud config, logging config, which features to enable... You will be interested in the developer settings if you deploy `dochelper_app` to your customers, or if you build extension for `dochelper_app` for developers. These settings are declared inside `flowsettings.py`.
- Admin settings. These settings show up in the Admin page, and are meant to allow admin-level user to customize low level features, such as which credentials to connect to data sources, which keys to use for LLM...
- [User settings](/pages/app/settings/user-settings/). These settings are meant for run-time users to tweak dochelper_app to their personal needs, such as which output languages the chatbot should generate, which reasoning type to use...

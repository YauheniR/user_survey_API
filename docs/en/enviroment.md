# Environment variables

[Русский](../ru/enviroment.md) | **English**

Part of the project settings is taken from environment variables. 
To define them, create a **.env** file next to **manage.py** in the **src** folder and write the data there in this format: **VARIABLE=value**.

The following variables are available:

- **PROJECT_HOST** - allowed hosts that django can access;
- **DEBUG** - debug mode. Set **True** to see the debugging information in case of an error. It is disabled by the value **False**.
- **SECRET_KEY** - the secret key for a specific Django installation.

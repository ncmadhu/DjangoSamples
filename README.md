1. Create a new virtual environment in python virtualenvwrapper using the command
mkvirtualenv <environmentName>
eg. mkvirtualenv djangoSamples
2. List available virtual environments using command
lsvirtualenv
3. Choose a virtual environment to work on using the command
workon <environmentName>
4. To exit virtual environment use the command
deactivate
5. To create a django project use the command
django-admin startproject <projectName>
eg. django-admin startproject djangoSamples
6. To create a django app use the command
django-admin startapp <appName>
eg. django-admin startapp sampleModels
7. Add the newly created apps and third party apps installed using pip to the settings.py under the INSTALLED_APPS
8. Add the necessary changes to the Database section in the settings.py file


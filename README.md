Ok, It's nice to meet you. I'm Phinehas.

I'm writing this in hope that you have a little to no knowledge in the Django project and a very healthy does of understanding in the Python Lang. 
So without any further ado, let'd dive in. Now i just realised that by saying that, I just further adoed. And now again 😂 

So let's dive in, shall we?
You should have created your django project and probably stuck trying to create your custom user model for your project. You're on the right repository.

To Start:
You want to create a user app in your project directory with the command- py manage.py startapp 'youruserappname'

Once that app is created, you should have some of the same files I have in my users folder in this repository.

Now you want django to be able to access that newly created user app you have, so now you navigate to your main project folder and to the settings.py
look for the list of INSTALLED_APPS amongst the already written code there.
Add 'youruserappname' to the list and don't forget to add a ',' after that.

Now back to your user app.

#### NOW MY CODE

## models.py

I imported some of the django models and methods to create our own Custom User model
AbstractBaseUser - A default django user model you'd be inheriting attributes from and overriding them to your preference
PermissionsMixin - A default django user model for certain superuser attributes you have to override 
BaseUserManager - Another default django model. This we are using to customize our user and superuser creation function
gettext_lazy - a django method to get users emails however case is typed by the user.
timezone - a django datetime method

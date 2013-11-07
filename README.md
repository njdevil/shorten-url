shorten-url
===========

A URL shortening app for Django


Install & Requirements
----------------------
This code was designed with Python 2.7 and Django 1.5.5
There are no additional packages required for use.
Just add the app to your settings.py file and clone the files into a directory under your project.
Then change the import lines (at the top of each file) to your project name, referenced by the ****


Overview
----------
There are various methods that can be employed to create a Shortened URL from a Long URL.  This package includes 2 methods.

The first, under the "URL" app, stores the request into the Database and presents the user with the Primary Key of the stored record.  The user then uses the link with the Primary Key appended to the URL and this Key is retrieved from the Database to obtain the original "long" URL.  This method will ensure that there are no duplicate records because the Primary Key of the Database is always set to UNIQUE.

The second method, under the "URLFORM" app, utilizes an Encryption Scheme to shield the internal Database Primary Key from the user.  There are various methods of how (and what) to encrypt, and this method utilizes the internal library "base64" to create 24-character string of any sized URL.  Alternatives for encryption include CRC32 checks (also an internal library, but slightly longer to process), or a custom alphabet of hard-coded characters is also possible (but with much longer code).  Furthermore, this URLFORM method encrypts the full URL string including the "http://".  Some alternative methods encrypt the Database Primary Key instead.


Operation
--------
The "URL" app does not utilize the Django Forms system and was designed as a straight-HTML proof-of-concept.  However, this app is fully operational.  The Database Primary Key is retrieved after the Database record is written, then presented to the user on a newly rendered webpage. 

The "URLFORM" app utilizes the Django Forms system and also features the Encryption Scheme.  The "long" URL strong is processed with the Base 64 encrpytion via "base64.urlsafe_b64encode".  This ensures that the base64 system will create a string that can be used in the URL.

For either app, the user is provided with a link to either the Primary Key (for the URL app) or to the base64 Encryption String (for the "URLFORM" app).  This link is processed through the main Urls.py and the App's Views.py  The "long" URL is retrieved and an HttpResponseRedirect is issued immediately redirecting the user to the appropriate website (as listed in the "long" URL).


Tracking
--------
On both apps, the Visitor's IP and the Date/Timestamp of the request is recorded.  No user login is required for use, but can be added if desired.


Extra
--------
The Django Decorator, "csrf_exempt" has been employed for ease of use & testing.

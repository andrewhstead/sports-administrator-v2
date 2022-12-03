# Sports Administrator v2

Sports Administrator is a Django-based content management system for the administration of sports games, clubs and leagues.  Version 1 of this project was begun in 2018 using an earlier version of Django, and the project is now being revived using Django 4.1.3.

## Apps

### Home

This will be the visible front end of the main website, introducing the product and the options available to the user.

### Data

The data app includes models which can be used by account holders, such as competitions, matches, and individual athletes.

### CMS

The CMS is what account holders will use to manage their installation. Competitions, tournaments and games can be created and people added. Live updates will also be available for some sports.

### Site Admin

The site admin app includes models which are used across the whole platform, such as the geographic database and the list of available sports, as well as the database of user with their permissions. It is designed to include all data which should not be accessible to account holders, only to staff.
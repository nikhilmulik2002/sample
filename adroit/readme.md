
## Adriod

### (Django Project)
Used to automate the manual tracking of the shipments, manipulate and generate reports. Scraping mailbox to extract important information and duping it to MongoDB. Manipulated user data and new reports generated from then information gets saved in Mysql DB. Notifying users through a email after each cycle of automation is performed. Allows users to access and manipulate information on the fly. 

### Flow of operation
- Read mails from client mailing server and dump them in MongoDB non-relational database.
- Script the saved data to extract required information and save it to Mysql DB.
- Display all information to UI using jqGrid JavaScript, user can modify/add the information if required. 
- Backend script with track shipments with respect to their flight details from tracking portals.


## Requirements

- Install packages from requirements.txt
- Create a Mysql DB from the process_it/models and configure it on settings.py
- Setup the Host details and mailing server details in view.py


## Usage

```js
python manage.py runserver
```
Note: Server starts on localhost by default. 







# myTrainer
#### Video Demo:  https://youtu.be/XA_vQfOTtMw
## Description:
The app myTrainer was designed to help a personal trainer professional to manage its trainee's / clients - not sure how call them in English - helping the personal trainer to set its plan such as personal trainer classes, training advisory, training consultancy or others; and differentiate plans into packages which let's the personal choose how many weekly meetings will happen with the client.

The app also will let the trainer registering its clients, control if the meetings happened or not, check for monthly and week performance, set months observations and control client's payment status. On the other hand, the clients can also register to the app. Since the client's email is the same used by the personal the clients have access to their own classes and payment status.

It is possible to have more than one personal trainer registered into the app and have its own clients independently without one accessing client's data from the other.

This necessity came from a real case and app will have a lot of improvements, such as:
- A page to register classes and packages; (at this point is being done through admin)
- Make the personal plans and packages independent;
- Add collors to classes status
- Let add more classes to the week (more than 4 times per week)
- Let add extra week (for cases when a month calendar uses 5 weeks according to the personal trainer)
- Set page to personal post important messages and invites to its clients
- Set a space to manage the train itself, like exercises, weigth, etc
- Set a place for training videos as a demonstration of the exercises
- Change the database to Postgree
- Code improvements
- Tests

and others, which I intent to keep doing as a personal project.

## Getting Started
- To use this application within your own network, as a debbug mode, you will:
  - Create a Python Virtual Environment into a folder which will holds the virtual env and project (This project was built using Python's version 4.2.2)
    ```Python
     project_folder_absolute_path $ virtualenv .
    ```
  - Activates your virtual env if not yet activated. You can use the commandline
    ```Powershell
     virtual_env_path $ source Scripts/activate
    ```
  - Install Django (This project was built using django's version 3.11.2)
    ```Python
     pip install django
    ```
  - Creates a folder into your virtual env. For example, 'src'.
    ```Powershell
     project_venv_absolute_path $ mkdir src
    ```
  - Clone this project into the 'src' folder.
  - Into src folder you can run migrations to create the database.
    ```Powershell
     project_venv_absolute_path $ cd src
    ```
    ```Python
     python manage.py makemigrations
    ```
    ```Python
     python manage.py migrate
    ```
  - Start the Django's default server and access through your browser connecting to the shown IP address.
    ```Python
     python manage.py runserver
    ```

  ### Setting a specific IP address into your private network
  If you want to access the application from your mobile or another pc and both are connected to the same network you can:
    - Open CMD or your corresponding Terminal and execute
    ```powershell
    $ ipconfig
    ```
    - Copy the corresponding IPv4.

    - In the myTrainer project, into settings.py, you will look for allowed_hosts and set this number into the constant list as a string. Example:
    ```python
    settings.py:
    (...)
    allowed_hosts = ['123.456.789.123']
    (...)
    ```
    - Then, you run the server into this IP and set a port. In our case we will use the port 80.
    ```python
    python manage.py runserver 123.456.789.123:80
    ```
    - Now, access this ip address into your computer, mobile or other device conected into this network. As the port is the '80', it's not necessary to write it into the web browser as it's a default port (insecure).


  <br>It's possible to also use othe mechanisms to set the application on cloud, but I didn't get this far yet. Also, there are cares you must take related to security in your network. It should be in mind that if you run on cloud, don't forget to deactivate the "debug mode", changes the database in case you have many mutual access and also check for security configuration.


  Lastely, some resorces must be changed into admin mode as they are not fully implemented into the application (yet).

## Resources
There are other specific resources used in this app. Basically is divided into two django apps: users and trainer. Users concentrates the most user related content as creating (register) and updating a user and user's profile, reset password, login and logout. This project is using the native django user object, extending it to a relation OneToOne to the user into client's object. This is a fundamental rule to avoid a personal trainer to wait a client to create an account to then the trainer creates all the rest. Trainer content holds all the other function related to personal trainer professional and client.

### Templates and URLs
The templates are located into specific 'templates' folder and urls.py holds the url's information, linking a web address to a special python function. Both templates folder and urls.py are presented into both apps folder.

### Features and Functions
Django is a free and open source Python framework for web development. It's design pattern is based on MVT (Model-Template-View) architecture where the Model is responsible for structuring and manipulating the data of the application and it comes with an object-relational mapper in which it's possible to describe the database layout in Python code; The Template is the user interface — what you see in your browser when a webpage is rendered to you. It is represented by HTML, CSS, Javascript and Jinja to manipulate data dynamically into the page itself; Finally, the View is responsible to encapsulate the logic for processing a user’s request and for returning the response receiveid through the URLs and also set the templates and dynamic content to be rendered in the template.

Django also has the concept of apps, where we can split the whole project into smaller focused pieces. The application has basically two apps, one called 'users' for users properties and the other is called 'trainer' for the trainers and app's general features. These are the features to be found in the application.

**User**

A user is any person registered to the platform. The main actions to be found for a user are:

- Home
  * URL: /
  * View: homeView(request)
  * Description and Rules: It renders the Homepage which presents a content restricted for logged users (login required) and other content for not logged users.


+ Register
  * URL: /register/
  * View: registerView(request)
  * Description & Rules: Allow anyone to create an account to the platform and select if is a personal trainer professional or not. When registering the user, three important things happen: a User object is created, there is a check for ClientProfile object registered with user's email to associate with eventual data created by client's personal trainer; and in case of Personal Trainer Professional is checked, a TrainerProfile is created and personal trainer permissions are given to the user.


* Login
  * URL: /login/
  * View: loginView(request)
  * Description & Rules: Authenticates a user in the platform checking the user through email and password. If the email and password are corrects or the user is already logged in, the user is redirected to the homepage. If the user's email and password doesn't match, a error message is shown and the user can try again.


+ Logout
  * URL: /logout/
  * View: logoutView(request)
  * Description and Rules: Logs an user out, i.e, unauthenticate the user. Login required.


* Password Change
  * URL: /change_password/
  * View: changePassword(request)
  * Description and Rules: Changes the actual user's password, first validating its actual password and then checking if the new one is valid or not by password rules, such as 8 characters, containing at least one lower case and one upper case; and must not be similar to email or username characters. Login required.


+ Profile View
  * URL: /profile/
  * View: userProfileView(request)
  * Description and Rules: Shows the user's name, last name and email. If a personal trainer profile, the user can also see its professional name. Login required.


* Profile Update
  * URL: /profile/update/
  * View: userProfileUpdateView(request)
  * Description and Rules: This page allows a user to edit it's own information, such as name and last name. If a personal trainer profile, the user can also edit it's own professional name. Login required. In both cases the email cannot be changed as it's used for credentials and also to associate a trainee/client to a personal trainer professional.


**Personal Trainer Professional**

A personal trainer professional is the user who has permissions to have trainees (or called clients / customers). This class allows a user to bring a professional name and also have access to add and manage customers.

* Clients List
  * URL: /trainer/clients/
  * View: clientsList(request)
  * Description and Rules: It brings a list of all customers from the logged in trainer professional. Login and personal_trainer permission required.


* Client Detail
  * URL: /trainer/client/<client_id>/
  * View: clientDetail(request, client_id)
  * Description and Rules: It brings client's info, such as name, email, hired package (frequency per week) and plan (offered service), due date (chosed payment date), monthly price and a bar to choose (or create) a train, i.e. a month control. If the user accessing is not the refered user or the trainer accessing is not the user's trainer, a 404 error is shown. Login required.


* Client Train
  * URL: /trainer/client/<client_id>/<pk_train>/
  * View: clientTrain(request, client_id, pk_train)
  * Description and Rules: Client's train brings a specific train from that customer. Each train is used as controller of frequency, i.e. to check if that month is already paid or not, if the trains were made or not and also set observations about that specific month. The trains can be selected throught a list of that particular client and ordered by the last train to the first. Login required to access this page and also checks whether or not the person requesting is the customer itself or its personal trainer profile, if not a 404 error is shown.


* Client Train Update
  * URL: /trainer/client/<client_id>/<pk_train>/update/
  * View: clientTrainUpdate(request, client_id, pk_train)
  * Description and Rules: This view allows the Personal Trainer to update his client's train, setting the classes status, payment status and observations. If changes are success the user is redirected to the client's train view. Login and Personal Trainer permission required. If the trainer accessing the link is not the customer's official trainer, the PermissionDenied error is raised.


* Client Create
  * URL: /trainer/clients/create/
  * View: clientCreate(request)
  * Description and Rules: Allows a personal trainer to create a new client object and set a name to that particular client, client's email, plan, package and payment date (days 5, 10 or 25 of each month). This object has the personal trainer linked to this client and also allows to create this object without the client creates an account. However, according to the client's email, if the client has or create a account, this object will be linked to this client's user. Login and personal trainer permission required.


* Client Train Create
  * URL: /trainer/client/<client_id>/create/
  * View: clientTrainCreate(request, client_id)
  * Description and Rules: Creates the month schedule to specific client. Before creating, the personal trainer can choose a starting date to the period which is a cycle to one month, i.e. 4 or 5 weeks period. If the period is not created yet, it's possible creating before the training itself. Othwerwise, the personal trainer chooses the date corresponding to the initial date of week 1 from that month and the training is created to that client. The dates are shown from the newst date to the farest date. If no client is found a 404 error raises. The initial dates are listed as unique values to avoid unecessary data to the database. The personal trainer to create the train must be the one who registered that client or a 404 error is risen. If everything's right, the train is created and the train update page is loaded. Login and personal trainer permission required.


* Start Period Create
  * URL: /trainer/new_date/
  * View: startPeriodCreate(request)
  * Description and Rules: Allows a personal trainer to create a new date as starting train period. These dates are unique to the database as it avoids multiple begining dates representing the same period. Login and personal trainer permission required.


* Client Edit
  * URL: /trainer/client/<client_id>/edit/
  * View: clientEdit(request)
  * Description and Rules: This function allows a personal trainer to edit the client's hired information, like package, plan, client's name to that client object (Not the same as the client's user name). When this information is saved, the function will look for a user with that particular email and if found will link the user to this client object. If the person requesting is not the client's personal trainer, a Permission Denied is risen. Login and personal trainer permission required.


**Trainee / Client**

At this point the trainee / client will have access to register its user, follow up messages into home page where yet there is no dynamic content. And follow it's train status. View only.


### Tech Stack
The following tools and languages were used in the construction of this project:

#### **Front-end**
- HTML
- CSS
- JavaScript
- Bootstrap

#### **Back-end**
- Python
- Django
- DB: SQLite

#### **Tools**
- Editor: Visual Studio Code
- Version control: Git
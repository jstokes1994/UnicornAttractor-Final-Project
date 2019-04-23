# Unicorn Attractor - Stream 5 Project (Full Stack Software Development Diploma)

This project required me to create a website drawing on all of the software
development techniques I have learned throughout the course. 

## Functionality

A user is able to register for the website and begin interacting with the 
community immediately. A user will fill in some personal information and have 
the opportunity to further edit their profile after registration.

The website essentially represents a hypothetical app in which users are given 
the ability to decide the direction of the app. It integrates ecommerce
functionality that allows users to suggest new features for the app for a fee. 
Other users can also donate for previously made features and the features with
the highest money donated will be worked on as priority. Users are also able to 
post any bugs they have found. Other users are able to 'like' the bug to inform
us they have also had a similar issue. Again most liked bugs will be worked on 
first. Users are able to comment on features/bugs to further incoorporate the
community feel the app is looking to promote.

The website includes a 'Stats' page which allows the community to track the
activity of the app. I incoorporated HighCharts to visualise the data generated
by the website. The page displays the traffic from within the site to give 
users a feel for the size of the community. It also includes the features/bugs
which are leading the way and therefore which will be worked on first.

The website only allows access to the features/bugs page if a user is logged
in and authenticated.

## Technologies Used

- Python 3.4.3
- Django 2
- BootStrap 3
- Google Fonts
- JavaScript
- CSS
- HTML
- threadedcomments
- Pillow
- Materialize
- jQuery
- django-vote

## Testing

#### Testing Registration

- Check that user is able to successfully register
- Check that username/email must be unique to others
- Check that user is immediately able to sign in after registration
- Ensure form validation is working correctly, especially with passwords
- Ensure a user is able to change their password
- Make sure a user is able to successfully update their details when editing
profile

### Testing Features/Bugs & Single Feature/Bug Page

- Ensure media queries work properly to show one feature per row on smaller
screens
- Ensure that the donation button works correctly and adds the correct amount
into the cart
- Ensure the comments system works on the single page and the link takes the
user back to the correct feature/bug after clicking link on thank you page
- Ensure after adding comment the comment count is correct
- Ensure that after donating for feature the 'money donated' field is updated
correctly
- Ensure the like button increases the amount of likes shown on the bugs/bug
page
- Make sure the same user is unable to like the same bug twice - the flash
message should provide feedback

### Testing Add Feature/Bug

- Ensure new features/bugs immediately show up on the respective pages after
creation
- Ensure the maximum character limit works for the description section
- Ensure the correct user is shown as the author

### Testing Cart

- Ensure that adding the same feature twice adds up the total and doesn't show
separately on the cart page
- Ensure smaller screens doesn't cause text overflow with differing number of
features in cart
- Ensure amending the donation amount works properly and updates in nav too
- Ensure the correct feature is being added into the cart
- Make sure the delete button completely removes the object from the cart

### Testing Checkout

- Ensure form validation is working
    - Typing in invalid card number 
    - Typing an expiry date in the past
    - Invalid security code
    - Leave a section blank in the user details section
- Correct feedback if payment is successful - redirection to features page
and a flash message informing user of a successful payment

#### Testing Stats Page

- Ensure when new user, new feature or new bug is added it is reflected on the
graphs
- Make sure when a donation is made that pushes into top 5 it is shown straight
away on stats page

[![Build Status](https://travis-ci.org/jstokes1994/UnicornAttractor-Final-Project.svg?branch=master)](https://travis-ci.org/jstokes1994/UnicornAttractor-Final-Project)


## Deployment

To Clone the project from github:

```python
$ git clone https://github.com/jstokes1994/online-cookbook.git
```

I recommend deploying the project in a virtual envioronment:

```python
$ cd directory-name
$ python3 -m venv virtual-env-name
```

You will need to install the dependencies found in the requirements.txt file:

```python
$ pip3 install -r requirements.txt 
```

To run the project locally use:

```python
$ python3 run.py
```

You can also run the app through Heroku.

The project was deployed to Heroku with config vars:

- IP = 0.0.0.0
- PORT = 5000

https://online-cookbook-js.herokuapp.com/

There are no differences between the development and deployed versions.

Note the project is written with Python3 and not Python2.


# The Cookbook Project

A project for the Code Institute

This is a non-for-profit site to fit the purpose, for users to share and exchange simple, quick and easy-to-cook and budget recipes. 
Prospective users can collaborate on a network basis and get added value in the daily routing and promotes healthy meals.
Users can upload data and get familiar with the full recipe list to cook after login authentication.

## Visualisation

An online version is deployed here (insert link). This app is hosted on Heroku,
and is based on the Flask framework and uses MongoDB (NoSQL Database). 

<img src="imgreadme/desktop.png" width=300> <img src="imgreadme/md.png" width=90> <img src="imgreadme/sd.png" width=55>



## User Experience

The app is meant for use by anyone with a passion for cooking, especially for people with limited time at dispose, 
but desire to prepare a quick meal. It allows interaction between between people with limited and broad experience 
in cooking. 

Main purpose is to achieve to be fast and clear result for the user, either by uploading a recipe or browsing through 
the existing content. This achieved by implementing simplified desing suitable for desktop and mobile screens.
The header provides a navbar which shrinks to a burger type collapsible menu when used on mobile. Both the header and 
the footer are designed in natural colours with emphasis on deep dark orange. 

When the user lands on the page sees an two cards with pictures. The first provides links to sign up or login. 
The second card is a sample teaser recipe with an expand button with activator class which hints some details and presents the full
picture of the meal. I implemented this a sort of teaser tool and presenting the limitations of user involvement 
without being logged in. After the login the user has access to a form to submit a recipe with various input fields provided. 
I included the culinary region to enrich the content, and make it more insteresting for the user checks the recipe afterwards
and the switch button lever that the user who has to confirm 'Yes, I have cooked this meal'. It provides additions human touch and
a brings more sense of reliability that this meal is for real.

In case the user is just visiting has an option just to check out the recipes list. Each recipe has a separate card with a picture 
and inviting buttons to find more about the recipe. The full recipe can be accessed by either clicking on the expand button or
or by clicking on the picture. Both actions are againg of the activator class. 

The footer give an option for contact the owner via social network links and provides convenient back-to-top button at the bottom right of the screen. The button has an easy 
to approach even on the mobile version.

## Technologies

1. Flask
2. PyMongo
3. MongoDB
4. Heroku
5. Bcrypt
6. Python
7. JavaScript
8. HTML
9. CSS 
10. Materialize 1.0.0

## Development process

Started with coding the app.py file and linking it to my MongoDB account. The initial part was based on what I have learned in 
the Code Institute. At some point adding the login authentication presented a challenge. However I received an inspiration from [this page](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login) 
at Digital Ocean. It was a nice starting point and along the way I decided to simplified it and keep it one python file because
the the form I use is rather basic. 

After more exploring more details I found [this tutorial](https://www.youtube.com/watch?v=vVx1737auSE) which presented the idea how encrypt the password in the mongodb database. I had to 
fix a bug for login process after wiring up the sign up process. The password stays encrypted using the Bcrypt format and
I don't have access to the actual password of the user. At some point the media upload provided limited options. MongoDB is document 
based and storing pictures is not recommened. Hence, I decided to store the picture by converting it to a string to fit in the
database. To improve the uploads each picture size is restricted to 4MB. 

The entire CSS styling was done near the end of the project. The styles of the app stick to the Materialize framework. In order to stick to simplified approach I tried to resort as less as possible to custome 
css in the static folder. Interestingly Materialize does not provide style input for the login page, more specifically for the username input form validation. 
When I tried to use the input form it changed the style of the form. Therefore I stick to the email validation offered by Materialize.  


## Testing

### Manual Testing

First testing was done on the login page which required some bug fixing to come up the fix in final version of the code in line
line 87. After I need to make sure that routing differs wheather user is in login session. Testing the CRUD framework for creation, 
read, update and delete is in place took the great part of the tests. It needed to make sure is managing the right document.

I used the Firefox browser and was constantly testing it for content consistency with Chrome. Hence there are no additional issues 
with the compatability. After completion of the final version manual test for compatability were done for Safari and Microsoft Edge 
browser. The back to top button was additionally modified with line of code inside the function '''document.body.scrollTop = 0;'''. 
Hence the page is compatable with the Safari browser.


## Features

The start page section indroduces the sections for login. It possess a navbar menu to navigate accross the sections.
Once landed on the start page the user can read only. Only after signing up in the app, allows the user to provide input.
The mandatory login feature serves as a filter the content. 

The share recipe section present the user with a contact form where can provide the recipe specifics. Before posting the recipe, 
the uploader needs to provide with the name of the recipe and region or country of origin which represents. The field do not 
have restictions for word count. Each user can provide a detailed explanation as possibel. After filling the ingredients and 
a the cooking steps, a photo the user needs to submit a date of the upload. All fields have html validations. The last field
before sending the recipe the user needs to confirm that had cooked the recipe. Many test users have found this feature nice
to have as it prompts some self-accountability in the user. 

After the upload the recipe is listed in the Recipes section. There each recipe has own card consistent with the sample recipe card 
included in the landing page. There are two levels of interaction there. First one get you acquinted with the card by pictire uploaded 
in the form with buttons to find more. Second level triggers the actual recipe with the instructions and the details needed. 

### Features Left to Implement

Score rating - the button to Rate the recipe is wired up to another collection in MongoDB. Still does not provide the reviews 
output. I indend to add a two level of scoring system, 1) score 1 to 5; 2) review text with limited word count. This way the 
review rating will be included in the recipe card. The average score will be visible at the first level and the full review list 
would be accessed by another button.

User profile - such feature will take the app to the platform level and can become for profit type. Each user can be visible to 
some extent and other user can see the recipes listed by the user. 

A chatbox could be nice to have next to each recipe card. It will be an option to ask the uploaded questions. 

### Know issues

Coooked meal shows ON - and Datepicker
The rate button on the recipe card is not entirely wired up with the website. It has a collection in MongoDB for reviews but 
is still a feature that needs to be implemented. I indend to add it a ratings key nested in each recipe document.

## Credits

### Content

I have written all text and published the existing recipes.
All media in the form of picteres are either my own or taken from [Pexels.](https://www.pexels.com)

### Acknowledgements

The JQuery code that triggers the navbar on mobile and the datepicker form was taken from the Materialize [website.](https://materializecss.com/) 

The steps needed to add back to top button was taken from [here.](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)

Guiding steps on the flask login feature can be found [here](https://www.youtube.com/watch?v=vVx1737auSE). The video tutorial
with the more guiding steps can be found [here](https://www.youtube.com/watch?v=vVx1737auSE). Both served as guidance and we not
taken litterally as shown in the tutorials.


## Instalation

I used GitPod for this project and if you'ra planning to clone the repository here are the commands. Please start with this
command line to make sure all frameworks are in place:

```pip3 install flask
   pip3 install flask_pymngo
   pip3 install dnspython
   pip3 install -r requirements.txt
```

The GitPod editor doesn't ask for ```sudo``` before ```pip3``` in the command, but most editors require it. 
I used environmental variable and secret key to connect the app with the database which are know only be mu.
This Flask framework website provides sufficient details how to create your you environmental variable and
add secret key.








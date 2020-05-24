The Cookbook Project

Milestone Three for the Code Institute

This is a non-for-profit site to fit the purpose, for users to share and exchange simple, quick and easy-to-cook and budget recipes. 
Prospective users can collaborate on a network basis and get added value in the daily routing and promotes healthy meals.
Users can upload data once logged in and 

Visualisation

An online version is deployed here (insert link). This app is hosted on Heroku,
and is based on the Flask framework and uses MongoDB (NoSQL Database). 

screenshot 

screenshot 

screenshot 


User Experience

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

Technologies

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

Development process

Started with coding the app.py file and linking it to my MongoDB account. The initial part was based on what I have learned in 
the Code Institute. At some point adding the login authentication presented a challenge. However I received an inspiration from [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login) 
at Digital Ocean. It was a nice starting point and along the way I decided to simplified it and keep it one python file because
the the form I use is rather basic. Another tutorial presented the idea how encrypt the password in the mongodb database. I had to 
fix a bug for login process after wiring up the sign up process. The password stays encrypted using the Bcrypt format and
I don't have access to the actual password of the user. At some point the media upload provided limited options. MongoDB is document 
based and storing pictures is not recommened. Hence, I decided to store the picture by converting it to a string to fit in the
database. To improve the uploads each picture size is restricted to 4MB. 

https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

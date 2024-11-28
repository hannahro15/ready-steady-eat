# Online Food Shop Project (Milestone 4)
 
 An online food shop that sells meals and fresh food products.

 # UX

 ## User stories

 ### Registration and Login
 - As a user, I should be able to easily register for an account, so I have a personal account and their profile.
 - As a user, I should be able to log in to my account, so that I can see the relevant information on my account.
 - As a user, I should be able to log out of my account to keep my account safe and secure.
 - As a user, I should receive a confirmation email after registering to confirm that my registration went through and was succesful.
 - As a user, if I forget my password I should easily be able to recover it, so I am able to access my account again and log in.
 - As a user, I should have a personalised profile so I can have access to my personal information, my orders, and update payment information.

 ### Food/Meal Products and Checkout
- As a shopper, I should be able to view a list of my products and on the relevant pages, so I see the items and purchase them.
- As a shopper, I should be able to view the product details of each product, so that I see further information about it such as the name, image, dietary/cooking requirements symbols, and description.
- As a shopper, I should be able to search and filter the various meals/food in the search bar, so it can help me to find items that are relevant to what I am looking for.
- As a shopper, I should be able to see the total of items that are added to my cart so I can see how much my order costs.
- As a shopper, I should be able to add and remove items from my cart, so I can amend items I need to when I add it to an order.
- As a shopper, I should be able to edit quantity of items that are in my basket before I pay, so I can order the right amount of products that I need.
- As a shopper, I expect the payment to go through succesfully without any errors, so that I can purchase what is in my basket.

### Other/General
- As a user, it should be clear what the purpose of the website is, what it is about, and what content is in it, so I can decide if I want to explore and view the website further.
- As a user, I should be able to easy navigate across the website, to improve the user experience, so I find the information easily that I am looking for.
- As a user, I expect the website to be responsive on different screen sizes on mobile, tablet, and desktop, so I can view everything easily on the website.
- As a user, I want be able to see the FAQ page, so I can find out the relevant information to any queries or general information that I may need.
- As a user, I want to be able contact the company on the contact us page, so I can request inforamtion that I need or ask general queries.
- As a user, I want to be able to view various offers and subscriptions listed on the home page, so I can decide whether to go ahead with using any of them before I purchase any items.

## Wireframes 
### Home Page - Mobile
![Home Page - Mobile](wireframes/home-page-mobile.png)
### Home Page - Desktop
![Home Page - Desktop](wireframes/home-page-desktop.png)
### Products Page - Mobile
![Products Page - Mobile](wireframes/products-page-mobile.png)
### Products Page - Desktop
![Products Page - Desktop](wireframes/products-page-desktop.png)
### Product Details Page - Mobile
![Product Details Page - Mobile](wireframes/product-details-page-mobile.png)
### Product Details Page - Desktop
![Product Details page - Mobile](wireframes/products-page-desktop.png)
### Checkout Page - Mobile
![Checkout Page - Mobile](wireframes/checkout-page-mobile.png)
### Checkout Page - Desktop
![Checkout Page - Desktop](wireframes/checkout-page-desktop.png)
### Contact Page - Mobile
![Contact Page - Mobile](wireframes/contact-mobile.png)
### Contact Page - Desktop
![Contact Page - Desktop](wireframes/contact-desktop.png)
### FAQ Page - Mobile
![FAQ Page - Mobile](wireframes/faq-mobile.png)
### FAQ Page - Desktop
![FAQ Page - Desktop](wireframes/faq-desktop.png)

## Deployment to Heroku

Go to Heroku.com and implement the following steps in this order:

1. On the home page, click 'New' and in the dropdown, click on 'Create a new app'.
2. Add app name (This name must be unique, and have all lower case letters. Also use minus/dash signs instead of spaces.)
3. Select Region (Select the most relevant region, mine is Europe)
4. Click the button that says 'Create App'.
5. Click on the Deploy tab near the top of the screen.
6. Where is says Deployment Method click on Github.
7. Below that, search for your repo name and add that.
8. Click connect to the app.

Before clicking below on enable automatic deployment do the following:

1. Click on the settings tab
2. Click on reveal config vars.
3. Add in your variables from your env. files as key value pairs. 
4. Go back and click on the Deploy tab.

Before the app can be connected, push the following new files below to the repository. Go back in the terminal in your coding environment and add the following:

1. git status
2. git add requirements.txt
3. git commit -m "Add requirements.txt file"
4. git add Procfile (web: gunicorn ready_steady_eat.wsgi:application)
5. git commit -m "Add Procfile"
6. git push

Head back over to Heroku where the Deploy tab is.

1. Click 'Enable Automatic Deploys'
2. Click Deploy Branch. (Should be a main or master branch)
Heroku will receive code from Github and build app with the required packages. Hopefully once done the 'App has successfully been deployed message below' will appear. 
3. Click 'View' to launch the new app. 
The deployed link of the app is https://ready-steady-eat-8febfd678f9f.herokuapp.com/

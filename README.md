# Ready, Steady, Eat! (Milestone 4)
 
 An online food shop called Ready, Steady, Eat! that sells meals and fresh food products for my Milestone 4 project. This ia Full-Stack Django E-commerce project based on the Boutique Ado project. It is customised and contact and faq pages added in with models.

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
- As a shopper, I should be able to view the product details of each product, so that I see further information about it such as the name, image, and description.
- As a shopper, I should be able to search and filter the various meals/food in the search bar, so it can help me to find items that are relevant to what I am looking for.
- As a shopper, I should be able to see the total of items that are added to my cart so I can see how much my order costs.
- As a shopper, I should be able to add and remove items from my cart, so I can amend items I need to when I add it to an order.
- As a shopper, I should be able to edit quantity of items that are in my basket before I pay, so I can order the right amount of products that I need.
- As a user I should be able to add, edit, and delete product listings so I can update the website accordingly.
- As a shopper, I expect the payment to go through succesfully without any errors, so that I can purchase what is in my basket.

### Other/General
- As a user, it should be clear what the purpose of the website is, what it is about, and what content is in it, so I can decide if I want to explore and view the website further.
- As a user, I should be able to easy navigate across the website, to improve the user experience, so I find the information easily that I am looking for.
- As a user, I expect the website to be responsive on different screen sizes on mobile, tablet, and desktop, so I can view everything easily on the website.
- As a user, I want be able to see the FAQ page, so I can find out the relevant information to any queries or general information that I may need.
- As a user, I want to be able contact the company on the contact us page, so I can request inforamtion that I need or ask general queries.

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

# Database Schema

Please see below a screenshot of a Database Schema for my models of my project which I created using Django-extensions and PygraphViz. I found about this via the Code Institute Slack Channel.

![Database Schema](documentation/models.png)

As you can see from the model above, my two custom models that I created were the contact form and the FAQ's, which are both within the contact app. Not all apps used models so are not on the Schema.

# Technologies Used

The technologies I used for creating the project were HTML, CSS, Javascript, JQuery, Python, Django, Bootstrap 4, AWS, Heroku, Github, Git, and the Stripe API.

# Features

## Home Page

![Home Page](documentation/site-photos/home-page-screenshot.png)

A home page introducing the website and it's purpose for users.

## All Products Page

![All Products Page](documentation/site-photos/products-screenshot.png)

A page where all the products are shown.

## Individual Product Pages (This is for the main courses!)

![Main Courses](documentation/site-photos/individual-product-page-screenshot.png)

Pages where products for different categories are shown.

## My Shopping Bag Page

![My Bag](documentation/site-photos/bag-screenshot.png)

A page where users can see their items before going to the checkout page.

## Checkout Page

Checkout (top half)
![Checkout Page 1](documentation/site-photos/checkout-one-screenshot.png)

Checkout page (bottom half)
![Checkout page 2](documentation/site-photos/checkout-two-screenshot.png)

Where users checkout and pay for items. The screenshot doesn't show the payment bit which is lower down on the page!

## Contact Page

![Contact Page](documentation/site-photos/contact-screenshot.png)

Where users can contact Ready, Steady, Eat! with queries.

## FAQ Page

Non-admin photos for this.
![FAQ Page](documentation/site-photos/faq-screenshot.png)

With the edit and delete and add FAQ's for admin.
![FAQ Page](documentation/site-photos/faq-admin-screenshot.png)

Where users can see frequently asked questions. There are options from this page for admin's to add, edit and remove faq's.

## My Profile Page

![Profile Page](documentation/site-photos/profile-screenshot.png)

Where you users have access to their own profile.

## Product Management Page (For adding products)

![Product Management page](documentation/site-photos/add-product-screenshot.png)

Where the admins are can manage products in the shop. There are also from the products page when logged in as an admin an option to edit products which has a very similar looking form.

## Sign Up Page

![Sign Up](documentation/site-photos/sign-up-screenshot.png)

## Sign In Page

![Sign In](documentation/site-photos/sign-in-screenshot.png)

## Future Features

- Make titles dynamic on product pages
- Have an option to stop products and FAQ's being deleted on one click.
- Add a rating and reviews system
- Add in more products to the site
- Add a wishlist
- Set up a subscribe option with a monthly newsletter

# Testing

## Bugs

### Fixed bugs 

- Fixed footer so it is at the bottom of the page.
- Made images all the same size so it looks more uniform in the product containers.
- Footer overlapping content in page on some pages.
- Order total showing zero amount on order confirmation and in profile after adding product to basket and going through the checkout procedure. Small fix within the template tags in the html.
- Small responsiveness issue on the bag page on mobile devices.

### Unfixed bugs 

- Images a little slow loading the page.
- Order confirmation email doesn't actually send to an email but confirmation message does appear on the checkout success page once order is placed. Emails are received ok for verification when registering and also for forgotting a password. This was checked using a temp email address on https://temp-mail.org/en/.

## Validation

### HTML Validation

I have validated all the html files (not the all auth ones) by copying the url in the html validator, and can confirm the are without errors. 

![HTML Validator Screenshot](documentation/validation/html-validator.png)

HTML Validation Checks Below:

| Page      | Checked with HTML Validator with no errors (Yes or No)  |
| ------    | ------- |
| index.html | Yes |
| profile.html | Yes |
| register.html | Yes |
| login.html | Yes |
| products.html | Yes |
| product_detail.html | Yes | 
| bag.html | Yes |
| checkout.html | Yes |
| checkout_success.html | Yes | 
| contact.html | Yes (Errors only from the backend as from details in forms.py) |
| success.html (contact form success page) | Yes |
| add_product.html (on product management page) | Yes |
| edit_product.html | Yes |
| faq.html | Yes |
| add_faq.html | Yes |
| edit_faq.html | Yes |

Errors on the contact page due to the fact that the contact form is like a table and it is coming from the backend.

### CSS Validation

I have validated all the css files within each of the apps and I can confirm there were no errors and everything is validated.

![CSS Validation Screenshot](documentation/validation/css-validation-screenshot.png)

### JS Validation

I have validated the JavaScript and everything runs without error, apart from some ES6 ones which I have ignored.

### Python Validation

This is has been thoroughly tested using flake8 extension and the only errors that remained are mostly in settings.py and models which I have decided to ignore. All validation issues within views, urls etc. are all clear of errors. There are odd other errors, but these were issues that were originally from the Boutique Ado such as the 'except' error.

## Google Lighthouse Testing

## Home Page - Mobile

![Home Page - Mobile](documentation/lighthouse/lighthouse-home-mobile.png)

## Home Page - Desktop

![Home Page - Desktop](documentation/lighthouse/lighthouse-home-desktop.png)

## All Products Page - Mobile

![All Products Page - Mobile](documentation/lighthouse/lighthouse-products-mobile.png)

## All Products Page - Desktop

![All Products Page - Desktop](documentation/lighthouse/lighthouse-products-desktop.png)

## My Basket/Shopping Bag Page - Mobile

![My Basket - Mobile](documentation/lighthouse/lighthouse-bag-mobile.png)

## My Baske/Shoopping Bag Page - Desktop

![My Basket - Desktop](documentation/lighthouse/lighthouse-bag-desktop.png)

## Contact Page - Mobile

![Contact Page - Mobile](documentation/lighthouse/lighthouse-contact-mobile.png)

## Contact Page - Desktop

![Contact Page - Desktop](documentation/lighthouse/lighthouse-contact-desktop.png)

## FAQ Page - Mobile

![FAQ Page - Mobile](documentation/lighthouse/lighthouse-faq-mobile.png)

## FAQ Page - Desktop

![FAQ Page - Desktop](documentation/lighthouse/lighthouse-faq-desktop.png)

# Manual Testing

Through testing my app during the development stage these are the testing results of my manual tests based on my user stories above.

### Registration and Login
 - As a user, I can easily register for an account, so I have a personal account and their profile.
 - As a user, I am able to log in to my account, so that I can see the relevant information on my account.
 - As a user, I am able to log out of my account to keep my account safe and secure.
 - As a user, I can confirm that I do receive a confirmation email after registering to confirm that my registration went through and was succesful.
 - As a user, if I forget my password I can easily recover it, so I am able to access my account again and log in. This has been tested and an email sent for forgotten passwords.
 - As a user, I can confirm that I have a personalised profile so I can have access to my personal information, my orders, and update payment information.

 ### Food/Meal Products and Checkout
- As a shopper, I can confirm that I can see a list of my products and on the relevant pages, so I see the items and can purchase them.
- As a shopper, I can confirm that I can view the product details of each product by clicking on the image, so that I see further information about it such as the name, image, and description.
- As a shopper, I can confirm that I can search and filter the various meals/food in the search bar, so it can help me to find items that are relevant to what I am looking for.
- As a shopper, I can confirm that I am able to see the total of items that are added to my cart so I can see how much my order costs.
- As a shopper, I can confirm that I can add and remove items from my cart.
- As a shopper, I can confirm that I am able to edit quantity of items that are in my basket before I pay, so I can order the right amount of products that I need.
- As a user I can confirm that I am able to add, edit, and delete product listings so I can update the website accordingly.
- As a shopper, I can confirm that the payment to go through succesfully without any errors, so that I can purchase what is in my basket. This goes through via Stripe on the backend.

### Other/General
- As a user, it is clear what the purpose of the website is, what it is about, and what content is in it, so I can decide if I want to explore and view the website further.
- As a user, I can confirm that I can easily navigate across the website, to improve the user experience, so I find the information easily that I am looking for.
- As a user, I can confirm that the website is responsive on different screen sizes on mobile, tablet, and desktop, so I can view everything easily on the website.
- As a user, I can see the FAQ page, so I can find out the relevant information to any queries or general information that I may need. As an admin you can add, edit, and delete FAQ's.
- As a user, I can confirm that I can contact the company on the contact us page, so I can request inforamtion that I need or ask general queries. This contact form goes to the database once submitted.

# Credits

### General

* [Canva](https://www.canva.com/) - or creating and designing the logo

* [Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes

* [Gitpod](https://www.gitpod.io/) - For working/completing on my project

* [Github](https://github.com/) - To store my project online

* [Heroku](https://id.heroku.com/login) - For deploying the project and storing the env variables.

* [Django Secret Key Generator](https://djecrety.ir/) - For generating a Django secret key.

* [Rgb color code website](https://rgbcolorcode.com/) - For choosing colours

* [Readme Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links) - For markdown documentation for the ReadMe

* [ChatGPT](https://openai.com/index/chatgpt/) - For general debugging and spotting basic syntax errors such as urls not working.

* [Am I responsive](https://ui.dev/amiresponsive) - For testing responsiveness and also for taking screenshots of the different pages on the website.

### Images

* [Pexels](https://www.pexels.com/photo/photo-of-building-in-chetham-manchester-11856438/) - For the food product images

* [Pixabay](https://pixabay.com/) - For the food product images

* [Font Awesome](https://fontawesome.com/icons) - For the icons used for the social links in the footer.

* [Croppola](https://croppola.com/) - For cropping and re-sizing the food images so they are all the same height and width.

### Validators/Testing

* [HTML Validator](https://validator.w3.org/) - HTML Validator

* [CSS Validator](https://jigsaw.w3.org/css-validator/) - CSS Validator

* [PEP8 Python Validator](https://pep8ci.herokuapp.com/#) - Python Validator

* [JS Hint](https://jshint.com/) - For validating my Javascript code

* [Page speed Insights/Lighthouse](https://pagespeed.web.dev/) - For testing performance, accessibility, best practices and SEO on all pages I used a website called Page Speed Insights

### Content/Documentation

* For sorting out the whitespace under the footer issue I used some of the code on [this webpage](https://www.30secondsofcode.org/css/s/footer-at-the-bottom/). The website is called the 30 seconds of code website and the page is about the footer being on the bottom.

* [Django website](https://www.djangoproject.com/) - For Django documentation

* [W3 schools](https://www.w3schools.com/) - For general documentation

* [Bootstrap 4](https://getbootstrap.com/docs/4.0/layout/grid/) - For the relevant documentation

* For the django contact form views - [Django contact form views](https://mailtrap.io/blog/django-contact-form/#How-to-validate-and-verify-data-from-a-contact-form)

* For styling the django contact form - [Django contact form styling](https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa)

* All content for the products were written myself.

* This project was based on the Boutique Ado Walkthrough on the LMS as the Code Institute with additional features in and customised to my own project by adding in a contact app that has a contact and faq page with models for both of them.

## Acknowledgements

A big thanks to the support from my mentor at the Code Institute, my facilitator at the City of Bristol College, and the Code Institute Slack Community and Tutor Support for assistant on my Milestone 4 project.

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

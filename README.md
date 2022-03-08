<h1 align="center">Scrawndog Media</h1>

### **Live Site**
[Scrawndog Media Repository](https://github.com/JamesFahey/project4-scrawndogmedia)

### **Repository:**
[Scrawndog Media Site](https://scrawndogmedia.herokuapp.com/)

# About

My ambition is to create a functioning and responsive website for photography and videography business, Scrawndog Media. The website will allow users to book the owners services for a number or events or organise a personal shoot for themselves or family. 

The sites purpose is to enable effective management and handling of bookings and work load for the owners. Allowing the owner to take bookings and manage their diary of upcoming events. Designed to grow with the business itself. Popularity growth will correlate to additional features being made available, with user experience a priority


 

# Table of Contents

# User Experience
## User Stories
### Epic: As a site user/admin I have the option to register or sign into the site
- As a site owner I can access an admin page so that I can manage site content 
- As a site user I can register an account so that I can book an event
- As a site user/owner I can sign in and out so that I can easily access my account

### Epic:  As a site user/admin I can create and view bookings
- As a registered user I can book an event through the site so that I do not need to call
- As a registered user I can click on a booking so that I can see all information for that booking
- As a registered user I can see my booked events so that I can keep track of bookings
- As a user I can see upcoming bookings so that I can see which dates are available

### Epic:  As a site user/admin I can edit and delete bookings
- As a site user/ business owner I can edit booked events so that I can manage my bookings
- As a site user/ business owner I can cancel bookings if necessary

### Epic:  As a site admin I can manage my diary and confirm bookings
- As a Business owner I can confirm booking request so that I can manage my workload
- As a business owner I can order and filter bookings to better manage my diary

### Epic: As a business owner I can promote the brand
- As a Business owner I will have the brands logo prominent on the home page
- As a Business owner I can add my work to the site for users to see 

For my user stories and epics I have taken an Agile approach. 

After creating my user stories, I assigned each a tag with varying levels of importance. These ranged from the most important tag ‘Must have’, ‘Should have’ for the features which should be included and the least important tagged ‘could have’. I attached a user story with a fourth tag of ‘Won’t do’ as it will not be implemented during this project however it would be beneficial to add at a later date.

Once all user stories had been finalised, I created Github Project in a Kanban format. Using these project boards allowed for greater ease in organising and prioritising my work. My project board was comprised of columns labelled; To do, In progress, Done and Future content. All user stories, known as issues in the project, began in the ‘To do’ column and progressed them throughout the project.

<img src="assets/readme_imgs/planning/agile_user_stories.png" width="50%">

# Features

### Home page and landing image for all users. 

This image was chosen to convey to the user one of the primary services the site will be offering. The business logo is also positioned centrally where the users eyes will be initially drawn promoting the brand as soon as a user visits the site.

<img src="assets/readme_imgs/features/landing_page.png" width="50%">

### Nav bar – all users

The navbar for all users will focus on promoting the business highlighting previous work and services on other

<img src="assets/readme_imgs/features/navbar1.png" width="50%">

### Nav bar – registered users

Once registered users will have access to more options such as booking forms, booked events and a business calendar

<img src="assets/readme_imgs/features/navbar2.png" width="50%">

### Portfolio

Here the site owner can promote their latest work with the goal of generating further business

<img src="assets/readme_imgs/features/portfolio1.png" width="50%">

<img src="assets/readme_imgs/features/portfolio2.png" width="50%">

### Social links

Social links for users to follow the business’ social platforms

<img src="assets/readme_imgs/features/social_links.png" width="50%">

### Sign up

From the sign up page users can register in order to access the rest of the site

<img src="assets/readme_imgs/features/signup.png" width="50%">

### Log in

A log in page for returning users

<img src="assets/readme_imgs/features/signin.png" width="50%">

### Log out

Users will be asked to confirm their decision to log out

<img src="assets/readme_imgs/features/logout.png" width="50%">

### Events page

Here registered users can view their booked events. They will be listed in date order and also indicate whether they have been accepted or still waiting for an update from the site owner. Users will also have the option to either edit or delete their events.

<img src="assets/readme_imgs/features/event_page.png" width="50%">

### Event details

Users will be able to click on bookings in order to see all of the bookings information

### Booking form

Here registered users can complete a booking form for any of the events on offer. Once the form has been completed their events page will be updated with the request and they will be notified that someone will be in contact shortly.

<img src="assets/readme_imgs/features/booking_form.png" width="50%">

### Edit form

If the user decides to edit one of their events they will follow the link to a prepopulated form, with the previous details provided, where they can make changes to any of the fields

<img src="assets/readme_imgs/features/edit_form.png" width="50%">

### Delete event

If the user decides to delete an event, they will be directed to a page to confirm their decision. They will also be provided with information regarding refunds.

<img src="assets/readme_imgs/testing/delete_booking.png" width="50%">

### Calendar

Registered users will be able to view the current months calendar in order to see which dates are available

<img src="assets/readme_imgs/features/calendar.png" width="50%">

# Site Design

For the site I used a boostrap template from startbootstrap.com called creative. I have updated images and colours to fit the style of the brand

### Fonts

I chose not to update the fonts used by the template as I felt it worked well with the brand design.

The primary font used was Merriweather

### Colour scheme

The colour scheme has been chosen to complement the predominant colour of the logo. With the logo colour being a dark shade of purple, I used google to find further colours to use for the site

- color: # 351c44| This is the colour of the site logo and has been used for sections of the home page, ‘At your service’ text, submit buttons throughout the site, social links
- color: # 9CAF88| Hover effects offer a good contrast to the primary colour of the logo.
- color: # fffff| white has been used for large portions of text as it offers good contrast to the background image and colour scheme
- color: # b69426| used for the hover effect on the navigation links

### Balsamiq Wireframes

   * [Desktop](assets/readme_imgs/wireframes/desktop/)

   * [Mobile](assets/readme_imgs/wireframes/mobile/)

### Structure

I have kept the structure simple and clean to not overload the customer. The homepage contains information the promote the business and highlight the owners previous work. 
The website focuses on a booking app for events.

All visitors to the site can view brand information and portfolios however a user must register/login to have access to:

- Book Event
- Your events
- Calendar
- Edit Event
- Delete Event

# Testing

### Unittesting

I predominantly chose to do manual testing but to demonstrate unittesting I chose to focus on the url.py. I carried out 8 tests all coming back successfully

### Manual Testing by User Story

### Epic: As a site user/admin I have the option to register or sign into the site
From the home page users can access either the register/signup or log in page by using the nav bar situated at the top right of the page
- As a site owner I can access an admin page so that I can manage site content 
A superuser was created allowing access to an admin page. There the owner has access to all backend information including users and bookings
- As a site user I can register an account so that I can book an event
Once a user has registered, they will be granted further site access including a booking page

### Epic:  As a site user/admin I can create and view bookings
- As a registered user I can book an event through the site so that I do not need to call
- As a registered user I can click on a booking so that I can see all information for that booking
- As a registered user I can see my booked events so that I can keep track of bookings
- As a user I can see upcoming bookings so that I can see which dates are available

### Epic:  As a site user/admin I can edit and delete bookings
- As a site user/ business owner I can edit booked events so that I can manage my bookings
- As a site user/ business owner I can cancel bookings if necessary

### Epic:  As a site admin I can manage my diary and confirm bookings
- As a Business owner I can confirm booking request so that I can manage my workload
- As a business owner I can order and filter bookings to better manage my diary

### Epic: As a business owner I can promote the brand
- As a Business owner I will have the brands logo prominent on the home page
- As a Business owner I can add my work to the site for users to see
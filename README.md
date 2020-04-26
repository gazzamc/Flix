[![Build Status](https://travis-ci.org/gazzamc/Milestone-Project-Four.svg?branch=master)](https://travis-ci.org/gazzamc/Milestone-Project-Four)

# Flix - Content Streaming Website
Full Stack Frameworks with Django Milestone Project - Code Institute

The is a content streaming website built using `Django`, `Python`, `Javascript` and `Bootstrap`. 
The user can like, dislike and add videos to their watchlist. Using the `Stripe` API the user has a choice of 
different tiers they can subscribe to in order to view the content. 
All the video URLs are fetched from youtube using the `youtube-dl` module.

## Table Of Contents:
- [Demo](#demo)<br>
- [UX](#ux)<br>
    * [User Stories](#user-stories)<br>
    * [Strategy](#strategy)<br>
    * [Scope](#scope)<br>
    * [Structure](#structure)<br>
    * [Skeleton](#skeleton)<br>
    * [Surface](#surface)<br>
- [Database Schema](#database-schema)<br>
- [Features](#features)<br>
- [Features left to Implement](#features-left-to-implement)<br>
- [Technologies Used](#technologies-used)<br>
- [Testing](#testing)<br>
    * [Manual Testing](#manual-testing)<br>
    * [Automated Testing](#automated-testing)<br>
    * [Known Bugs](#known-bugs)<br>
- [Deployment](#deployment)<br>
- [Credits](#credits)<br>
    * [Content](#content)<br>
    * [Media](#media)<br>
    * [Acknowledgements](#acknowledgements)<br>

## Demo
You can try the live version of the API [Here]()<br><br>
<p align="center">
<img src="" alt="Responsiveness" width="80%">
</p>

## UX

#### User Stories
- As a user I should be like/disliek videos.
<p align="center">
<img src="" alt="Like/Dislike" width="80%">
</p>

- As a user I should be able to add videos to a watch list.
<p align="center">
<img src="" alt="Watchlist" width="80%">
</p>

- As a user I should be able to view my profile details.
<p align="center">
<img src="" alt="profile">
</p>

- As a user I should be able to change my subscription tier.
<p align="center">
<img src="" alt="change sub" width="80%">
</p>

- As a user I should be able cancel my subscription.
<p align="center">
<img src="" alt="cancel" width="80%">
</p>

- As a user I should be able to search for videos.
<p align="center">
<img src="" alt="search" width="80%">
</p>

- As a user I should be able to filter videos by genre.
<p align="center">
<img src="" alt="Filter Genre" width="80%">
</p>

#### Strategy
I wanted to create a content streaming using `Django`, `Python`, `Javascript`. 
The website must be user friendly and easy to navigate in order for the user to find and watch the content they want.

#### Scope

#### Structure


#### Skeleton
[Landing Wireframe]()<br>
[Home Wireframe]()<br>
[Search Wireframe]()<br>
[Profile Wireframe]()<br>
[Plans Wireframe]()<br>
[Payment Wireframe]()<br>
[Video Page Wireframe]()<br>

#### Surface


## Database schema
Below you can find the schema of each table along with the datatypes for each field.


## Features


### Features left to Implement


## Technologies Used

- [Python3](https://www.python.org/)

- [Django](https://palletsprojects.com/p/flask/)

- [Javascript](https://www.javascript.com/)

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

- [Bootstrap](https://getbootstrap.com/)

- [Font Awesome](https://fontawesome.com/)

- [OMDB API](http://www.omdbapi.com/)

- [AWS](https://aws.amazon.com/)

- [Heroku](https://www.heroku.com/)


## Testing

### Manual Testing
- Navbar
    - Logged Out
        - Clicking the flix branding in the navbar refreshes the page.
        - Clicking the login page brings you the login view.
        - Clicking the register page brings you to the register view 
    - Logged In (No Sub)
        - Clicking the Flix branding on the navbar bring the user back to the plans page.
        - Click any of the genres will show results for videos but when trying the click the video the user will be redirected back to plans.
        - Clicking the search icon expands the search bar and allows the user to search.
        - Clicking the profile icon brings the user to the profile page.
        - Clicking the logout icon in the navbar logs the user out and redirects them back to the index page.
    - Logged In (Active Sub)
        - Clicking the Flix branding on the navbar brings the user to the home page.
        - Click any of the genres will show results for videos in that genre.
        - Clicking the search icon expands the search bar and allows the user to search.
        - Clicking the profile icon brings the user to the profile page.
        - Clicking the logout icon in the navbar logs the user out and redirects them back to the index page.

- Index Page
    - The index page doesnt have any fuctionality a part from the navbar.
- Login Page
    - Inputting the wrong username/password results in an error message.
    - Leaving any of the fields blank gives a HTML error message to fill in the required fields.
    - Inputting the wrong case for the username also returned an error message.
    - Clicking the "Reset Password" links brings you to the reset passwork page.
- Reset Password Page
    - Clicking the "Reset Password" button without entering an email address gives you an error message.
    - Entering an email and clicking the button redirects the page to a confirmation screen that the email has been sent.
    - Clicking the link in the email recieved brings you to a form that asks for a new password and confirmation password. 
        - If the links invalid you will be giving a message saying so with a link to restart the process.
        - Entering a common/short password returns an error message.
        - Completing the form redirects you the completed page with a link to sign-in.
- Registration Page
    - Leaving any of the fields blanks gives a HTML5 validation error.
    - Entering two different password returns "Passwords must match".
    - Completing the form logs the user in and redirects them to the plans page.
- Plans
    - The plans page is shown when the user doesnt have an active subscription. 
    If they try to access some areas of the site they will be redirected back here.
    - Clicking any of the subscribe buttons will redirect the user the payment page (with the plan the user clicked selected)
- Payment Page
    - Clicking the "Cancel" button brings the user back to the plans page.
    - Clicking pay without filling in any of the fields shows an error `Could not find payment information`.
    - Clicking the pay button with just the full name field filled returns the same error.
    - Clicking pay with the card and full name field filled returns the error "Your card's expiration year is invalid"
    - Filling in all fields with valid information but the CVV completes the payment *.
        - This is a bug I've yet to fix, not sure if stripe side or mine.
    - Filling all payment details and leaving full name empty completes the payment.
- Profile
    - Clicking the reset button brings the user to the reset page.
    - Clicking the change button brings the user to the plan pages where they can "Upgrade" or "Downgrade" their plan.
    - Clicking cancel bring up a modal confirming the cancellation of your subscription.
        - Clicking "Yes" cancels your subscription and refreshes the page with the new data.
        - Clicking "No" or the "X" icon closes the modal.
- Video Page
    - When the user clicks a video they will be redirected to the video page. This will autoplay the video and have the video
    details shown below.
    - If the video has similar tags to another video it will be shown in the "More like this" section (limited to 3).
    - If the user clicks the tags they will be redirected the search page with results of that tag.
    - If the user clicks the genre they will be redirected the search page with results for that genre.
    - The user can like/dislike and add/remove the video from the watchlist with the icons below the video.
    - If the user has watched more than 10 seconds of the video it will be added to the "watching list" and 
    will record the last known position for later viewing.
    - If the user watched the whole video or will less than 15 seconds left the video will be removed from the watching
    list and added to the watched list.
- Home
    - Clicking the watch now button in the jumbotron will bring the user to the featured videos page.
    - Scrolling down the page will stop the video playing in the jumbotron and show a play icon.
    - Clicking the play icon will play the video again.
    - If the user watched partial videos they will be shown a "Continue Watching" section where they can resume the videos.
    - If the user liked any video they will be shown a random column of suggestion/similar videos.
    - By default the page will be populated with videos from all the genres (limited to 20).
    - On this page the user can do the usual like/dislike and adding/removing videos from the watch list.
- Watch List
    - If the user has not added any videos to their watch list they will be shown the message `It's a little lonely in here, Add some videos to your list by pressing the + icon`.
    - If the user has added videos to their watch list the the video will be shown here.
        - When hovering over the videos the user will be shown three icons.
        - Clicking the "X" icon will remove the video from the watch list.
        - Clicking the like icon will darken the dislike button and add the video to the user likes (resulting in suggested videos)
        - Clicking the dislike button will darken the like button and add the video to the user dislikes
- Search page
    - There are three types of search filters. Genre, tag and search term.
        - If the user clicked one of the genres in the navabar they will be redirected here and shown videos in the given genre.
        - If the user clicks the tags under the video in the video page they will be redirected here and shown results of the given tag.
            - The search box on this page will still search by term and not by tag.
    - Searching using the icon in the navbar or the search box in this page will show video results with the searhc term used.
    - The user can do the usual things will the icons shown on the videos if there is results.

#### Known bugs
- When clicking the navigation items occasionally the background of the icon turns white.
- Sometimes `youtube-dl` has an issue retrieving the video, to counteract this I've returned `None` so that only the background image shows.
- Object-fit doesnt stretch the featured video on Edge. I've yet to find a fix for this.
- If liking/disliking/watch listing a lot of videos in a short space of time some of them dont register.
- Username is case-sensitive. This seems to be built into Django.

### Automated Testing

## Deployment

#### Heroku Dashboard

#### Locally

## Credits

### Content
- All content such as titles, descriptions were retireved from IMDB using `OMDB API`.

### Media
- The videos are all retrieved from youtube using `youtube-dl`. I don't claim to own any of these and are only being used for educational purposes.
- All promotion images for the videos were sourced from IMDB. As with the videos I dont claim to own these and are only being used for educational purposes.
- All Icons are from font awesome.
- The Landing page hero image was sourced from [here](https://ya-webdesign.com/image/responsive-web-design-png/567783.html).

### Acknowledgements
- The accounts app I used was sourced and modified from Code Institute.
- In order to register the models in the admin panel I used the example [here](https://djangobook.com/mdj2-django-admin/).
- To filter the items using the fields of the models I used this example [here](https://stackoverflow.com/questions/48665353/django-1-11-admin-list-filter-to-include-fields-in-another-model).
- In order to get a random video if a featured video wasnt supplied I used this example [here](https://stackoverflow.com/questions/22816704/django-get-a-random-object/22816927).
- When showing the home view I needed to get join several querysets from separate genres, I was able to do so using this example [here](https://stackoverflow.com/questions/38967599/joining-two-querysets-in-django).
- I was able to add tags to my models using [this](https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704) example.
- As I'm using `django-taggit` in order to add tags to videos I needed a way to retrieve the tags, using this example [here](https://stackoverflow.com/questions/11321906/in-django-taggit-how-to-get-tags-for-objects-that-are-associated-with-a-specifi) I was able to do so.
- This example [here](https://stackoverflow.com/questions/56580696/how-to-implement-add-to-wishlist-for-a-product-in-django) gave me a good idea on how to implement a watch, like and dislike list for the user.
- I used this [example](https://stackoverflow.com/questions/54945781/django-how-to-get-url-path) to get the current url when adding/removing liked/disliked videos.
- When adding a video I needed the fetured option to be unique to one video, in order to do this I used this example [here](https://stackoverflow.com/questions/1455126/unique-booleanfield-value-in-django).
- In order to dynamically add the genres to the navigation bar within the `base.html` drop down I needed to create a context processors. To achieve this I used the example [here](https://stackoverflow.com/questions/34902707/how-can-i-pass-data-to-django-layouts-like-base-html-without-having-to-provi/34903331).
- To use the `OMDB API` when adding videos I needed a way to pass my script to the admin panel. Using this [example](https://stackoverflow.com/questions/16014719/adding-a-jquery-script-to-the-django-admin-interface) I was able to do so.
- In order to store the dates returned by Stripe I needed to convert the date from Unix timestamp using this [example](https://stackoverflow.com/questions/12589764/unix-timestamp-to-datetime-in-django-with-timezone).
- To identify which button was pressed in a form I used this [example](https://stackoverflow.com/questions/8571383/how-to-identify-button-click-event-of-template-page-in-view-page-of-django).
- In order to filter videos in the django templates I needed to create custom template filters. I used these examples [here](https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/) and [here](https://stackoverflow.com/questions/47792373/invalid-filter-error-in-django-custom-template-filter).
- When creating new video entries I wanted the slug for each video to be generated using that videos title. In order to achieve this I used the [this](https://gist.github.com/ishwar6/a0beb5e7cb04b56b931877071cdc853c) example shown in this [video](https://www.youtube.com/watch?v=d5LYM3C_A98).
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
You can try the live version of the Website [Here](https://flix-streaming.herokuapp.com/)<br><br>
**Credentials:**
   ```
   Username: demo
   Password: demopassword123
   ```
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Four/raw/master/screenshots/responsive.gif" alt="Responsiveness" width="80%">
</p>

## UX

#### User Stories
- As a user I should be able to like/dislike videos.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Four/raw/master/screenshots/like-dislike.gif" alt="Like/Dislike" width="80%">
</p>

- As a user I should be able to add videos to a watch list.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Four/raw/master/screenshots/watchlist.gif" alt="Watchlist" width="80%">
</p>

- As a user I should be able to view my profile details.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Four/raw/master/screenshots/profile.jpg" alt="profile" width="80%">
</p>

- As a user I should be able to change my subscription tier.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Four/raw/master/screenshots/change-sub.jpg" alt="change sub" width="80%">
</p>

- As a user I should be able to cancel my subscription.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Four/raw/master/screenshots/cancel.jpg" alt="cancel" width="80%">
</p>

- As a user I should be able to search for videos.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Four/raw/master/screenshots/search.jpg" alt="search" width="80%">
</p>

- As a user I should be able to filter videos by genre.
<p align="center">
<img src="https://github.com/gazzamc/Milestone-Project-Four/raw/master/screenshots/genre.jpg" alt="Filter Genre" width="80%">
</p>

#### Strategy
I wanted to create a content streaming website using `Django`, `Python`, `Javascript`. 
The website must be user friendly and easy to navigate in order for the user to find and watch the content they want.

#### Scope
The main goal for this website was to make navigation as easy as possible. I think I achieve that and getting to the content you
want is painless. The overall design of the website is simple but modern looking and thats what I set out to do. The home page
can look different depending on the users likes, watchlist and the featured content.While the suggestions arent as complex as I 
wanted I still think I implement enough to allow the user to make the home page their own by liking/disliking content on the website.

#### Structure
When on the index page the navbar only has the login/register links. 
The index page consists of only a hero image. I wanted to keep this simple/clean 
as the theres already a lot going on in the home page.

When logged in and redirected to the home page (Subscriber) the homepage is where the user will be the most by design
It consists of partially watched videos (if you watched some), suggestions based on likes, most popular videos based on views
and 20 videos from each genre. The user can like/dislike or add/remove videos by hovering over video images.

The genre, search page are similar in layout and return the videos based on the criteria.
The watch list displays any videos you have added to your watch lists, if you dont have any it will display some text 
explaining how to add videos to it.

The profile page shows all the user details, allows the user to change/cancel their subscription and change their password.
The plans page shows the current plans with some details of each.
The payment page is simple and straigh to the point, it only consists of the form.

The video pages consists of the video, its landscape image behind it and below that is the video detials. The video
details consists of tags and genre, which can be clicked to search for similar videos. Under the detials are suggested
videos based on the current video you're watching.



#### Skeleton
[Landing Wireframe](https://github.com/gazzamc/Milestone-Project-Four/blob/master/wireframes/index.pdf)<br>
[Home Wireframe](https://github.com/gazzamc/Milestone-Project-Four/blob/master/wireframes/home.pdf)<br>
[Search Wireframe](https://github.com/gazzamc/Milestone-Project-Four/blob/master/wireframes/search.pdf)<br>
[Profile Wireframe](https://github.com/gazzamc/Milestone-Project-Four/blob/master/wireframes/profile.pdf)<br>
[Plans Wireframe](https://github.com/gazzamc/Milestone-Project-Four/blob/master/wireframes/plans.pdf)<br>
[Payment Wireframe](https://github.com/gazzamc/Milestone-Project-Four/blob/master/wireframes/payment.pdf)<br>
[Video Page Wireframe](https://github.com/gazzamc/Milestone-Project-Four/blob/master/wireframes/video.pdf)<br>
[Watch list Wireframe](https://github.com/gazzamc/Milestone-Project-Four/blob/master/wireframes/watch-list.pdf)<br>

#### Surface
For this project I chose to use Black and White as the color scheme. As this website is very content heavy I choose
to leave the featured video set the mood of the home page. By keeping it to black/white I my theme won't clash 
with any potential featured content. As for button colors, I choose to use the defaults in some places as it seemed
appropriate for their actions and would be instantly recognized by the user.

## Database schema
Below you can find the schema of each Model along with the datatypes for each field.

**Accounts Models**
#
|                       |  SubPlan                                              |
|:---------------------:|:-----------------------------------------------------:|
| Fields                |       Type       	                                    |
| plan_name             |  models.CharField(max_length=50) 	                    | 
| plan_price            |  models.DecimalField(max_digits=5, decimal_places=2)  |


|                       |  Subscriber                                           |
|:---------------------:|:-----------------------------------------------------:|
| Fields 	            |       Type       	                                    |
| user                  |  models.ForeignKey(User, on_delete=models.CASCADE) 	| 
| plan                  |  models.DecimalField(max_digits=5, decimal_places=2)  |
| stripe_sub_id         |  models.CharField(max_length=50) 	                    | 
| stripe_cus_id         |  models.CharField(max_length=50)                      |
| subscription_date     |  models.DateField() 	                                | 
| subscription_end_date |  models.DateField()                                   |


**Content Models**
#

|                 |                         Genre                          |
|:---------------:|:------------------------------------------------------:|
| Fields          |       Type       	                                   |
| name            |  models.CharField(max_length=50) 	                   | 


|                 |                         Video                          |
|:---------------:|:------------------------------------------------------:|
| Fields 	      |       Type       	                                   |
| title           |  models.CharField(max_length=50) 	                   | 
| slug            |  models.SlugField(max_length=50, null=True, blank=True)|
| description     |  models.TextField(max_length=300)	                   | 
| youtube_link    |  models.CharField(max_length=100)                      |
| genre           |  models.ForeignKey(Genre, on_delete=models.CASCADE)    | 
| imdb_link       |  models.CharField(max_length=100)                      |
| tags            |  TaggableManager() 	                                   | 
| image_cover     |  models.ImageField(upload_to='img')                    |
| image_landscape |  models.ImageField(upload_to='img')	                   | 
| views           |  models.IntegerField(default=0)                        |
| featured        |  models.BooleanField()                                 |

|                 |                         Watchlist                      |
|:---------------:|:------------------------------------------------------:|
| Fields 	      |       Type       	                                   |
| user            |  models.ForeignKey(User, on_delete=models.CASCADE) 	   | 
| item            |  models.ForeignKey(Video, on_delete=models.CASCADE)    |
| slug            |  models.CharField(max_length=50, null=True, blank=True)| 
| added_date      |  models.DateTimeField(auto_now_add=True)               |


|                 |                         Likelist                       |
|:---------------:|:------------------------------------------------------:|
| Fields 	      |       Type       	                                   |
| user            |  models.ForeignKey(User, on_delete=models.CASCADE) 	   | 
| item            |  models.ForeignKey(Video, on_delete=models.CASCADE)    |
| slug            |  models.CharField(max_length=50, null=True, blank=True)| 


|                 |                         Dislikelist                    |
|:---------------:|:------------------------------------------------------:|
| Fields 	      |       Type       	                                   |
| user            |  models.ForeignKey(User, on_delete=models.CASCADE) 	   | 
| item            |  models.ForeignKey(Video, on_delete=models.CASCADE)    |
| slug            |  models.CharField(max_length=50, null=True, blank=True)| 


|                 |                         Watching                       |
|:---------------:|:------------------------------------------------------:|
| Fields 	      |       Type       	                                   |
| user            |  models.ForeignKey(User, on_delete=models.CASCADE) 	   | 
| item            |  models.ForeignKey(Video, on_delete=models.CASCADE)    |
| slug            |  models.CharField(max_length=50, null=True, blank=True)| 


|                 |                         Watched                        |
|:---------------:|:------------------------------------------------------:|
| Fields 	      |       Type       	                                   |
| user            |  models.ForeignKey(User, on_delete=models.CASCADE) 	   | 
| item            |  models.ForeignKey(Video, on_delete=models.CASCADE)    |
| slug            |  models.CharField(max_length=50, null=True, blank=True)| 


## Features
- Users can like/dislike videos
- Users can add/remove videos from their watch list.
- Two tier subscription model using stripe.
- Users can upgrade/downgrade seamlessly.
- Users can cancel their subscription.
- Users can search videos by term, genre or tag.
- If users partially watch videos, the video is added to a watch list, which allows the user to 
    continue where they left when revisiting that video.
- Suggested video based on user likes on home page.
- Suggested videos on the video page based on the the current video being watched.
- Most popular videos based on views.
- Featured video on home page can be set or randomly selected on each visit.
- When adding videos (Admin) video details are grabbed based on the imdb link.
- Users can reset password.
- The navigation bar appears and disappears as the user scrolls

### Features left to Implement
- Displaying IMDB rating on each video (either on hover of image or on video page).
- Custom video player.
- A more complex algorithm for video suggestions (that takes dislikes into account).
- Option for users to delete account.
- Logging in with email.
- Video stream resolution based on subscription tier (custom video player needed).
- Grabbing images when adding new videos (Admin)
- A more refined search app.
- Dynamic loading of results as the user scrolls (to prevent loading all videos at once)

## Technologies Used

- [Python3](https://www.python.org/)
    - Used for most of the backgroud functionality of the website.

- [Django](https://palletsprojects.com/p/flask/)
    - Handles all the views, database queries.

- [Javascript/ jQuery](https://www.javascript.com/)
    - Used for manipulating the DOM and stripe api.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - Custom **CSS3** for styling the website.

- [Bootstrap](https://getbootstrap.com/)
    - All the websites structure is built using **Bootstrap**

- [Font Awesome](https://fontawesome.com/)
    - All the icons used in this project are from **Font Awesome**

- [OMDB API](http://www.omdbapi.com/)
    - Used in the admin panel to fetch data when adding new videos.

- [AWS](https://aws.amazon.com/)
    - USed for serving images and static files to the user.

- [Heroku](https://www.heroku.com/)
    - Used to host the website and database.

- [Heroku Postgres](https://www.heroku.com/postgres/)
    - Used to store all the data on the website.
    

## Testing
The website was tested using Edge, Firefox and Chrome. As I was developing the website I tested it using chrome dev tools. 
Once I had a section the way I wanted it I would then test it using the other browsers and the device emulation. I used media queries to
make the website responsive across multiple devices (using chrome dev tools). I mainly stuck with bootstrap breakpoints when tweaking
the website.

As for testing the code, I use `console.log()` when testing javascript/jQuery and `print()` when testing python.

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

After moving the static and media files over to AWS I had an issue retrieving the global variable `MEDIA_URL` from the settings.py file in my main app.
To overcome this issue and get the images loading from the AWS bucket I had to import the variable from the settings.py file into my custom context processor.
I'm not sure if I did something wrong in the beginning of the project to prevent this variable from being reachable in my templates but this has seemed to work and the
images are displaying.

I had issues getting the video to stretch the full width and height of the jumbotron on the home page. I was able to solve this with `object-fit: cover;`. 
Unfortunately, I discovered this didnt have the same effect in Edge. I've yet to find the solution to this but it covers the whole jumbtron on Chrome and Firefox.

In order to make the columns scrollable in the home page I needed to make the the overflow scroll and make the overflow-y hidden. This worrked perfectly in chrome but
when I tested this in the other two browsers I could still see the grey scroll bar. Edge was an easy enough fix I had to set `-ms-overflow-style` to none and in 
Firefox I had to set the scrollbar color to transparent (`scrollbar-color: transparent transparent;`).

When creating the custom context processor I never added a check to see if the user was authenticated. This throw an `dictionary update sequence error` when it 
tried to retrieve lists created by the user. Thankfully it was an easy fix once i figured it out but it took a bit of debugging to ge there.

### Automated Testing
When trying to write some automated testing I was getting a database permission error for my testing database. 
As I wasn't too sure on how to fix this issue I omited automated testing for this project.

If i was to do it I would have checked that each view rendered correctly using the response code. I would try
add/remove videos from various lists that the user has control over to see if they functioned correctly.
    

## Deployment

#### Heroku Dashboard

1. In the dropdown on the right, click **Create New App**.
2. On the next screen, enter app name and select server, then click **Create App**.
3. In the **Overview** page go to the **Deploy** tab.
4. Scroll down to **Deployment method** and choose **Heroku** (You can also deploy via **Github** here).
5. Using the git commands below, commit your code/project to **Heroku**:
```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
6. To keep the Heroku branch up to date connect your **Github** repo for auto-deployment.
7. You can do this by clicking the Github icon and searching for the repo.
8. Once the repo is connected you should have an option below it called **Automatic deploys**.
9. To enable this click **Enable Automatic Deploys**.

Once the project is deployed you need to set the **config variables**, 
you can do this by following the instructions below:

1. In the **Heroku Dashboard** go to **Settings**.
2. Click **Reveal Config Vars**.
3. Enter in the variable names and their values
```
    SECRET_KEY
    EMAIL_ADDRESS
    EMAIL_PASSWORD
    STRIPE_PUBLISHABLE
    STRIPE_SECRET
    * AWS_ACCESS_KEY_ID
    * AWS_SECRET_ACCESS_KEY
    DATABASE_URL
```

 &ast; If you're going to use AWS to host your static/media files you will need to create a bucket and modify
 the variables within `settings.py`.

#### Locally
To run the website from your local machine you can clone the project using the below command. 
You will need to install python3 and all its dependencies found in the requirements.txt file. 

1. Clone the git repository.
```
    git clone https://github.com/gazzamc/Milestone-Project-Four.git
```
2. Run the following commands to create the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
4. Create env.py file in the project directory and enter in the values for the following variables:
```
os.environ.setdefault("SECRET_KEY", "your-secret-key")
os.environ.setdefault("EMAIL_ADDRESS", "your-email")
os.environ.setdefault("EMAIL_PASSWORD", "your-email-password")
os.environ.setdefault("STRIPE_PUBLISHABLE", "your-stripe-test-key")
os.environ.setdefault("STRIPE_SECRET", "your-stripe-secret-key")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "your-aws-key")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "your-secret-key")
# If you dont supply the db below django will create a local sqlite db
os.environ.setdefault("DATABASE_URL", "optional-remote-database")
```

4. Add localhost to settings.py:

5. Navigate to the cloned folder via the terminal and enter:
```
python3 manage.py runserver $IP:$PORT
```

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

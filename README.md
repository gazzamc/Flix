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


#### Bugs
- When clicking the navigation items occasionally the background of the icon turns white.
- Sometimes `youtube-dl` has an issue retrieving the video, to counteract this I've returned `None` so that only the background image shows.

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
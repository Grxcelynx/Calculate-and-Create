# <img src="/static/img/Calculate&Create.jpeg" alt="Calculate & Create">

Calclate & Create came from my own personal expirience as an artist. As a painter who uses all different kinds of paint mediums, It was always a challenge to organize my timeline for my next piece or have messed up a painting by touching it before it was dry. Especially considering many artists have multiple jobs and can feel as though their creation time is cut short due to life and work. Calculate & Create allows users to configure their estimated dry time for their artwork. While an artist's mind is always turning, a user can now focus more on their creation and process rather than worry about time constaints. 


## About the developer

Before Hackbright Academy, Grace was a Professional makeup artist who worked within the beauty industry doing photoshoots, short films, retail sales, and even making lipstick by hand. After almost 4 full years of makeup artistry, her artistic passion moved onto the more technical side. After attending a bootcamp prep at App Academy, she found a new joy in the puzzles of code. She set a new course in the software engineering world and landed at Hackbright.

## Deployment 

http://localhost:5005/

## Contents 
* [Tech Stack](#teach-stack)
* [Features](#features)
* [Future Features](#future)
* [Installation](installation)

## <a name="tech-stack"></a> Technologies 
* Python
* Flask
* Jinja2
* PostgresQL
* SQLAlchemy 
* JavaScript
* HTML
* CSS
* Bootstrap
* Twilio
* React

## <a name="features"></a>Features

#### Landing Page 
Users click on Calculate & Create to create!

#### Home Page 
Users can view all optins provided for the website. They can choose to create a calculation, view pre calaculated dry times, and information about the types of paints and their drying formula.

#### Create
User gets to name their creation, select their choice of paint, size of canvas, and what their current weather condition is. All hree values are calculated using jinja to return the users output of their final dry time in minutes and hours. If a user wants to save their creation, they can simply send themsleves their calculation info in a snap. By using the Twilio SMS API any user that inputs their name and phone number will recive their own calaculation with their creation name and dry time in minutes and hours. 

#### Paint Info
To help users understand their results of their calculation as well as to inform any new artists, users can learn more about each paint type and paint thinner. 

#### Examples
While many people can be in a rush, this currated page of set calculations is for any users that don't have time or want to go through the calculation process. 

## <a name="future"></a> Calculate & Keep Creating 
There are new features planned for addiontal sprints:
* Allowing users to post their finished creations 
* Implementing Michael's, Blick, and other art stores API to gather more accurate dry times and exact options for users calculations
* Having options for users to calculate more mediums such as nail polish, house paint, possibly even some makeup products 
* calculating multiple mediums at once 

## <a name="installation"></a>Installation

To run Calculate & Create:

Clone this repo:
```
https://github.com/Grxcelynx/Calculate-and-Create-HBProject2021
```

Create and activate a virtual enviornment inside you Calculate 7 Create directory:

```
virtual env
source env/bin/activate
```


Install the dependencies:
```
pip install -r requirements.txt
```

Sign up to use the [Twilio API](https://www.twilio.com/try-twilio/)



You will need to register for an API key. For the Python back-end, the key will need to be saved as below:


Save your API key in a file called <kbd>secrets.sh</kbd> using this format:

```
export TWILIO_API_KEY="YOUR_KEY_HERE"
export TWILIO_AUTH_TOKEN="YOUR_TOKEN_HERE"
export TWILIO_PHONE="YOUR_TWILIO_PHONE_NUMBER"
export GOOGLE_API_KEY="YOUR_KEY_HERE"
export GOOGLE_CLIENT_ID="YOUR_ID_HERE"
```

Source your key from your secrets.sh file into your virtual environment:

```
source secrets.sh
```

Set up the database:

```
createdb calculate_n_create
python3.6 model.py
```

Run the app:

```
python3.6 server.py
```

You can now navigate to 'localhost:5005/' to access Calculate & Create.


# SITE NOT LIVE ANYMORE
# <img src="https://github.com/Grxcelynx/Calculate-and-Create-HBProject2021/blob/main/Calculate%26Create.png" alt="Calculate & Create">

Calclate & Create came from my own personal expirience as an artist. As a painter who uses all different kinds of paint mediums, It was always a challenge to organize my timeline for my next piece or have messed up a painting by touching it before it was dry. Especially considering many artists have multiple jobs and can feel as though their creation time is cut short due to life and work. Calculate & Create allows users to configure their estimated dry time for their artwork. While an artist's mind is always turning, a user can now focus more on their creation and process rather than worry about time constaints. 


## About the developer

Grace got her start in the Cosmetic Beauty industry, working alongside corporate companies with largely client based roles, while freelancing as a lead Makeup Artist for multiple media platforms. After 4 years, she decided to shift her artistic eye to the art of programming. With Makeup Artistry being an interactive, visual, and hands on job, she found the problem solving of code and collaboration of paired programming to be a new form of creativity. She then began taking multiple prep courses and utilizing her creative side. By implementing new frameworks, learning new languages, and databases she is excited to further her career as a Software Engineer.
## View Demo Video 
https://www.youtube.com/embed/kAA_E5DfwLo

## Visit live site
https://www.calculateandcreate.art/
## Deployment 

http://localhost:5005/

## Contents 
* [Tech Stack](#teach-stack)
* [Features](#features)
* [Future Features](#future)
* [Installation](#installation)

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

# <img src= "https://github.com/Grxcelynx/Calculate-and-Create-HBProject2021/blob/main/1_0_GIF_2.GIF" alt= "landing-gif">

#### Home Page 
Users can view all optins provided for the website. They can choose to create a calculation, view pre calaculated dry times, and information about the types of paints and their drying formula.

#### Create
User gets to name their creation, select their choice of paint, size of canvas, and what their current weather condition is. All hree values are calculated using jinja to return the users output of their final dry time in minutes and hours. If a user wants to save their creation, they can simply send themsleves their calculation info in a snap. By using the Twilio SMS API any user that inputs their name and phone number will recive their own calaculation with their creation name and dry time in minutes and hours. 
# <img src="https://github.com/Grxcelynx/Calculate-and-Create-HBProject2021/blob/main/calculation.GIF" alt="calc">
# <img src="https://github.com/Grxcelynx/Calculate-and-Create-HBProject2021/blob/main/IMG_5646.jpg" alr="confirm">
#### Paint Info
To help users understand their results of their calculation as well as to inform any new artists, users can learn more about each paint type and paint thinner. 
# <img src="https://github.com/Grxcelynx/Calculate-and-Create-HBProject2021/blob/main/1_0_GIF_2%202.GIF" alt="paint=info">
#### Examples
While many people can be in a rush, this currated page of set calculations is for any users that don't have time or want to go through the calculation process. 
# <img src="https://github.com/Grxcelynx/Calculate-and-Create-HBProject2021/blob/main/1_0_GIF_2%203.GIF" alt ="examples">
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

Create and activate a virtual enviornment inside your Calculate & Create directory:

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


# auto-scrap-images
Small python script that automatically download images from urls

## So, I had a problem.
### I needed all Fortnite maps for a project, but it would've take too much time to download them manually.

Here is how I solved my problem without actually downloading them manually.

To make this project work, you'll need to download "Google Chrome for Testing" (I used Python 3.13, and downloaded the 136.0.7103.94 version Google Testing app through this [list](https://googlechromelabs.github.io/chrome-for-testing/) \
Then install requirements (you need pip installed, use this command : pip install -r requirements.txt)

## What is this script actually doing ?

At first, you can see we define the path to find Chrome Testing, then we define our Downloads directory. \
Then, we define all options to make Google Testing app work with ChromeDriver. \
For this specific use, I had to simply loop into different versions of maps. We have an array (a list) of versions we want to retrieve.

We have a function, that takes as argument 'startNumber'. We could change this to 'myUrl', and use a list of url we want to loop in. \
This function opens a new tab in a new google testing browser, we then check if we already saved the file (by checking the file names). \
I made an other 'if statement' that is also specific to my case, that looks if the html "title" tag is equal to a 404 (not found) or a specific string (here : Page Not Found - Fortnite.GG). \
If these two statements did not intervene, this means we can begin the actual work : we accessed the image url, we then use "PyAutoGui" to press commands & keys (here, "command + s" (for mac) to open the saving pop-up, then "enter" to click the "Save" button (Blue button (on mac) you can see when you try saving an image).

I may have more ideas to make this helpful and globally interesting, this is too niche for the moment. If you have an idea, a request or a question, don't mind asking me : \
My discord : yael#2898 (yaelou)


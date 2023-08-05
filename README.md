# ChatGPT-Clone
ChatGPT clone using Flask, Tailwind CSS and OpenAI API

Project Overview: It is a ChatGPT clone made using Flask and Tailwind CSS. Unlike many such 'clone' projects, this actually has a 'working' backend developed using OpenAI API. We can enter any search term in the box, which will be searched on the OpenAI's ChatGPT database using OpenAI API, and the results will be displayed.

Tech Stack: Python, Flask, Jinja2, MongoDB, HTML5, Tailwind CSS, JavaScript

Key Features:
◾ Made using Flask
◾ Uses static CSS classes by Tailwind CSS
◾ Backend developed by integrating OpenAI's GPT 3.5 Turbo API
◾ Uses Jinja2 classes
◾ Uses MongoDB
◾ Fetched results from OpenAI are stored on local mongo database for optimization

Challenges & Solutions: Had a hard time designing the backend processes, especially how the data is fetched from OpenAI's data servers and cached on MongoDB cloud(MongoDB Atlas). Also cloning how the site looks and works exactly the same needed enough experimentation with Tailwind's CSS classes.

I'm eager to hear your thoughts and feedback on this project. Feel free to try it out and share your impressions below! Let's connect if you'd like to collaborate or discuss Python and Web Develpoment projects further.

NOTE: Tailwind requires npm to run on localhost. So install npm, then on terminal 1 type 'npm run tailwind', and then on terminal 2 type 'python main.py'. Click on the link to open the website on your browser. Also, it fetches data from my local database hosted on cloud, so while trying you need to change the MongoDB links to display your own data and provide your own OpenAI secret key.

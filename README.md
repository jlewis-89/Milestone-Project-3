# MSP-3 Registered Interest

## Code Institute Milestone 3 Backend Development Project

Live Site []

Repository []

## Table of Content

## Purpose
### The purpose of the project is to develop a backend data based application using the Flask framework and MongoDB
### The project - Registered Interest
The purpose of this website is to enable users to litmus test their business ideas via a community feedback process.
Users will be able to: 
- Register a profile
- Post their Business Ideas
- Comment on other users ideas via the Q&A section
- Upvote and Downvote ideas
- Save ideas they are interested in
- Edit and update their ideas but not other peoples
- Choose whther they feel others ideas are investable or not

The platform will act like a online community of "Dragons Den" helping users to recieve feedback and promote thought and development of ideas for free from the community.

## Project Goals

## Developer Goals

## Tools & Technologies Used
### Software
Figma
DALL.E 3
VS-Code
### Frameworks
Materialize Framework
Flask Framework
###Languages
HTML / CSS / JS / Python

## Design

### UI
#### Wireframes
#### Navigation
- Navbar takedn from the Materialize CSS framework
#### Imagery
- Logo imagery created by DALL.E 3 and the edited with MS Photo Editor
#### Typography
- Montserrat is a versatile and modern font with good readibility
- Roboto is a clean and widely used font that complements Montserrat well
#### Colour scheme - WebAIM Accessibility
- Navy Blue #001F3F - This colour represents trust and professionalism
- Teal #39CCCC - Adds a fresh and approachable tone 

### UX
As a user I want to be able to view all the ideas on the website
As a user I want to be able to create my own ideas and post them to the website
As a user I want to be able to edit and delete my ideas on the website
As a user I would like to be able to edit and delete my user account
As a user I would like to be able to change the email registered to my account
As a user I would like to be the only onje who can edit or delte my ideas
As a user I would like to be the only oner who can edit or delete my account

### Data Schema
* Users Collection:
* Attributes:
- username: A unique identifier for each user.
- password: The user’s password (hashed and salted for security).
* Ideas Collection:
* Attributes:
- description: A detailed description of the idea
- title: A concise title for the idea
- valuation: The estimated value or potential impact of the idea
- created by: The user who originated the idea
- invest: Would you invest in the idea Yes or No

#### JSON

{
  "users": [
    {
      "username": "string",
      "password": "string"
    }
  ],
  "ideas": [
    {
      "description": "string",
      "title": "string",
      "valuation": "number",
      "created_by": "reference to user",
      "invest": "Yes or No"
    }
  ]
}

## Features
The website features include:
- Usere profiles to register and loginm
- Ideas to view the community of ideas
- Profile to change any profile specific details
- Create edit and delete users own ideas


## Testing
### Alpha Testing
### Validators HTML/CSS/JS

-Python code has been checked for PEP8 compliance and formatted appropriately

### Bugs & Fixes

## API's

## Deployment
### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
   - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

    By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original     repository by using the following steps...

    1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
    2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
    3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### Hosting via Heroku
Log in to Heroku

## Credit
Logo generated via DALL.E 3 AI
### Acknowledgement
### Resources
### Assets
### Code Re-use
### Licensing

## Status
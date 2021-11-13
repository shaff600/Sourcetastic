
  Python Flask Video Uploading Web Application
# Purpose 
This application was developed to aid small tech teams to collaborate and share YouTube learning resources in one centralized system. I have found myself within several online tech communities where members where posting links for learning resources but they used to get lost with an array of different messages. This application was developed to solve that issue.
# User Experience (UX)
## Stratergy: 
This application will allow a member to create an account and add learning resources to share with other users. A user can only edit or delete there OWN resource and do not have access to alter other team members content. There is also an Admin account where they have the additional functionality of adding a category. This user will tend to be a moderator or an the lead of the community.

The objective is to create a platform where members of a community can share learning resources for a range of different tech categories. Although the application is appropriate for people of all ages, the interface must be visually pleasing to boost user engagement and acceptability across different age groups

-	### User stories
	-	As a user, I would like to view all learning resources 
	-	As a user, I would like to be instructions on how to add a new resource
	-	As a user, I would like to edit and delete a post 
	-	As a user, I would like to know who has created a post
	-	As a user, I would like informed responses on system actions 
	-	As a user, I would like to view the application on various devices 

## Scope:
The application has a set of categories that are restricted by the admin user. This is to ensure that the categories are aligned to what the tech community are intrested in and prevent users from adding content that aren't relevant. There are no limitations to how many resources a user can add within the application.

## Structure:
To enable consistancy throughout the applicatuon, the Python template engine of "Jinja" was used to help structure the HMTL pages. Jinja is a modern day templating language for Python developers. Jinija templates include inheritance which  is used to prevent repeated code. This saves a lot of time and reduces work. A base template contains the basic layout which is common to all the other templates. This is beneficial as it provides a level of consistency throughout the application structure. 

## Skeleton:
Prior to the development of the project, I sketched out my initial idea in Balsamiq Wireframes to provide a visual representation of how the application will look like. This has helped when creating the application as it allowed for guide to follow during development. I have kept the layout pretty straightforward as this is a CRUD application. In order allow these database interactions, I have used forms to create resources and update resources. The application will be reading resources and displaying them on individual cards. 

My initial design did not include a landing page, instead the user was navigated to the resource page on their first visit. This was a bad idea as the user would not have any context of the application purpose and the user isn't provided with instructions on how to use the application either. 

## Surface:

### Front-end Framework -  [Materialize](https://materializecss.com/)
-	The front-end framework of Materialize was used to build the styling components of the application. Materialize does alot of the heavy lifting for you and provides  default stylings that speed up the development process.

### Live background -  [Loading.io](https://loading.io/background/m-interstellar/)
-   The live background was implemented into the site by using an SVG file. I have chosen the "ripple" effect to keep it minimalistic to not distract the user whilst using the application. 

### Custom Font -  [Google Fonts](https://fonts.google.com/specimen/Permanent+Marker)
-   To make the headings stand out on the web pages i have selected the "Permanant Marker" font to catch the user's attention. For text I have used "Outfit".

### Glass Cards-  [Glassmorphism](https://hype4.academy/tools/glassmorphism-generator)
-   This generator was used to create the background styling for the card components on the application. It was simple to use and provided CSS that's required for the desired effect.

## Features
-	Connectivity to mongoDB database. 
-	User can Create, Read, Update and Delete items from database.
-	Responsive on all device sizes

## Technologies Used

### Languages Used
 1. HTML <img align="left" alt="HTML5" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png" />
 2. CSS/Materialize <img align="left" alt="CSS3" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png" />

 3. <img align="left" alt="JavaScript" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png" /> JavaScipt
 4.   <img align="left" alt="MongoDV" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/mongodb/mongodb.png" /> MongoDB
 5.   <img align="left" alt="MongoDV" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" /> Python
 

### Frameworks, Libraries & Programs Used
1.  [Flask:](https://flask.palletsprojects.com/en/2.0.x/)
-   Flask provided tools, libraries and technologies that helped build the application. One of the tools used was the Jinja templates.

2.  [Google Fonts:](https://fonts.google.com/)

-   Google fonts were used to import the 'Ubuntu Condensed' font into the style.css file which is used on all pages throughout the project.

3.  [Font Awesome:](https://fontawesome.com/)

-   Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

4.  [jQuery:](https://jquery.com/)

-   jQuery came with Materialize to aid the frameworks interactive features.

5.  [Git](https://git-scm.com/)

-   Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

6.  [GitHub:](https://github.com/)

-   GitHub is used to store the project's code after being pushed from Git.

7.  [Balsamiq:](https://balsamiq.com/)

-   Balsamiq was used to create the  [wireframes](https://github.com/)  during the design process.


# Testing

Please find the results of my tetsting [here](Testing.md)
	

## Testing User Stories from User Experience (UX) Section


  ## Manual Testing 


### Known Bugs


### Issues Faced



### Future Development 

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/shaff600)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://shaff600.github.io) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/shaff600/TriviaGameNight
```

7. Press Enter. Your local clone will be created.

```
$ git clone ****
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done .
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Sources 

### Acknowledgements

# Digital Board

We are here to make your digital classroom experience as seamless as possible. Our tools make it simple to manage and submit your assignments, view and share study material and resources, keep a track of your pending tasks and help you make most of your remote learning experience.

Here is the link to the website: [Digital Board](https://digitalboard.herokuapp.com/)

## Contents ##

- [Features](#features)
- [Key Points](#key-points)
- [Walkthrough](#walkthrough)
  - [Student](#student)
  - [Teacher](#teacher) 
- [Getting Started](#getting-started)
- [Bug Reporting](#bug)
- [Feature Request](#feature-request)


<a id="features"></a>

## 🚀 Features

- Teachers can easily upload assignments, set deadlines, share study materials and assign them to students. The students can view & submit these assignments and add comments, if necessary. 
- Teachers can pin important resources at the very start, so that the students don't find it difficult to navigate to them at the time of need.
- Digital Board offers students a to-do list so that they can easily keep a track of what all tasks have been assigned.
- Teachers can view the submissions made by each student for a particular assignment
- By providing easy login and logout capability via Social Accounts, we have removed the hassle of remembering another set of login credentials.
- Although developed as a desktop-first application, Digital Board is fully responsive and will work on screens of all sizes.

<a id="key-points"></a>

## ⭐ Key Points
- ### Loggin In 🚪
  - All users, be it teachers or students(in real life) are granted student access only. This makes them unable to create classes and subsequently assignments. This has been implemented as a security feature to prevent anyone from having teaching access.
- ### Teaching Access 👩‍🏫
  - To get teaching access, click on the Request Teacher Access button. An email will be sent to admin as well as to you, indicating that you have requested for teaching access. If everything checks out well and you indeed are a teacher, the admin will grant you teaching access within 24 hours. You need to log out and log in, for the changes to be visible.
- ### Join a Class 🏛
  - In order to join classes and submit assignments, you need to have class codes. Ask your teacher to share it with you. In the meantime you can join these classes, Class Code: b626R4 (Python), Class Code: 9Mxc1T (C++). Class codes are 6 digit alphanumeric unique strings.
- ### Assignments & Study Material 📚
  - The teacher can upload both assignments as well as study materials. Assignments need to be submitted before the deadline. For resources, there are no submissions required. The deadline associated with resources means that teacher expects you to complete them before that date.



<a id="walkthrough"></a>

## 🚶‍♀️ Walkthrough 


<a id="getting-started"></a>

## 📦 Getting Started

- Fork this repository and clone it in your local environment.
- Create a virtual environment and install relevant packages.
  ### Anaconda ###
  Go to the desired directory and run the following command in Anaconda Prompt:

  ```bash
  conda create -n myenv --file requirements_conda.txt
  conda activate myenv
  ```
  Here myenv is the name of the virtual environment (can be set according to ones liking) amd requirement_conda.txt is the requirements file that has been provided alongside the  project. The second line of code activates the newly created virtual environment.

  ### PIP ###
  Go to the desired directory and run the following command in Commmand Prompt:

  ```bash
  pip install virtualenv
  virtualenv myproject source myproject/venv/bin/activate
  cd myproject
  pip -r requirements_pip.txt
  ```

  Here myproject is a folder that gets created. For ease, run git clone inside the myproject directory. requirements_pip.txt is the file which contains all the packages that need to be installed.
  
  
- Go to web/settings.py and make the following changes in these lines of code.

  ```python
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
  }
  ```

  - In NAME field specify the name of the database (create one, if not already present).
  - In user specify which user of MySQL you want to connet with and specify the password for that user.

- Now after having the virtual environment activated, run the command:
  ```python
   python manage.py runserver
  ```

<a id="bug"></a>

## 🐛 Bug Reporting

Feel free to [open an issue](https://github.com/saksham117/Samarthya_Grievance_Redressal_System/issues) on GitHub if you find any bug.

<a id="feature-request"></a>

## ⭐ Feature Request

- Feel free to [Open an issue](https://github.com/saksham117/Samarthya_Grievance_Redressal_System/issues) on GitHub to request any additional features you might need for your use case.
- Connect with me on [LinkedIn](https://www.linkedin.com/in/saksham-basandrai117/). I'd love ❤️️ to hear from you.
  
 

  


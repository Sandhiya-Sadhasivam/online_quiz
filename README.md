# online_quiz
### [onlinee-quiz.herokuapp.com](https://onlinee-quiz.herokuapp.com/)
This is an online quiz organizing website project, developed using Python's web framework Django.<br>
For front-end designing I have used Twitter's front-end library Bootstrap4.



[![Website](https://img.shields.io/website?url=https%3A%2F%2Fonlinee-quiz.herokuapp.com%2F)](https://onlinee-quiz.herokuapp.com/)
[![GitHub license](https://img.shields.io/github/license/Sandhiya-Sadhasivam/online_quiz)](https://github.com/Sandhiya-Sadhasivam/online_quiz/blob/main/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
![Django Version](https://img.shields.io/badge/Django-V3-brightgreen)
![Python Version](https://img.shields.io/pypi/pyversions/Django)
## Current Features

### Site access features:
* User must be logged in to access the Quiz.
* For signup user is required to give *username*, *first name*, *last name*, *e-mail address*, *College name*, *Phone no* and *password*.
* For login the user will be required to enter *username* and *password* only.

### Features of the quiz:
* The logged in user either can take an existing quiz.
* All questions are multiple choice question.
* Each question is displayed only once per user.
* Questions are displayed randomly for every user.

### Leaderboard features:

* Leaderboard is a shorted list according to the score obtained by the users.
* If two users are having same score, the user who has signed up earlier will have good ranking than the one who joined late.
* Leaderboard is open to all. No login required.

### Administrative features:

* Only admin can add questions.
* Admin can add questions and modify them until they are not marked as *Has been published?*
* Once a question has been published, it can neither be modified nor can be accessed. Admin can only see a list of questions.
* Admin can search questions by question text or choice text.
* Admin can filter questions based on whether the questions have been published or not.



## Technologies and Tools

1. **Language** - Python 3.6 or later
2. **Backend Framework** - Django 3.2
3. **Database** -SQLite but POSTGRESQL is recommended
4. **DBMS** - Pgadmin 
5. **Version-control** - Git and GitHub
6. **Style Libraries** - Bootstrap

## Instructions to run locally
### 1. Clone this repository
```bash
git clone https://github.com/Sandhiya-Sadhasivam/online_quiz.git
cd online_quiz
```
### 2. Install the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
Follow [instructions on official documentation page](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

### 3. Create the virtualenv
```bash
## run following command from `online_quiz` directory
virtualenv env
```

### 4. Activating virtualenv
```bash
## Activate the virtualenv which you created on the last step
.\venv\Scripts\activate
```

### 5. Install python packages
```bash
pip install -r requirements.txt
```

###6. Migrations
To run migrations.
```bash
python manage.py makemigrations
python manage.py migrate
```
### 7. Create superuser
To create superuser run. 
```bash
python manage.py createsuperuser
```
After running this command it will ask for username, password. You can access admin panel from
```bash
localhost:8000/admin/
```

### 8. Run development server
```bash
python manage.py runserver
```

## Contributors

* [Rajeshwaran](https://github.com/Rajeshwaran2001)
* [Sandhiya](https://github.com/Sandhiya-Sadhasivam)

## Scope

This Project can be utilized in a wide range of Educational Institutes like Colleges, Schools, Coaching Institutes etc. It is still under development and we plan to keep working on it till it is ready to be used commercially.Hopefully if it turns out to be good enough we will be able to support all the online quizzes held in our college at the local level.

The room for development is enourmous. We can first start by adding a code editor and an online judge. We can use webscraping to scrape the best quizzes from the net. ML can be implemented to predict quiz chices for students who are here to practice. Quiz-groups features can be added and some imitation of hackerearth's code arena can also be added. 

The main reason behind choosing this project was that we can keep on working on it and improving it.

##**Upcomeing Features of online_quiz:**

* Timer for each quiz and the user is required to finish the quiz in given time.
* When the timer stops, the corresponding record (i.e. number of correct answers) will be saved automatically.

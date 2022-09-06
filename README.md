# Project: 	Task Distribution Service

## Description:
Api service for distributing tasks between employees. Analogue to Jira, Asana, Redmine.The service should allow registering, authorization, creating commands, creating tasks, linking tasks to a specific user and commands.

### To test project:

Install all requirements:

`pip install -r requirements.txt`

Then in Unix-systems type next commands to upload fixtures and runserver:

`make migrate`

`make run`

In case of Windows:

`python manage.py migrate`

`python manage.py loaddata fixtures.json`

`python manage.py runserver`


### Features

API / Authorization / Swagger;

User roles: 
- Worker (he sees only his team’s tasks)
- Manager (sees the tasks of all his teams)
- Admin (doesnt have any restrictions)
 
 
Worker and Manager can have statuses:
 - in_team - sees team/teams tasks
 - bench - does not see tasks but sees list of teams
 - fired - does not see anything, cannot log in
 
Teams:
 - one worker can have only one team
 - team has an unlimited number of employees
 - team has an unlimited number managers
 - one manager has an unlimited number of teams
 - team members only see the tasks of the teams with which they have a connection.
 - manager can add and delete worker to the team
 - only the Admin can delete a team
 - Workers in the team have the status of “in_team”
 - Workers and Managers without a team have “bench” status
 
Tasks:
 - connection with other tasks (for example, a task on the backend that is connected to a task on the frontend)
 - employee that the task is assigned to
 - has a status (Backlog, Ready to Dev, In progress, Ready to QA, Production)
 - task is tied to a command
 - task without a command cannot exist
 - only the Manager/Admin can create tasks
 - can exist without a deadline and employee
 - has history of changes to the task, who changed the task when and how (in admin panel)
 - can be sorted by team, status, employee
 - employees can comment tasks
 
Permissions:

 - Anyone with access can get a list of tasks.
 - Any person with access can view a specific task.
 - Anyone with access can edit a task
 - Anyone with access can change the status of a task.
 - Anyone with access can delete a task
 

### This project was creating as a pet-project in team:
 Dmitriy Chadaev: https://github.com/ELesten
 
 Taras Chebukov: https://github.com/CheTars
 
 Evgeny Bobarnev: https://github.com/InhumanMagpie

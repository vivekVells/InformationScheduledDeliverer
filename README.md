# InformationScheduledDeliverer
Information Deliverer is an app to schedule the desired content information to be delivered by delivery medium like Email, Text, Fax, etc.

### Note
- This project is one among the specials to me as I solely completed this project solving a real time issue by utilizing best SDLC practices starting from understanding customer needs, design, build, test, deploy and maintain.

## Objective
- To schedule mail automatically and deliver the contents via email or test or any such medium

## Reason for this project creation
- When I was working at [Digital Education](https://www.marist.edu/digital-education), Marist College, I had an opportunity to sovle a real time problem being faced by Digital Education Representatives. 
- **Issue to solve:**
  - Digital Education Representatives have to manually mail to all the faculties who have registered for thier workshop session daily in the morning based on the scheduled workshop timing & location
- **What I did:**
  - I learnt Django for different goal set by developing this [EmployeeWorkTimeLogManagement](https://github.com/vivekVells/EmployeeWorkTimeLogManagement) project and just before few days, this issue showed up. I found that this issue can be resolved using Django and this will be a good one to test my skills in Django.
  - I used Celery to schedule mailing action. Digital Ed Rep can now log into the website and set the automatic mailing timing manually or let it be sending mail by default on 08:00 AM daily so that the program can send mail to the faculties who have registered for the workshop accordingly. 
    - Celery is an asynchronous message queue manager and I used Redis as Message broker for it.

## Failures & Learnings
- I have failed in designing the architecture layout for this project initially; but after lots of iteration of the design, I was able to successfully complete it. 
- Will update the failures and learnings soon

## Response
- Got appreciated for the work I did from my supervisors and Web services team at Marist College

## For now
- Website alone completed
- Successfully able to schedule the timings and send the mails accordingly

## Future works
- Have to just link the backend from where this will pull the workshop information data
- To implement project as mobile app (Android using Kotlin)
- Use other info deliver medium other than email
- UI tweaks

### Project Working Demo
- [Video Link]() to be updated soon
- [Working Demo Files](https://github.com/vivekVells/InformationScheduledDeliverer/tree/master/WebsiteBlock/memories) 


### Tech Involved 
- Frontend language, Python, Django, SQLite3, Bootstrap, Celery, Redis

### Versions & Packages used
- python==3.6, celery==4.1.0, django==2.0.4, eventlet==0.22, django-celery-beat==1.1.1, django-celery-results==1.0.1, redis==2.10.6
- Redis-Server == 2.4.6.0 (install like file)
- For mailing, used gmail port  -> smtplib.SMTP_SSL('smtp.gmail.com', 465) - use this one for your project if you are interested, tried different ports that never worked.

### Features
- administer the scheduling mail actions

# App Previews
## Images
### Login Page
![]()
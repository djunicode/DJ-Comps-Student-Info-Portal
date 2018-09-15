# DJ Comps Student Information Portal
Information about Students with complete background, for use  primarily by recruiters.

## Use Case

- Information about Internships, Grades, Volunteer work, for reference of teachers, recruiters, department.

- **Verified Profiles**: To ensure that the information added by the student is not fake, a system of verification is used for every update a student makes to his/her profile.

- **Three Level of User Permissions**: A superuser, a teacher and the student. The student has the most basic access rights, the teacher verifies student information.

- **Dashboard for Student and Teachers**: A dashboard facility with interactive forms for students and teachers to regularly update profiles.

- **Filter-based Results**: For ease of use by teachers and recruiters, profiles can be filtered based on area of interest, research aptitude, projects, competitive coding skills etc.

- **Profile Updation and Analysis**: Whenever a student updates his/her profile, it can be viewed by all as a student progress in the respective domain. Analysis is carried out to show how much progress is carried it in the domain in how much time.

- **Connecting teachers and students**: When students take up projects under a college professor, the system users can view the professor portfolio and project details on the portal.

- **BE Project Information**: Giving details about final year projects like teacher co-ordinator, project domain, abstract etc. to gauge the area of interest of the student.

## Team Members
### Project Leader
Rudresh Panchal

### Mentors
Vishal Jain, Krutik Menkudle, Shraddha Shaligram, Saumya Shah

### Front End Developers
Parth Mehta, Sanika Potdar, Kushal Doshi, Vishesh Vohra

### Back End Developers
Ayush Kothari, Sarvesh Joglekar, Siddhant Soni




# To run this repo on your local:

- **Create a virtual environment using python 3.6**

- **Creating the database - Make sure you have Postgres installed on your machine. Follow the below steps in terminal after installing Postgres**
1. ```sudo su - postgres```
2. ```psql```
3. ```CREATE DATABASE info_portal;```
4. ```CREATE USER xyz WITH PASSWORD 'abc@123';```
5. ```ALTER ROLE xyz SET client_encoding TO 'utf8';```
6. ```ALTER ROLE xyz SET default_transaction_isolation TO 'read committed';```
7. ```ALTER ROLE xyz SET timezone TO 'UTC';```
8. ```GRANT ALL PRIVILEGES ON DATABASE info_portal TO xyz;```
9. ```\q```
10. ```exit```

- **Install all the dependencies of the project**
```pip3 install -r requirements.txt```


- **To run the project**
1. ```python manage.py makemigrations```
2. ```python manage.py migrate```
3. ```python manage.py runserver```

### Screenshots

- Landing Page
![0](https://user-images.githubusercontent.com/29770201/45575846-9804fd80-b892-11e8-8900-614a0fca018d.png)
- Landing Page
![3](https://user-images.githubusercontent.com/29770201/45575849-9b988480-b892-11e8-90e7-f8ba9a3c51d9.png)
- Teacher Dashboard
![teacherdashboard](https://user-images.githubusercontent.com/29770201/45575853-9e937500-b892-11e8-8ebb-ea0af950a127.png)
- Search and Filter page
![filter1](https://user-images.githubusercontent.com/29770201/45575871-a7844680-b892-11e8-9930-e73d21bc4aff.png)
- Edit Profile page for student
![edit](https://user-images.githubusercontent.com/29770201/45575874-a9e6a080-b892-11e8-968e-984e33601315.png)
- Student Profile page
![profile](https://user-images.githubusercontent.com/29770201/45575965-f631e080-b892-11e8-906d-51b42602ff36.png)

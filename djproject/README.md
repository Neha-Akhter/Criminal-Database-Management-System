
# Criminal Database Managment System

The Criminal Database Management System is a comprehensive software application created to enhance the management and organization of crime-related data. It serves the essential function of streamlining the registration and administration of data associated with various aspects of criminal cases, including complaints, criminal records, suspects, prisoners, and workforce details.



## Tech Stack


**Frontend:** HTML, CSS, Bootstrap, Django(Python)

**Backend:** MySQL

**Tool:** VS Code



## Installation

### 1. Clone the repository

First, clone this repository:

```bash
  git clone https://github.com/Neha-Akhter/Criminal-Database-Management-System.git
  cd Criminal-Database-Management-System
  cd djproject
```
### 2. Create a virtual environment

```bash
  virtualenv myenv
  source myenv/bin/activate
```

### 3. Install project dependencies

```bash
  pip install -r requirements.txt
```

### 4. Configure database and apply migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```
### 5. Run the application on local server

```bash
  python manage.py runserver
```

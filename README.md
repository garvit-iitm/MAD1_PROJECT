# MAD1_PROJECT
# Vehicle Parking App - V1

## Project Overview

This is a multi-user Vehicle Parking Management application developed as part of the Modern Application Development I (MAD1) course project. The app helps in managing multiple parking lots, parking spots, and parked vehicles, specifically designed for 4-wheeler parking.

## Features

- Admin and User login system
- Parking lot and spot management
- Vehicle parking and exit tracking
- Simple and responsive user interface using HTML, CSS, and Bootstrap
- Backend developed using Flask (Python) with SQLite database
- Templating handled via Jinja2

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Templating Engine:** Jinja2
- **Database:** SQLite
- **Version Control:** Git & GitHub

# Vehicle Parking App - Issues and Solutions Log

## Issue 1: Login Validation Logic

**What Happened:**
At first, login functionality was hardcoded to allow only a specific username and password ("garvit" and "pass").

**How It Was Fixed:**
Updated the logic to validate credentials directly from the User table in the database using SQLAlchemy:

```python
user = User.query.filter_by(username=username, password=password).first()
```

---

## Issue 2: Method Not Allowed Error

**What Happened:**
A POST request was being sent from the form but the corresponding route didn't accept POST by default.

**How It Was Fixed:**
Explicitly mentioned HTTP methods for the route:

```python
@app.route('/login', methods=['GET', 'POST'])
```

---

## Issue 3: URL Build Error (BuildError)

**What Happened:**
Flask complained about not finding the route endpoint 'login'. The actual function was named 'login\_page'.

**How It Was Fixed:**
Corrected the route call:

```python
return redirect(url_for('login_page'))
```

---

## Issue 4: SQLite Disk I/O Error

**What Happened:**
An SQLite disk I/O error occurred when trying to create or access the database.

**How It Was Fixed:**

* Closed all programs accessing the database.
* Checked and fixed file and folder permissions.
* Deleted and recreated the database using `db.create_all()`.

---

## Issue 5: Flash Messages Displaying on Unintended Pages

**What Happened:**
Flash messages intended for the login page were also showing on the registration page.

**How It Was Fixed:**
Restricted flash messages to only show on the login page using:

```html
{% if request.endpoint == 'login_page' %}
  {% with messages = get_flashed_messages(with_categories=true) %}
    ...
  {% endwith %}
{% endif %}
```

---

## Issue 6: Input Type Mistakes in Registration Form

**What Happened:**
Wrong input types were used (like `alphanumeric` and `numeric`), which are invalid in HTML.

**How It Was Fixed:**
Corrected input types to valid ones:

```html
<input type="text" name="address">
<input type="text" name="pincode" pattern="\d{6}">
```

---

## Issue 7: Port Already in Use

**What Happened:**
The port (5054) was occupied by another process, so the Flask app couldn’t start.

**How It Was Fixed:**

* Either changed the port in `app.run()`:

```python
app.run(port=5055)
```

* Or freed the port using Linux commands:

```bash
lsof -i :5054
kill -9 <PID>
```

---

## Issue 8: Database Design Clarification

**What Happened:**
Clarified how tables like User, Admin, ParkingLot, ParkingSpot, Reservation are connected using foreign keys and relationships in SQLAlchemy.

**How It Was Solved:**
All relationships between tables were defined clearly using SQLAlchemy `ForeignKey` and `relationship`.

---

## General Improvements Made

* Fixed spelling mistakes such as changing "Registeration" to "Registration".
* Centered the login button.
* Added a 'New User? Register here' message below the login button.
* Changed login heading color to red using Bootstrap class `text-danger`.

---

## Conclusion

All problems and doubts during development were resolved manually through proper debugging and code correction without using automation tools. The project is functioning as expected and is ready for demonstration or viva.

---

Prepared manually by Garvit Bhatnagar for the Vehicle Parking App (2025).


# 🚗 Vehicle Parking Management System

A full-stack web application for managing vehicle parking efficiently using Flask, SQLite, Bootstrap, and Jinja2. This project offers seamless interfaces for both **users** and **administrators** to interact with parking lots in real time.

> 📽️ **[Watch Demo Video](https://drive.google.com/file/d/18jhauNpSMuhFjG5ryEZK59afJkWGXszr/view?usp=sharing)**

---

## 👨‍💻 Author

**Garvit Singh Bhatnagar**  
- B.Tech (CSE - AI) @ Galgotias College of Engineering and Technology  
- BS in Data Science @ IIT Madras  
- ✉️ garvitsinghbhatnagar289@gmail.com

---

## 🧰 Tech Stack

### Backend
- **Flask** – Core web framework
- **Flask-SQLAlchemy** – ORM for interacting with SQLite
- **Flask-Session & Flash** – For authentication and notifications

### Frontend
- **HTML5 + CSS3**
- **Bootstrap 4.5** – Responsive UI
- **Jinja2** – HTML templating engine

### Database
- **SQLite** – Lightweight file-based RDBMS

---

## 🚀 Features

### 👤 User Panel
- User registration & login
- Edit profile
- Book available parking spots
- Release spots with auto cost calculation
- View real-time availability
- Reservation history
- Parking summary dashboard

### 🔧 Admin Panel
- Secure admin login
- Add, edit, or delete parking lots
- Auto-generate parking spots
- View and manage user profiles
- Spot status analytics (available vs occupied)
- Revenue and occupancy summary

### 🔍 Search
- Users can search parking lots by:
  - Prime location
  - Address
  - PIN code

---

## 🗂️ Project Structure

```

├── app.py                 # Main Flask application
├── models/
│   └── database.py        # SQLAlchemy models
├── templates/             # HTML templates (Jinja2)
├── static/                # Static files (CSS, JS)
├── parking.db             # SQLite database

````

---

## ⚙️ Setup Instructions

1. **Clone this repository**  
   ```bash
   git clone https://github.com/yourusername/vehicle-parking-system.git
   cd vehicle-parking-system
````

2. **Set up virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Visit in browser:**
   Open [http://localhost:5054](http://localhost:5054)

---

## 🧠 AI/LLM Usage

AI/LLMs were used minimally (\~5–7%) for:

* Bug fixing
* Route optimization
* UI structuring
  All logic and design decisions were developer-driven.

---

## 📽️ Demo Video

▶️ **[Click to Watch the Demo](https://drive.google.com/file/d/18jhauNpSMuhFjG5ryEZK59afJkWGXszr/view?usp=sharing)**

---

## 📄 License

This project is for academic and learning purposes. Modify and build upon it freely. Attribution appreciated.

```


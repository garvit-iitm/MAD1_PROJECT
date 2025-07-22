Certainly! Here's your complete and detailed `README.md` file with all sections including the **correctly formatted Setup Instructions**, so you can copy-paste it directly into your GitHub project:


# 🚗 Vehicle Parking Management System

A full-stack web application for efficiently managing vehicle parking using Flask, SQLite, Bootstrap, and Jinja2. This project supports both **user** and **admin** functionalities with intuitive dashboards, spot booking, cost calculation, and dynamic summaries.

> 📽️ **[Watch Demo Video](https://drive.google.com/file/d/18jhauNpSMuhFjG5ryEZK59afJkWGXszr/view?usp=sharing)**

---

## 👨‍💻 Author

**Garvit Singh Bhatnagar**  
- B.Tech in CSE (AI) @ Galgotias College of Engineering and Technology  
- BS in Data Science @ IIT Madras  
- 📧 garvitsinghbhatnagar289@gmail.com  
- 🌐 [LinkedIn](https://www.linkedin.com/in/bhatnagargarvitsingh/) | [GitHub](https://github.com/garvit-iitm)

---

## 🧰 Tech Stack

### 🔙 Backend
- **Flask** – Python microframework for web apps  
- **Flask-SQLAlchemy** – ORM for interacting with the database  
- **Flask-Session & Flash** – Authentication and UI feedback  
- **Werkzeug** – Underlying routing and security utilities  

### 🧮 Database
- **SQLite** – Lightweight embedded RDBMS  
- **SQLAlchemy** – ORM for model definition and query management  

### 🎨 Frontend
- **HTML5** – Markup for page structure  
- **CSS3** – Styling  
- **Bootstrap 4.5** – UI components and responsiveness  
- **Jinja2** – Python templating engine  

---

## 🚀 Features

### 👤 User Dashboard
- Secure registration and login  
- Profile editing  
- Search parking lots by location/address/PIN  
- Book an available parking spot  
- Release a spot with cost calculation (based on time spent)  
- View reservation history  
- Visual summary of parking availability and revenue  

### 🛠️ Admin Dashboard
- Admin-only login  
- Add, edit, delete parking lots  
- Auto-create multiple parking spots per lot  
- View lot, spot, and user details  
- Delete users and free up their spots  
- Analytics dashboard with revenue and occupancy charts  

### 🔍 Search
- Search lots by location or user ID  
- View individual spot details (available & occupied)  

---

## 🗂️ Project Structure



```

├── app.py                 # Main Flask application
├── models/
│   └── database.py        # SQLAlchemy models for all entities
├── templates/             # HTML templates (user.html, admin.html, etc.)
├── static/                # CSS, JS, image assets
├── parking.db             # SQLite database
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies (optional)

```



## ⚙️ Setup Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/vehicle-parking-system.git
   cd vehicle-parking-system

2. **Set up virtual environment (optional but recommended)**
   For macOS/Linux:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   For Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
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
   ```bash
   Open [http://localhost:5054](http://localhost:5054)
   ```
---

## 📊 Sample User Credentials

| Role  | Username | Password |
| ----- | -------- | -------- |
| Admin | admin    | admin123 |
| User  | testuser | testpass |

*(You can register your own user too)*

## 📦 Database Schema

### 🧑 User Table

| Column    | Type     | Description             |
|-----------|----------|-------------------------|
| id        | Integer  | Primary key             |
| username  | String   | Unique user name        |
| password  | String   | User password           |

### 🅿️ ParkingLot Table

| Column                  | Type     | Description                      |
|-------------------------|----------|----------------------------------|
| id                      | Integer  | Primary key                      |
| prime_location_name     | String   | Location name                    |
| price                   | Float    | Rate per hour                    |
| address                 | String   | Full address                     |
| pin_code                | String   | PIN code                         |
| maximum_number_of_spots| Integer  | Total spot capacity              |

### 🔲 ParkingSpot Table

| Column     | Type     | Description              |
|------------|----------|--------------------------|
| id         | Integer  | Primary key              |
| lot_id     | Integer  | Foreign key to ParkingLot|
| spot_number| String   | e.g., Spot-1, Spot-2     |
| status     | String   | 'A' (Available), 'O' (Occupied) |

### 📄 Reservation Table

| Column            | Type     | Description                        |
|-------------------|----------|------------------------------------|
| id                | Integer  | Primary key                        |
| spot_id           | Integer  | Foreign key to ParkingSpot         |
| user_id           | Integer  | Foreign key to User                |
| vehicle_no        | String   | Vehicle number                     |
| parking_timestamp | DateTime | Check-in time                      |
| leaving_timestamp | DateTime | Check-out time                     |
| parking_cost      | Float    | Auto-calculated based on duration  |
| status            | String   | 'O' or 'A'                         |

---

## 🧠 AI/LLM Usage

AI/LLMs were used minimally (\~5–7%) to assist with:

* Bug fixes and debugging
* Optimizing route logic
* Structuring HTML and Flask code

🛑 **Note**: All decision-making, architecture design, and core logic were human-authored. No autonomous AI-generated logic was included.

---

## 📽️ Demo Video

▶️ **[Click to Watch the Demo](https://drive.google.com/file/d/18jhauNpSMuhFjG5ryEZK59afJkWGXszr/view?usp=sharing)**

This video covers:

* User flow (login → book → release)
* Admin panel features (lot creation, analytics)
* Real-time database interactions

---

## 📄 License

This project is for educational purposes and open to public contributions. Feel free to fork, use, and improve. Attribution is appreciated but not required.


# 👥 User Manager API
A simple RESTful API built with **Flask**, allowing you to manage users (create, read, update, delete).  
Perfect for learning backend fundamentals or using as a base for bigger Flask projects.

---

##  Features
-  Get all users
-  Get user by ID
-  Add new users
-  Update user information
-  Delete users
-  JSON-based REST API
  
---

##  Tech Stack
| Component | Technology |
| **Backend** | Flask (Python) |
| **Language** | Python 3.10+ |
| **Database** | In-memory list (no DB yet) |
| **Format** | JSON API |

---

## ⚙️ Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/user-manager-api.git
   cd user-manager-api
Create a virtual environment

bash
Copy code
python -m venv venv
venv\Scripts\activate      # Window
Install dependencies

bash
Copy code
pip install Flask
Run the app

bash
Copy code
python app.py
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000
🔑 API Endpoints
Method	Endpoint	Description
GET	/users	Get all users
GET	/users/<id>	Get a specific user
POST	/users	Add a new user
PUT	/users/<id>	Update an existing user
DELETE	/users/<id>	Delete a user

 Example JSON (for adding a user)
json
Copy code
{
  "name": "John Doe",
  "email": "john@example.com",
  "role": "admin"
}
 Example Responses
GET /users

json
Copy code
[
  {"id": 1, "name": "Samandar", "email": "samandar@example.com", "role": "admin"},
  {"id": 2, "name": "Ali", "email": "ali@example.com", "role": "user"}
]
POST /users

json
Copy code
{
  "id": 3,
  "name": "John Doe",
  "email": "john@example.com",
  "role": "admin"
}
 Project Structure
sql
Copy code
user-manager-api/
│
├── app.py
└── README.md
☁️ Deployment
You can deploy this API easily on:

Render

Railway

PythonAnywhere

#  Author 
Developed by Coder-dev2006
 For learning and personal projects.

#  License
This project is licensed under the MIT License — you can freely use, modify, and distribute it.

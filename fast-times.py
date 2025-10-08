from flask import Flask, jsonify, request

app = Flask(__name__)

# Dastlabki foydalanuvchilar ro‘yxati
users = [
    {"id": 1, "name": "Samandar", "email": "samandar@example.com", "role": "admin"},
    {"id": 2, "name": "Ali", "email": "ali@example.com", "role": "user"},
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the User Manager API 👋"})

# Barcha foydalanuvchilarni olish
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# ID bo‘yicha foydalanuvchini olish
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Yangi foydalanuvchi qo‘shish
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400
    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"],
        "email": data["email"],
        "role": data.get("role", "user")
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Foydalanuvchini yangilash
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    user.update({
        "name": data.get("name", user["name"]),
        "email": data.get("email", user["email"]),
        "role": data.get("role", user["role"])
    })
    return jsonify(user)

# Foydalanuvchini o‘chirish
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": f"User {user_id} deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template_string, redirect
import json
import os

app = Flask(__name__)

# HTML and CSS embedded directly in Python
login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <style>
        body {
            background: linear-gradient(to right, #74ebd5, #ACB6E5);
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            width: 300px;
        }
        h2 {
            text-align: center;
            margin-bottom: 24px;
        }
        input[type="email"], input[type="password"] {
            width: 100%;
            padding: 12px;
            margin: 8px 0 16px;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .message {
            text-align: center;
            margin-top: 16px;
            color: green;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form method="POST">
            <input type="email" name="email" placeholder="Email" required />
            <input type="password" name="password" placeholder="Password" required />
            <button type="submit">Submit</button>
        </form>
        {% if message %}
        <div class="message">{{ message }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user_data = {"email": email, "password": password}

        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                users = json.load(f)
        else:
            users = []

        users.append(user_data)
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

        message = "Login successful! Credentials saved."

    return render_template_string(login_page, message=message)

if __name__ == "__main__":
    app.run(host="localhost", port=9999)


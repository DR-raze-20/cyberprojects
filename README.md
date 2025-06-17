# 🎣 Phishing Login Simulator (Educational Project)

This project simulates a fake login page using Flask to demonstrate how phishing attacks work. It captures submitted credentials locally and then redirects the user to a real site (e.g., YouTube). This is intended for ethical hacking education and awareness only.

## ⚠️ Disclaimer

This tool is for **educational use only**. Do **not** deploy or use it against real users or systems without **explicit authorization**. Misuse can result in **legal consequences**.

## 🔧 How It Works

1. User lands on a fake "YouTube Login" page.
2. When they input a username and password:
   - The credentials are saved to `stolen_credentials.txt`.
   - The user is redirected to `https://youtube.com`.

## 🚀 Running the Project

### Prerequisites:
- Python 3
- Flask

### Steps:

```bash
git clone https://github.com/your-username/phishing-simulator.git
cd phishing-simulator
pip install flask
python app.py

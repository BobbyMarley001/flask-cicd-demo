# 🚀 Flask CI/CD Demo

A simple Flask web application to demonstrate CI/CD pipelines using **GitHub Actions** and deployment on **Render**.

---

## 📆 License

This project is licensed under the MIT License. See the full license text in the [LICENSE](LICENSE) file.

---

## 📆 Features

* ✅ Flask web server (`app.py`)
* ✅ Unit test with `pytest`
* ✅ GitHub Actions for automated testing
* ✅ Deployment to Render
* ✅ CI/CD integration with each push to `main` branch

---

## 🏗️ Project Structure

```
flask-cicd-demo/
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # HTML template
├── tests/
│   └── test_app.py       # Pytest test file
├── requirements.txt      # Python dependencies
├── .github/
│   └── workflows/
│       └── python-app.yml  # GitHub Actions workflow
└── README.md             # Project overview
```

---

## 🧪 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/BobbyMarley001/flask-cicd-demo.git
cd flask-cicd-demo
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Visit `http://localhost:5000`

---

## ✅ Run Tests

```bash
pytest
```

---

## ⚙️ GitHub Actions CI/CD

This project includes a GitHub Actions workflow:

* Runs on every push or pull request to `main`
* Installs dependencies
* Runs `pytest` to ensure tests pass

Path: `.github/workflows/python-app.yml`

---

## ☁️ Deploying to Render

### 📟 Setup Instructions

1. Go to [https://render.com](https://render.com)
2. Create a **new Web Service**
3. Fill out the fields:

   * **Name:** `flask-cicd-demo`
   * **Build Command:**

     ```bash
     pip install -r requirements.txt
     ```
   * **Start Command:**

     ```bash
     gunicorn app:app
     ```
   * **Instance Type:** Free (or paid, as needed)
   * **Region:** Singapore (or your choice)
4. Click **Deploy Web Service**

Render will build and deploy your app using the latest code from the `main` branch.

---

## 📟 Requirements

```txt
Flask==2.3.3
pytest
gunicorn
```

---

## 🧑‍💻 Author

**Bobby Marley**
GitHub: [@BobbyMarley001](https://github.com/BobbyMarley001)

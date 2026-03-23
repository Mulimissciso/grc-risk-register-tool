# grc-risk-register-tool
# project overview

Building a mini grc tool. A system that maps controls controls to frameworks, tracks risks &amp; vulnerabilities, monitors compliance status and generate audit ready reports.
This project is a lightweight GRC tool designed to automate risk identification, scoring, and tracking. It simulates how enterprise GRC platforms manage risk registers and compliance processes.

## ✨ Personal Motivation

For a long time, I understood risk management conceptually, but I lacked a practical way to apply and validate that knowledge.

This project is a personal initiative to move from theory to practice — to build something tangible that reflects how risk management works in real-world systems.  
More than a portfolio piece, this project is a way for me to challenge myself, solidify my understanding, and prove that I can design and implement risk-based thinking in a functional system.

## Objectives
- Translate theoretical risk management knowledge into a working system
- Automate risk scoring and classification
- Build a centralized and structured risk register
- Simulate real-world GRC workflows and processes

  ## ⚙️ Features
- Add risks via API (POST request)
- Retrieve all risks (GET request)
- Automatic risk scoring (Likelihood × Impact)
- Risk classification (Low, Medium, High)
- In-memory data storage (initial prototype)

 ## 🛠️ Tech Stack

- Python
- Flask (REST API framework)
- cURL (API testing)

## 🔌 API Endpoints

### Add Risk
POST /add_risk

### Get All Risks
GET /risks

## 🚀 How to Run

1. Clone the repository:
   git clone <>

2. Navigate into the project folder:
   cd grc-risk-register-tool

3. Install dependencies:
   pip install flask

4. Run the application:
   python app.py

5. Access the API at:
   http://127.0.0.1:5000

   ## 📂 Project Structure

grc-risk-register-tool/
│── app.py
│── README.md
│── docs/

## 📘 Documentation

Detailed build steps and implementation notes are available in the /docs folder.

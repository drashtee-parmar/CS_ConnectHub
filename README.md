# CS_ConnectHub
An AI-powered web platform built with Flask and OpenAI API that connects students, faculty, and alumni through an intelligent chatbot interface for quick access to academic and networking information.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![OpenAI API](https://img.shields.io/badge/OpenAI-Integrated-orange.svg)

## Table of contents
- [Overview](#overview)
- [User Story](#user-story)
- [Acceptance Criteria](#acceptance-criteria)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Visuals](#project-visuals)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Run on a custom port](#run-on-a-custom-port)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Tools Used ](#tools-used )
- [References](#references)

---

## Overview
**CS_ConnectHub** is a Flask-based web application that enables students, faculty, and alumni to interact through an AI-powered chatbot interface.  
It allows users to retrieve relevant academic and professional information by selecting a category and engaging in a conversational experience.

**Personas:**
- **Student:** Needs academic guidance, course info, or networking opportunities.
- **Faculty:** Shares expertise, academic guidance, and career advice.
- **Alumni:** Offers mentorship, job insights, and industry connections.
---
##  User Story
> Create a mscs application that allows the student to interact and retrive information from Faculty, Alumini and Student, on selection using chatbot.
---
##  Acceptance Criteria
- Ability to choose between **Faculty**, **Alumni**, or **Student** chat modes.
- AI-generated responses relevant to the selected persona.
- Responsive and accessible UI design.
- Secure storage of API keys.

---
##  Features
- AI chatbot integration using **OpenAI API**
- Role-based interaction: **Students**, **Faculty**, and **Alumni**
- Clean, responsive UI built with **HTML, CSS, and Bootstrap**
- `.env` support for secure API key storage
- Modular structure for easy scaling

---

## Project Visuals
![Campus Connect Main Page](images/CampusConnectMainPage.png)  
![Campus Connect Faculty Page](images/Faculty.png)  

---
 ## Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/drashtee-parmar/CS_ConnectHub.git
cd CS_ConnectHub
```

### 2️⃣ Create & Activate Virtual Environment
```
python -m venv .venv
source .venv/bin/activate     # Mac/Linux
.venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a .env file in the project root:
```
OPENAI_API_KEY=your_openai_api_key
FLASK_ENV=development
```
Note: ⚠ Do not commit .env to source control.

---
### Running the Application
```
flask run
```
---
### Run on a custom port:

```commandline
flask run -h localhost -p 3000
```
---
## Deployment
- [Github Repository: Source Code](https://github.com/drashtee-parmar/CS_ConnectHub)
- [Live Demo](https://cs-connecthub-app-01f88dff8294.herokuapp.com/)
---
##  Project Structure
```
CS_ConnectHub/
│– .venv/
│– images/
│   ├── CampusConnectMainPage.png
│   ├── Faculty.png
│– static/
│   ├── styles.css
│– templates/
│   ├── alumni.html
│   ├── faculty.html
│   ├── index.html
│   ├── students.html
│– .env
│– .gitignore
│– app.py
│– requirements.txt
│– README.md

```
## Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML5, CSS3, Bootstrap  
- **AI Engine:** OpenAI API  
- **Environment Management:** python-dotenv  
- **Version Control:** Git & GitHub  

---
## Tools Used 
- [Presentation](Hackathon_Fall23_CodeBusters_Latest794c046eb9357f5654c874e48eff1a064f1a0b1119c5ea04e7db54db1ed17aa2.pptx)
- [Requirement Traceability Matrix](Requirement_Traceability_Matrix0acf999732bebd053887fe8e664821c7744e819db385284794fe208ea5cd91f5.xlsx)
- [Connector test cases](Connector_TestCases40ea3a478045dc8a8371a9627a5d15f2ef329c496222fad6a499283ea05900cf.xlsx)
---

## References
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Font Awesome](https://fontawesome.com/v5.15/icons?d=gallery&p=2)
- [Design](https://www.canva.com/)
---

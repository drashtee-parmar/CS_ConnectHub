import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set. Please configure it in your .env file.")
client = OpenAI(api_key=api_key)

# Faculty, alumni, and advisor data
faculty_members = [
    {"name": "Professor Karayakya", "subject": "Machine Learning"},
    {"name": "Professor Shaw", "subject": "Information Retrieval"},
    {"name": "Professor Choi", "subject": "Data Warehousing and Mining"},
    {"name": "Professor Khan", "subject": "Natural Language Processing"},
]

Student_advisor_members = [
    {"name": "Career Advisor Nurse", "advisor": "Resume Building"},
    {"name": "Career Advisor Sherif", "advisor": "Career Advising"},
    {"name": "Career Advisor Rodger", "advisor": "Personality Development"},
]

alumni_members = [
    {"name": "John Smith", "company": "Google", "graduation": "2020"},
    {"name": "Alex Hales", "company": "Microsoft", "graduation": "2000"},
    {"name": "Agith Agarkar", "company": "Facebook", "graduation": "2004"},
]

# ------------------------------
# OpenAI Chat Handler
# ------------------------------
def conversation(messages, temperature=0.4):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=temperature,
            max_tokens=512,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return "The chatbot was unable to process your request at this time."

# ------------------------------
# ROUTES
# ------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/faculty")
def faculty():
    return render_template("faculty.html", faculty=faculty_members)

@app.route("/alumni")
def alumni():
    return render_template("alumni.html", alumni=alumni_members)

@app.route("/students")
def students():
    return render_template("students.html", student=Student_advisor_members)

# ------------------------------
# CHAT ENDPOINTS
# ------------------------------

# Faculty Chat API
@app.route("/facultychat", methods=["POST"])
def faculty_chat():
    data = request.get_json()
    faculty_name = data[0].get("Professor Name", "Unknown Professor")
    subject = data[1].get("Subject Taught", "Unknown Subject")
    question = data[2].get("Question", "")

    context = [
        {"role": "system", "content": f"You are {faculty_name}, an expert in {subject}. Provide clear, professional answers."},
        {"role": "user", "content": question}
    ]

    answer = conversation(context)
    return jsonify({"faculty_name": faculty_name, "user_message": question, "assistant_response": answer})

# Alumni Chat API
@app.route("/alumnichat", methods=["POST"])
def alumni_chat():
    data = request.get_json()
    alumni_name = data.get("alumni_name", "Unknown Alumni")
    department = data.get("department", "Unknown Department")
    grad_year = data.get("graduation_year", "Unknown Year")
    company = data.get("company", "Unknown Company")
    question = data.get("question", "")

    context = [
        {"role": "system", "content": f"You are {alumni_name}, a {department} graduate ({grad_year}), working at {company}. Share relevant insights."},
        {"role": "user", "content": question}
    ]

    answer = conversation(context)
    return jsonify({"alumni_name": alumni_name, "user_message": question, "assistant_response": answer})

# Student Advisor Chat API
@app.route("/studentadvisorchat", methods=["POST"])
def student_advisor_chat():
    data = request.get_json()
    advisor_name = data.get("advisor_name", "Unknown Advisor")
    expertise = data.get("career_advisor", "Career Guidance")
    question = data.get("question", "")

    context = [
        {"role": "system", "content": f"You are {advisor_name}, an expert in {expertise}. Provide concise, practical guidance."},
        {"role": "user", "content": question}
    ]

    answer = conversation(context)
    return jsonify({"advisor_name": advisor_name, "user_message": question, "assistant_response": answer})


# Teaching Assistant Chat Example
@app.route("/teachingassistant")
def teaching_assistant_chat():
    assistant_name = "Teaching Assistant"
    question = "Explain the basics of web scraping."

    context = [
        {
            "role": "system",
            "content": f"{assistant_name} is an expert in Information Retrieval. "
                       f"Provide clear and accurate explanations."
        },
        {"role": "user", "content": question}
    ]

    response = conversation(context)
    return render_template(
        "assistant_chat.html",
        assistant_name=assistant_name,
        user_message=question,
        assistant_response=response,
    )

# Run App
if __name__ == "__main__":
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

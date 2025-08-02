# import openai
# import os
# from flask import Flask, render_template, request, redirect, url_for, jsonify
# from flask import Flask, render_template, request
# import openai
#
# app = Flask(__name__)
#
# # Replace 'YOUR_API_KEY' with your actual OpenAI API key
#
# # Define the list of faculty members (you can expand this list)
# faculty_members = [
#     {"name": "Professor Karayakya", "subject": "Machine Learning"},
#     {"name": "Professor Shaw", "subject": "Information Retrieval"},
#     {"name": "Professor Choi", "subject": "Data Warehousing and Mining"},
#     {"name": "Professor Khan", "subject": "Natural Language Processing"},
# ]
# Student_advisor_memebers = [
#     {"name": "Carrer Advisor Nurse", "Adviosr": "Resume Building"},
#     {"name": "Carrer Advisor Sherif", "Advisor": "Career Advising"},
#     {"name": "Carrer Advisor Rodger", "Advisor": "Personality Development"},
# ]
# alumni_members = [
#     {"name": "John Smith", "Working at google": "Graduated in 2020"},
#     {"name": "Alex hales", "Working at microsfot": "Graduated in 2000"},
#     {"name": "Agith Agarkar ", "Working at Facebook": "Graduated in 2004"},
# ]
#
#
# app = Flask(__name__)
#
# # Set your OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")
#
#
# # openai.api_key = ""
# # openai.api_key = os.getenv("OPENAI_API_KEY")
# # if not api_key:
# #     print("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
# #     exit(1)
#
# def conversation(messages, temperature=0.7):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages,
#         temperature=temperature,
#     )
#     return response.choices[0].message["content"]
#
#
# @app.route("/facultychat", methods=["POST"])
# def Facutly_chat():
#     if request.method == "POST":
#         print(request.get_json())
#         input_info = request.get_json()
#         print(type(input_info))
#         question = input_info[2]["Question"]
#         print("User Question", question)
#         print(request.args)
#         faculty_name = input_info[0]["Professor Name"]  # Default faculty name
#         subject_name = input_info[1]["Subject Taught"]  # Subject taught
#         # question = "What is Cosine Similarity Score?"  # Default question
#
#         # Create or load the context for the conversation
#         context = [
#             {
#                 "role": "system",
#                 "content": f"{faculty_name} is teaching the subject of "
#                            f"{subject_name}. He should be able to answer queries related to the subject. Please feel free to ask any questions related to "
#                            f"{subject_name}.",
#             }
#         ]
#
#         # Append the user's question to the conversation context
#         context.append({"role": "user", "content": question})
#
#         # Get the assistant's response
#         response = conversation(context)
#
#         # Append the assistant's response to the context
#         context.append({"role": "assistant", "content": response})
#
#         # Print the answer to the console
#         print("Assistant's Response:", response)
#         print(type(response))
#         print("Done")
#         # return render_template('faculty.html', faculty_name=faculty_name, user_message=question, assistant_response=response)
#         return jsonify(
#             {
#                 "faculty_name": faculty_name,
#                 "user_message": question,
#                 "assistant_response": response,
#             }
#         )
#
#
# @app.route("/")
# def index():
#     print("Going for Index.html")
#     return render_template("index.html")
#
#
# @app.route("/faculty")
# def faculty():
#     print("Accessed the faculty route")
#     # return render_template("faculty.html",faculties=faculty_members)
#     return render_template("faculty.html", faculty=faculty_members)
#
#
# @app.route("/alumni")
# def alumni():
#     print("Accessed the alumni route")
#     # Return the alumni HTML template with alumni data
#     return render_template("alumni.html", alumni=alumni_members)
#
#
# @app.route("/alumnichat", methods=["POST"])
# def alumni_chat():
#     if request.method == "POST":
#         input_info = request.get_json()
#         question = input_info[4]["Question"]
#         alumni_name = input_info[0]["Alumni Name"]
#         alumni_department = input_info[1]["Department"]
#         graduation_year = input_info[2]["Graduation Year"]
#         company_working = input_info[3]["Current Position"]
#
#         context = [
#             {
#                 "role": "system",
#                 "content": f"{alumni_name} graduated in "
#                            f"{graduation_year} from the"
#                            f"{alumni_department} department. They are currently working at"
#                            f" {company_working}. They can provide insights and advice related to their experience at our university and their work field at"
#                            f" {company_working}. Please feel free to ask any questions.",
#             }
#         ]
#
#         # Append the user's question to the conversation context
#         context.append({"role": "user", "content": question})
#
#         # Get the assistant's response using your conversation function
#         response = conversation(context)  # You need to define this function
#
#         # Append the assistant's response to the context
#         context.append({"role": "assistant", "content": response})
#
#         # Print the answer to the console
#         print("Assistant's Response:", response)
#         print("Done")
#
#         # Return the response as JSON
#         return jsonify(
#             {
#                 "alumni_name": alumni_name,
#                 "user_message": question,
#                 "assistant_response": response,
#             }
#         )
#
#
# @app.route("/teachingassistat")
# def assitant_chat():
#     assistant_name = "Teaching Assistant"  # Assistant's name
#     question = "Hey, I need some help to understand the topic of web scraping."  # Default question
#
#     # Create or load the context for the conversation
#     context = [
#         {
#             "role": "system",
#             "content": f"{assistant_name} is a teaching assistant for Information Retrieval. Students can ask questions about the subject.",
#         }
#     ]
#
#     # Append the student's question to the conversation context
#     context.append({"role": "user", "content": question})
#
#     # Get the assistant's response
#     response = conversation(context)
#
#     # Append the assistant's response to the context
#     context.append({"role": "assistant", "content": response})
#
#     # Print the answer to the console
#     print("Assistant's Response:", response)
#
#     return render_template(
#         "assistant_chat.html",
#         assistant_name=assistant_name,
#         user_message=question,
#         assistant_response=response,
#     )
#
#
# @app.route("/students")
# def students():
#     # Add students-related functionality here
#     return render_template("students.html", student=Student_advisor_memebers)
#
#
# @app.route("/studentadvisorchat", methods=["POST"])
# def studet_advisor_chat():
#     if request.method == "POST":
#         print(request.get_json())
#         input_info = request.get_json()
#         print(type(input_info))
#         question = input_info[2]["Question"]
#         print("User Question", question)
#         print(request.args)
#         advisor_name = input_info[0]["Advisor Name"]
#         career_advisor = input_info[1]["Carrer Advisor"]
#         # question = "What is Cosine Similarity Score?"  # Default question
#
#         # Create or load the context for the conversation
#         context = [
#             {
#                 "role": "system",
#                 "content": f"{advisor_name} is teaching the subject of "
#                            f"{career_advisor}. He should be able to answer queries related to the subject. Please feel free to ask any questions related to "
#                            f"{career_advisor}.",
#             }
#         ]
#
#         # Append the user's question to the conversation context
#         context.append({"role": "user", "content": question})
#
#         # Get the assistant's response
#         response = conversation(context)
#
#         # Append the assistant's response to the context
#         context.append({"role": "assistant", "content": response})
#
#         # Print the answer to the console
#         print("Assistant's Response:", response)
#         print(type(response))
#         print("Done")
#         # return render_template('faculty.html', faculty_name=faculty_name, user_message=question, assistant_response=response)
#         return jsonify(
#             {
#                 "advisor_name": advisor_name,
#                 "user_message": question,
#                 "assistant_response": response,
#             }
#         )
#
#
# # faculties = {['Prof. Alan Shaw', 'Information Retrieval', 'ashaw8@kennesaw.edu']}
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

# ===========================================================================

# import os
# from flask import Flask, render_template, request, jsonify
# from openai import OpenAI
# from dotenv import load_dotenv
#
# # Load environment variables from .env
# load_dotenv()
#
# # Read API Key from Environment (Fail Fast if Missing)
# api_key = os.getenv("OPENAI_API_KEY")
# if not api_key:
#     raise RuntimeError(" OPENAI_API_KEY environment variable is not set. Please export it before running the app.")
#
# # Initialize OpenAI Client
# client = OpenAI(api_key=api_key)
#
# # Initialize Flask
# app = Flask(__name__)
#
# # Initialize OpenAI Client
# # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#
# def conversation(messages, temperature=0.7):
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",  #  Latest powerful model
#             messages=messages,
#             temperature=temperature,
#         )
#         return response.choices[0].message.content
#     except Exception as e:
#         print(f"OpenAI API Error: {e}")
#         return "Unable to fetch a response from the chatbot. Please check API configuration."
#
#
# # ------------------------------
# # Faculty / Alumni / Advisor Data
# # ------------------------------
# faculty_members = [
#     {"name": "Professor Karayakya", "subject": "Machine Learning"},
#     {"name": "Professor Shaw", "subject": "Information Retrieval"},
#     {"name": "Professor Choi", "subject": "Data Warehousing and Mining"},
#     {"name": "Professor Khan", "subject": "Natural Language Processing"},
# ]
#
# student_advisors = [
#     {"name": "Career Advisor Nurse", "expertise": "Resume Building"},
#     {"name": "Career Advisor Sherif", "expertise": "Career Advising"},
#     {"name": "Career Advisor Rodger", "expertise": "Personality Development"},
# ]
#
# alumni_members = [
#     {"name": "John Smith", "company": "Google", "graduation_year": "2020"},
#     {"name": "Alex Hales", "company": "Microsoft", "graduation_year": "2000"},
#     {"name": "Agith Agarkar", "company": "Facebook", "graduation_year": "2004"},
# ]
#
# # ------------------------------
# # OpenAI Chat Function
# # ------------------------------
# def ask_openai(system_prompt, user_prompt, model="gpt-4o-mini", temperature=0.7):
#     """Handles conversation with OpenAI using the latest API."""
#     response = client.chat.completions.create(
#         model=model,
#         messages=[
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": user_prompt}
#         ],
#         temperature=temperature,
#     )
#     return response.choices[0].message.content.strip()
#
# # ------------------------------
# # Faculty Chat Route
# # ------------------------------
# @app.route("/facultychat", methods=["POST"])
# def faculty_chat():
#     data = request.get_json()
#     faculty_name = data[0]["Professor Name"]
#     subject = data[1]["Subject Taught"]
#     question = data[2]["Question"]
#
#     system_msg = f"You are {faculty_name}, an expert in {subject}. Answer student queries with clarity."
#     answer = ask_openai(system_msg, question)
#
#     return jsonify({"faculty_name": faculty_name, "user_message": question, "assistant_response": answer})
#
# # ------------------------------
# # Alumni Chat Route
# # ------------------------------
# @app.route("/alumnichat", methods=["POST"])
# def alumni_chat():
#     data = request.get_json()
#     alumni_name = data[0]["Alumni Name"]
#     department = data[1]["Department"]
#     grad_year = data[2]["Graduation Year"]
#     company = data[3]["Current Position"]
#     question = data[4]["Question"]
#
#     system_msg = f"You are {alumni_name}, a {department} graduate of {grad_year}, currently at {company}. Provide insights based on your experience."
#     answer = ask_openai(system_msg, question)
#
#     return jsonify({"alumni_name": alumni_name, "user_message": question, "assistant_response": answer})
#
# # ------------------------------
# # Student Advisor Chat
# # ------------------------------
# @app.route("/studentadvisorchat", methods=["POST"])
# def advisor_chat():
#     data = request.get_json()
#     advisor_name = data[0]["Advisor Name"]
#     expertise = data[1]["Career Advisor"]
#     question = data[2]["Question"]
#
#     system_msg = f"You are {advisor_name}, an expert in {expertise}. Advise students professionally."
#     answer = ask_openai(system_msg, question)
#
#     return jsonify({"advisor_name": advisor_name, "user_message": question, "assistant_response": answer})
#
# # ------------------------------
# # Routes for Pages
# # ------------------------------
# @app.route("/")
# def index():
#     return render_template("index.html")
#
# @app.route("/faculty")
# def faculty():
#     return render_template("faculty.html", faculty=faculty_members)
#
# @app.route("/alumni")
# def alumni():
#     return render_template("alumni.html", alumni=alumni_members)
#
# @app.route("/students")
# def students():
#     return render_template("students.html", student=student_advisors)
#
# # ------------------------------
# # Run App
# # ------------------------------
# if __name__ == "__main__":
#     app.run(debug=True)
# ============================================================
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


# # Faculty Chat API
# @app.route("/facultychat", methods=["POST"])
# def faculty_chat():
#     input_info = request.get_json()
#     question = input_info[2]["Question"]
#     faculty_name = input_info[0]["Professor Name"]
#     subject_name = input_info[1]["Subject Taught"]

#     context = [
#         {
#             "role": "system",
#             "content": f"{faculty_name} is a professor specializing in {subject_name}. "
#                        f"Provide clear and accurate answers to questions related to {subject_name}."
#         },
#         {"role": "user", "content": question}
#     ]

#     response = conversation(context)
#     return jsonify({
#         "faculty_name": faculty_name,
#         "user_message": question,
#         "assistant_response": response
#     })

# @app.route("/alumnichat", methods=["POST"])
# def alumni_chat():
#     input_info = request.get_json()
#     question = input_info[4]["Question"]
#     alumni_name = input_info[0]["Alumni Name"]
#     alumni_department = input_info[1]["Department"]
#     graduation_year = input_info[2]["Graduation Year"]
#     company_working = input_info[3]["Current Position"]

#     context = [
#         {
#             "role": "system",
#             "content": f"{alumni_name} graduated in {graduation_year} from {alumni_department}. "
#                        f"They currently work at {company_working} and can provide insights related to their career path."
#         },
#         {"role": "user", "content": question}
#     ]

#     response = conversation(context)
#     return jsonify({
#         "alumni_name": alumni_name,
#         "user_message": question,
#         "assistant_response": response
#     })

# @app.route("/studentadvisorchat", methods=["POST"])
# def student_advisor_chat():
#     input_info = request.get_json()
#     question = input_info[2]["Question"]
#     advisor_name = input_info[0]["Advisor Name"]
#     career_advisor = input_info[1]["Carrer Advisor"]

#     context = [
#         {
#             "role": "system",
#             "content": f"{advisor_name} is a career advisor specializing in {career_advisor}. "
#                        f"Answer questions related to {career_advisor} with clear and practical advice."
#         },
#         {"role": "user", "content": question}
#     ]

#     response = conversation(context)
#     return jsonify({
#         "advisor_name": advisor_name,
#         "user_message": question,
#         "assistant_response": response
#     })

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
    app.run(debug=True)

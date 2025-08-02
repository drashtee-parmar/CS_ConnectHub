import openai
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenAI API key

# Define the list of faculty members (you can expand this list)
faculty_members = [
    {"name": "Professor Karayakya", "subject": "Machine Learning"},
    {"name": "Professor Shaw", "subject": "Information Retrieval"},
    {"name": "Professor Choi", "subject": "Data Warehousing and Mining"},
    {"name": "Professor Khan", "subject": "Natural Language Processing"},
]
Student_advisor_memebers = [
    {"name": "Carrer Advisor Nurse", "Adviosr": "Resume Building"},
    {"name": "Carrer Advisor Sherif", "Advisor": "Career Advising"},
    {"name": "Carrer Advisor Rodger", "Advisor": "Personality Development"},
]
alumni_members = [
    {"name": "John Smith", "Working at google": "Graduated in 2020"},
    {"name": "Alex hales", "Working at microsfot": "Graduated in 2000"},
    {"name": "Agith Agarkar ", "Working at Facebook": "Graduated in 2004"},
]


app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


# openai.api_key = ""
# openai.api_key = os.getenv("OPENAI_API_KEY")
# if not api_key:
#     print("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
#     exit(1)

def conversation(messages, temperature=0.7):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


@app.route("/facultychat", methods=["POST"])
def Facutly_chat():
    if request.method == "POST":
        print(request.get_json())
        input_info = request.get_json()
        print(type(input_info))
        question = input_info[2]["Question"]
        print("User Question", question)
        print(request.args)
        faculty_name = input_info[0]["Professor Name"]  # Default faculty name
        subject_name = input_info[1]["Subject Taught"]  # Subject taught
        # question = "What is Cosine Similarity Score?"  # Default question

        # Create or load the context for the conversation
        context = [
            {
                "role": "system",
                "content": f"{faculty_name} is teaching the subject of "
                           f"{subject_name}. He should be able to answer queries related to the subject. Please feel free to ask any questions related to "
                           f"{subject_name}.",
            }
        ]

        # Append the user's question to the conversation context
        context.append({"role": "user", "content": question})

        # Get the assistant's response
        response = conversation(context)

        # Append the assistant's response to the context
        context.append({"role": "assistant", "content": response})

        # Print the answer to the console
        print("Assistant's Response:", response)
        print(type(response))
        print("Done")
        # return render_template('faculty.html', faculty_name=faculty_name, user_message=question, assistant_response=response)
        return jsonify(
            {
                "faculty_name": faculty_name,
                "user_message": question,
                "assistant_response": response,
            }
        )


@app.route("/")
def index():
    print("Going for Index.html")
    return render_template("index.html")


@app.route("/faculty")
def faculty():
    print("Accessed the faculty route")
    # return render_template("faculty.html",faculties=faculty_members)
    return render_template("faculty.html", faculty=faculty_members)


@app.route("/alumni")
def alumni():
    print("Accessed the alumni route")
    # Return the alumni HTML template with alumni data
    return render_template("alumni.html", alumni=alumni_members)


@app.route("/alumnichat", methods=["POST"])
def alumni_chat():
    if request.method == "POST":
        input_info = request.get_json()
        question = input_info[4]["Question"]
        alumni_name = input_info[0]["Alumni Name"]
        alumni_department = input_info[1]["Department"]
        graduation_year = input_info[2]["Graduation Year"]
        company_working = input_info[3]["Current Position"]

        context = [
            {
                "role": "system",
                "content": f"{alumni_name} graduated in "
                           f"{graduation_year} from the"
                           f"{alumni_department} department. They are currently working at"
                           f" {company_working}. They can provide insights and advice related to their experience at our university and their work field at"
                           f" {company_working}. Please feel free to ask any questions.",
            }
        ]

        # Append the user's question to the conversation context
        context.append({"role": "user", "content": question})

        # Get the assistant's response using your conversation function
        response = conversation(context)  # You need to define this function

        # Append the assistant's response to the context
        context.append({"role": "assistant", "content": response})

        # Print the answer to the console
        print("Assistant's Response:", response)
        print("Done")

        # Return the response as JSON
        return jsonify(
            {
                "alumni_name": alumni_name,
                "user_message": question,
                "assistant_response": response,
            }
        )


@app.route("/teachingassistat")
def assitant_chat():
    assistant_name = "Teaching Assistant"  # Assistant's name
    question = "Hey, I need some help to understand the topic of web scraping."  # Default question

    # Create or load the context for the conversation
    context = [
        {
            "role": "system",
            "content": f"{assistant_name} is a teaching assistant for Information Retrieval. Students can ask questions about the subject.",
        }
    ]

    # Append the student's question to the conversation context
    context.append({"role": "user", "content": question})

    # Get the assistant's response
    response = conversation(context)

    # Append the assistant's response to the context
    context.append({"role": "assistant", "content": response})

    # Print the answer to the console
    print("Assistant's Response:", response)

    return render_template(
        "assistant_chat.html",
        assistant_name=assistant_name,
        user_message=question,
        assistant_response=response,
    )


@app.route("/students")
def students():
    # Add students-related functionality here
    return render_template("students.html", student=Student_advisor_memebers)


@app.route("/studentadvisorchat", methods=["POST"])
def studet_advisor_chat():
    if request.method == "POST":
        print(request.get_json())
        input_info = request.get_json()
        print(type(input_info))
        question = input_info[2]["Question"]
        print("User Question", question)
        print(request.args)
        advisor_name = input_info[0]["Advisor Name"]
        career_advisor = input_info[1]["Carrer Advisor"]
        # question = "What is Cosine Similarity Score?"  # Default question

        # Create or load the context for the conversation
        context = [
            {
                "role": "system",
                "content": f"{advisor_name} is teaching the subject of "
                           f"{career_advisor}. He should be able to answer queries related to the subject. Please feel free to ask any questions related to "
                           f"{career_advisor}.",
            }
        ]

        # Append the user's question to the conversation context
        context.append({"role": "user", "content": question})

        # Get the assistant's response
        response = conversation(context)

        # Append the assistant's response to the context
        context.append({"role": "assistant", "content": response})

        # Print the answer to the console
        print("Assistant's Response:", response)
        print(type(response))
        print("Done")
        # return render_template('faculty.html', faculty_name=faculty_name, user_message=question, assistant_response=response)
        return jsonify(
            {
                "advisor_name": advisor_name,
                "user_message": question,
                "assistant_response": response,
            }
        )


# faculties = {['Prof. Alan Shaw', 'Information Retrieval', 'ashaw8@kennesaw.edu']}


if __name__ == "__main__":
    app.run(debug=True)

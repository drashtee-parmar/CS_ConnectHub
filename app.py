from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = "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"

# Define the list of faculty members (you can expand this list)
faculty_members = [
    {"name": "Professor Karayakya", "subject": "Machine Learning"},
    {"name": "Professor Shaw", "subject": "Information Retrieval"},
    {"name": "Professor Choi", "subject": "Data Warehousing and Mining"},
    {"name": "Professor Khan", "subject": "Natural Language Processing"},
]
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

def conversation(messages, temperature=0.7):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

@app.route("/facultychat")
def Facutly_chat():
    faculty_name = "Dr. Alan Shaw"  # Default faculty name
    question = "What is Cosine Similarity Score?"  # Default question

    # Create or load the context for the conversation
    context = [{'role': 'system', 'content': f"{faculty_name} is teaching the subject of Information Retrieval. He should be able to answer queries related to the subject. Please feel free to ask any questions related to Information Retrieval."}]

    # Append the user's question to the conversation context
    context.append({'role': 'user', 'content': question})

    # Get the assistant's response
    response = conversation(context)

    # Append the assistant's response to the context
    context.append({'role': 'assistant', 'content': response})

    # Print the answer to the console
    print("Assistant's Response:", response)
    print(type(response))
    print("Done")
    return render_template('faculty.html', faculty_name=faculty_name, user_message=question, assistant_response=response)



@app.route("/")
def index():
    print("Going for Index.html")
    return render_template("index.html")

@app.route("/faculty")
def faculty():
    print("Accessed the faculty route")
    #return render_template("faculty.html",faculties=faculty_members)
    return render_template("faculty.html",faculty=faculty_members)



@app.route("/alumnichat")
def alumni_chat():
    alumnus_name = "Mr. Karthik"  # Alumni name
    question = "What work are you doing, and how can one prepare for it?"  # Default question

    # Create or load the context for the conversation
    context = [{'role': 'system', 'content': f"{alumnus_name} is an alumnus working as a data scientist at Google. Feel free to ask questions about his work and how to prepare for it."}]

    # Append the user's question to the conversation context
    context.append({'role': 'user', 'content': question})

    # Get the assistant's response
    response = conversation(context)

    # Append the assistant's response to the context
    context.append({'role': 'assistant', 'content': response})

    # Print the answer to the console
    print("Assistant's Response:", response)
    print("Done")
    return render_template('alumni_chat.html', alumnus_name=alumnus_name, user_message=question, assistant_response=response)
@app.route("/teachingassistat")
def assitant_chat():
    assistant_name = "Teaching Assistant"  # Assistant's name
    question = "Hey, I need some help to understand the topic of web scraping."  # Default question

    # Create or load the context for the conversation
    context = [{'role': 'system', 'content': f"{assistant_name} is a teaching assistant for Information Retrieval. Students can ask questions about the subject."}]

    # Append the student's question to the conversation context
    context.append({'role': 'user', 'content': question})

    # Get the assistant's response
    response = conversation(context)

    # Append the assistant's response to the context
    context.append({'role': 'assistant', 'content': response})

    # Print the answer to the console
    print("Assistant's Response:", response)

    return render_template('assistant_chat.html', assistant_name=assistant_name, user_message=question, assistant_response=response)

@app.route("/students")
def students():
    # Add students-related functionality here
    return render_template("students.html")

#faculties = {['Prof. Alan Shaw', 'Information Retrieval', 'ashaw8@kennesaw.edu']}


if __name__ == "__main__":
    app.run(debug=True)

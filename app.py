def chatbot_response(u):
    u = u.lower().strip()

    # Greetings
    if u == "hi":
        return "Hello!"
    elif u == "hello":
        return "Hi there!"
    elif u == "hey":
        return "Hey! How can I help you?"
    elif u == "how are you":
        return "I'm doing great! How about you?"

    # About chatbot / project
    elif u == "about you":
        return "I am a student support chatbot developed using Python and Flask."
    elif u == "about this project":
        return "This is a Python Flask chatbot project hosted on the cloud."
    elif u == "is this ai":
        return "No, this is a rule-based chatbot."

    # School information (Montfort CBSE Pondur)
    elif u == "school name":
        return "The school name is Montfort Senior Secondary School, CBSE, Pondur."
    elif u == "where is montfort school located":
        return "Montfort CBSE School is located at Theresapuram, Pondur Post, Sriperumbudur, Kancheepuram District, Tamil Nadu."
    elif u == "which board is montfort school":
        return "Montfort Senior Secondary School is affiliated with CBSE, New Delhi."
    elif u == "cbse affiliation number":
        return "The CBSE affiliation number of Montfort School is 1931064."
    elif u == "when was montfort school established":
        return "Montfort Senior Secondary School was established in the year 2016."
    elif u == "classes offered":
        return "The school offers classes from LKG to Grade XII."
    elif u == "school facilities":
        return "Facilities include science labs, computer lab, library, smart classrooms, playground, and transport."
    elif u == "school timings":
        return "School timing is generally from 8:30 AM to 3:40 PM."
    elif u == "principal of montfort school":
        return "The Principal and Correspondent is Rev. Bro. Sebastian Antony Samy."
    elif u == "school transport":
        return "The school provides transportation facilities with multiple buses."
    elif u == "admission details":
        return "Admissions usually start from LKG, and registration begins around January."
    elif u == "contact details":
        return "Contact numbers are 8754217266 and 9626383244."
    elif u == "school email":
        return "The school email ID is montfortcbsepondur@gmail.com."
    elif u == "school website":
        return "The official website is www.montfortcbsepondur.in."
    elif u == "vision of the school":
        return "The school focuses on academic excellence, character building, and holistic development."

    # Career guidance for students
    elif u == "career guidance":
        return "I provide career guidance for students interested in IT and computer science."
    elif u == "career options after school":
        return "Students can choose engineering, science, commerce, arts, or vocational courses."
    elif u == "how to prepare for future career":
        return "Focus on basics, communication skills, discipline, and continuous learning."
    elif u == "importance of education":
        return "Education builds knowledge, confidence, and career opportunities."

    # Technology knowledge
    elif u == "what is python":
        return "Python is a popular programming language used in web development, AI, and data science."
    elif u == "what is flask":
        return "Flask is a lightweight Python web framework used to build web applications."

    # Polite conversation
    elif u == "thank you":
        return "You're welcome!"
    elif u == "thanks":
        return "Happy to help!"
    elif u == "bye":
        return "Goodbye! Have a great day 😊"

    # Default response
    else:
        return "Sorry, I don't understand that. Please try asking something else."



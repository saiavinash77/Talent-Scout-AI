import streamlit as st
from groq_client import call_llm
from prompts import technical_question_prompt

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🤖")
st.title("🤖 TalentScout Hiring Assistant")

st.write(
    "Welcome to TalentScout! "
    "I will assist you with an initial screening and a short technical interview."
)

# -------------------------------
# Helper Validation Functions
# -------------------------------
def is_valid_email(email):
    return "@" in email and "." in email

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) >= 10

def is_valid_experience(exp):
    return exp.replace(".", "", 1).isdigit()

# -------------------------------
# Session State Initialization
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "stage" not in st.session_state:
    st.session_state.stage = "greeting"

if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current_q" not in st.session_state:
    st.session_state.current_q = 0

# -------------------------------
# Initial Greeting
# -------------------------------
if st.session_state.stage == "greeting":
    bot_response = (
        "Hello 👋 Welcome to TalentScout!\n\n"
        "I’ll collect your details and conduct a short technical screening.\n\n"
        "May I know your **full name**?"
    )
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.session_state.stage = "name"

# -------------------------------
# Display Chat History
# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------
# Chat Input
# -------------------------------
user_input = st.chat_input("Type your response here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # -------------------------------
    # Stage-wise Logic
    # -------------------------------
    if st.session_state.stage == "name":
        st.session_state.candidate_data["name"] = user_input
        bot_response = "Please provide your **email address**."
        st.session_state.stage = "email"

    elif st.session_state.stage == "email":
        if not is_valid_email(user_input):
            bot_response = "❌ Invalid email. Please re-enter a valid email."
        else:
            st.session_state.candidate_data["email"] = user_input
            bot_response = "Please share your **phone number**."
            st.session_state.stage = "phone"

    elif st.session_state.stage == "phone":
        if not is_valid_phone(user_input):
            bot_response = "❌ Invalid phone number. Please enter digits only (min 10)."
        else:
            st.session_state.candidate_data["phone"] = user_input
            bot_response = "How many **years of experience** do you have?"
            st.session_state.stage = "experience"

    elif st.session_state.stage == "experience":
        if not is_valid_experience(user_input):
            bot_response = "❌ Please enter a valid number (example: 1.5)."
        else:
            st.session_state.candidate_data["experience"] = user_input
            bot_response = "What **position** are you applying for?"
            st.session_state.stage = "role"

    elif st.session_state.stage == "role":
        st.session_state.candidate_data["role"] = user_input
        bot_response = "What is your **current location**?"
        st.session_state.stage = "location"

    elif st.session_state.stage == "location":
        st.session_state.candidate_data["location"] = user_input
        bot_response = (
            "Please list your **tech stack** "
            "(languages, frameworks, databases, tools)."
        )
        st.session_state.stage = "tech_stack"

    elif st.session_state.stage == "tech_stack":
        st.session_state.candidate_data["tech_stack"] = user_input
        data = st.session_state.candidate_data

        bot_response = f"""
Please confirm your details:

- **Name:** {data['name']}
- **Email:** {data['email']}
- **Phone:** {data['phone']}
- **Experience:** {data['experience']}
- **Role:** {data['role']}
- **Location:** {data['location']}
- **Tech Stack:** {data['tech_stack']}

Type **confirm** to proceed  
or type **edit field_name** (example: `edit email`)
"""
        st.session_state.stage = "confirm"

    elif st.session_state.stage == "confirm":
        if user_input.lower() == "confirm":
            prompt = technical_question_prompt(
    tech_stack=st.session_state.candidate_data["tech_stack"],
    experience=st.session_state.candidate_data["experience"]
            )

            questions_text = call_llm(
                "You are a professional technical interviewer.",
                prompt
            )
            st.session_state.questions = questions_text.split("\n")
            st.session_state.current_q = 0
            bot_response = "Great! Let’s start the technical interview.\n\n" + \
                           st.session_state.questions[0]
            st.session_state.stage = "interview"

        elif user_input.lower().startswith("edit"):
            field = user_input.lower().replace("edit", "").strip()
            if field in st.session_state.candidate_data:
                st.session_state.stage = f"edit_{field}"
                bot_response = f"Please enter the correct **{field}**."
            else:
                bot_response = "❌ Invalid field name. Try again."

        else:
            bot_response = "Please type **confirm** or **edit field_name**."

    elif st.session_state.stage.startswith("edit_"):
        field = st.session_state.stage.replace("edit_", "")
        st.session_state.candidate_data[field] = user_input
        st.session_state.stage = "confirm"
        bot_response = f"✅ {field} updated. Please confirm details again."

    elif st.session_state.stage == "interview":
        # Light assessment
        assessment = call_llm(
            "You are an interviewer assessing answers briefly.",
            f"Question: {st.session_state.questions[st.session_state.current_q]}\n"
            f"Answer: {user_input}\n"
            "Give short feedback (1 line)."
        )

        st.session_state.current_q += 1

        if st.session_state.current_q < len(st.session_state.questions):
            bot_response = (
                # f"📝 Feedback: {assessment}\n\n"
                f"Next question:\n{st.session_state.questions[st.session_state.current_q]}"
            )
        else:
            bot_response = (
                f"📝 Final feedback: {assessment}\n\n"
                "Thank you! 🙏\n\n"
                "Your interview is complete. Our team will contact you soon."
            )
            st.session_state.stage = "end"

    else:
        bot_response = "Thank you for interacting with TalentScout!"

    # -------------------------------
    # Display Bot Response
    # -------------------------------
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )

    with st.chat_message("assistant"):
        st.markdown(bot_response)

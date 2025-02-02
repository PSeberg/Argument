import streamlit as st

# Lista med fem argumenterande texter
texter = [
    {
        "text": """
        **Tes:** Sverige borde införa en fyra dagars arbetsvecka.  
        En fyra dagars arbetsvecka skulle ge mer tid för familj och fritid, vilket ökar lycka och minskar stress (känsloargument).  
        Studier visar att en fyra dagars arbetsvecka kan öka produktiviteten och minska sjukfrånvaron (sakargument).  
        Vissa kritiker hävdar dock att detta skulle leda till lägre löner och ökad arbetsbelastning (motargument).  
        Som lärare ser jag hur stressade elever och föräldrar är, och jag tror att en extra ledig dag skulle göra stor skillnad (skribentens yrke).
        """,
        "tes": "Sverige borde införa en fyra dagars arbetsvecka.",
        "sakargument": "Studier visar att en fyra dagars arbetsvecka kan öka produktiviteten och minska sjukfrånvaron.",
        "känsloargument": "En fyra dagars arbetsvecka skulle ge mer tid för familj och fritid, vilket ökar lycka och minskar stress.",
        "motargument": "Vissa kritiker hävdar dock att detta skulle leda till lägre löner och ökad arbetsbelastning.",
        "skribentens_yrke": "Som lärare ser jag hur stressade elever och föräldrar är, och jag tror att en extra ledig dag skulle göra stor skillnad."
    },
    {
        "text": """
        **Tes:** Alla borde äta mindre kött för miljöns skull.  
        Att äta mindre kött gör att vi kan rädda djur och känna oss som en del av lösningen på klimatkrisen (känsloargument).  
        Köttproduktion står för en stor del av växthusgasutsläppen, och att minska köttkonsumtionen är effektivt för att bekämpa klimatförändringar (sakargument).  
        Vissa hävdar dock att vegetarisk kost är dyrare och mindre tillgänglig för många (motargument).  
        Som miljöaktivist ser jag hur viktigt det är att vi alla tar ansvar för vår planet (skribentens yrke).
        """,
        "tes": "Alla borde äta mindre kött för miljöns skull.",
        "sakargument": "Köttproduktion står för en stor del av växthusgasutsläppen, och att minska köttkonsumtionen är effektivt för att bekämpa klimatförändringar.",
        "känsloargument": "Att äta mindre kött gör att vi kan rädda djur och känna oss som en del av lösningen på klimatkrisen.",
        "motargument": "Vissa hävdar dock att vegetarisk kost är dyrare och mindre tillgänglig för många.",
        "skribentens_yrke": "Som miljöaktivist ser jag hur viktigt det är att vi alla tar ansvar för vår planet."
    },
    # Lägg till fler texter här...
]

# Initialize session state
if "current_text_index" not in st.session_state:
    st.session_state.current_text_index = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "show_feedback" not in st.session_state:
    st.session_state.show_feedback = False

# Funktion för att visa nästa text
def show_next_text():
    if st.session_state.current_text_index < len(texter):
        text_data = texter[st.session_state.current_text_index]
        st.write(f"### Text {st.session_state.current_text_index + 1}")
        st.write(text_data["text"])
        st.write("Markera följande delar av texten:")
        
        # Input för användarens svar
        st.session_state.user_answers["tes"] = st.text_input("Tes:")
        st.session_state.user_answers["sakargument"] = st.text_input("Sakargument:")
        st.session_state.user_answers["känsloargument"] = st.text_input("Känsloargument:")
        st.session_state.user_answers["motargument"] = st.text_input("Motargument:")
        st.session_state.user_answers["skribentens_yrke"] = st.text_input("Skribentens yrke:")
        
        if st.button("Kontrollera svar"):
            check_answers(text_data)
    else:
        st.write("Du har gått igenom alla texter!")
        if st.button("Börja om"):
            st.session_state.current_text_index = 0
            st.session_state.user_answers = {}
            st.session_state.show_feedback = False
            st.rerun()

# Funktion för att kontrollera svaren
def check_answers(text_data):
    st.session_state.show_feedback = True
    correct_answers = {
        "tes": text_data["tes"],
        "sakargument": text_data["sakargument"],
        "känsloargument": text_data["känsloargument"],
        "motargument": text_data["motargument"],
        "skribentens_yrke": text_data["skribentens_yrke"]
    }
    st.write("### Feedback:")
    for key, value in st.session_state.user_answers.items():
        if value.strip() == correct_answers[key].strip():
            st.success(f"{key.capitalize()}: Rätt!")
        else:
            st.error(f"{key.capitalize()}: Fel. Rätt svar var: {correct_answers[key]}")

# Streamlit app layout
st.title("Argumenterande Texter")
st.write("Läs texten och markera tes, sakargument, känsloargument, motargument och skribentens yrke.")

if st.session_state.current_text_index < len(texter):
    show_next_text()
    if st.session_state.show_feedback:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Fortsätt till nästa text"):
                st.session_state.current_text_index += 1
                st.session_state.user_answers = {}
                st.session_state.show_feedback = False
                st.rerun()
        with col2:
            if st.button("Gör om samma text"):
                st.session_state.user_answers = {}
                st.session_state.show_feedback = False
                st.rerun()
else:
    show_next_text()

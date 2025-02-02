import streamlit as st

# Example text and answers
texts = [
    {
        "title": "Text 1",
        "content": """Här är en argumenterande text där författaren diskuterar fördelarna med att använda mobiltelefoner i skolan. Tes: Mobiltelefoner är användbara i skolan för att underlätta lärandet. Sakargument: De gör det lättare att få information snabbt. Känsloargument: Det känns bra att kunna kommunicera med föräldrar och vänner även under lektionerna. Motargument: Mobiltelefoner kan vara distraherande. Skribentens yrke: En lärare nämns i slutet av texten.""",
        "answers": {
            "tes": "Mobiltelefoner är användbara i skolan för att underlätta lärandet.",
            "sakargument": "De gör det lättare att få information snabbt.",
            "känsloargument": "Det känns bra att kunna kommunicera med föräldrar och vänner.",
            "motargument": "Mobiltelefoner kan vara distraherande.",
            "yrke": "En lärare nämns i slutet av texten."
        }
    },
]

# Function to display the interactive text and choices
def display_text_and_choices():
    st.title(texts[0]["title"])
    st.write(texts[0]["content"])

    # Display multiple choice options for each argument part
    selected_tes = st.radio("Välj tes:", 
                            options=["Mobiltelefoner är användbara i skolan för att underlätta lärandet.",
                                     "Mobiltelefoner är distraherande i skolan.",
                                     "Mobiltelefoner har inget att göra med skolan."])
    
    selected_sakargument = st.radio("Välj sakargument:",
                                     options=["De gör det lättare att få information snabbt.",
                                              "Mobiltelefoner förstör lärandet.",
                                              "De hindrar elever från att fokusera på lektionerna."])
    
    selected_känsloargument = st.radio("Välj känsloargument:",
                                       options=["Det känns bra att kunna kommunicera med föräldrar och vänner.",
                                                "Det är inte bra att använda mobilen på lektioner.",
                                                "Det skapar oro att inte ha en mobiltelefon."])

    selected_motargument = st.radio("Välj motargument:",
                                    options=["Mobiltelefoner kan vara distraherande.",
                                             "Mobiltelefoner underlättar kommunikationen mellan elever.",
                                             "Mobiltelefoner ökar koncentrationen på lektioner."])

    selected_yrke = st.radio("Välj yrke:",
                             options=["En lärare nämns i slutet av texten.",
                                      "En student nämns i slutet av texten.",
                                      "En politiker nämns i slutet av texten."])

    # Button to check answers
    if st.button("Kontrollera svar"):
        # Checking if the answers match the correct ones
        feedback = []

        feedback.append(f"Tes: {'Correct' if selected_tes == texts[0]['answers']['tes'] else 'Incorrect'}")
        feedback.append(f"Sakargument: {'Correct' if selected_sakargument == texts[0]['answers']['sakargument'] else 'Incorrect'}")
        feedback.append(f"Känsloargument: {'Correct' if selected_känsloargument == texts[0]['answers']['känsloargument'] else 'Incorrect'}")
        feedback.append(f"Motargument: {'Correct' if selected_motargument == texts[0]['answers']['motargument'] else 'Incorrect'}")
        feedback.append(f"Yrke: {'Correct' if selected_yrke == texts[0]['answers']['yrke'] else 'Incorrect'}")

        # Display feedback
        for item in feedback:
            st.write(item)

        # Option to continue or restart
        st.write("Vill du fortsätta eller göra om samma text?")
        next_text = st.button("Nästa text")
        retry_text = st.button("Gör om text")

        if next_text:
            st.write("Nästa text kommer snart...")
            # Logic to go to next text can be added here
        if retry_text:
            st.write("Försök igen!")
            # You can reset the choices if needed

# Display the text and choices
if __name__ == "__main__":
    display_text_and_choices()

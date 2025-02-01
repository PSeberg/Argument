import streamlit as st
import random

# Lista med 10 teser, känsloargument och sakargument
teser = [
    {
        "tes": "Sverige borde införa en fyra dagars arbetsvecka.",
        "känsloargument": "En fyra dagars arbetsvecka skulle ge mer tid för familj och fritid, vilket ökar lycka och minskar stress.",
        "sakargument": "Studier visar att en fyra dagars arbetsvecka kan öka produktiviteten och minska sjukfrånvaron."
    },
    {
        "tes": "Alla borde äta mindre kött för miljöns skull.",
        "känsloargument": "Att äta mindre kött gör att vi kan rädda djur och känna oss som en del av lösningen på klimatkrisen.",
        "sakargument": "Köttproduktion står för en stor del av växthusgasutsläppen, och att minska köttkonsumtionen är effektivt för att bekämpa klimatförändringar."
    },
    {
        "tes": "Skolan borde börja senare på morgonen.",
        "känsloargument": "Elever skulle vara gladare och mindre stressade om de fick sova längre på morgnarna.",
        "sakargument": "Forskning visar att ungdomar har en annan dygnsrytm och att senare skolstart kan förbättra koncentration och prestation."
    },
    {
        "tes": "Alla borde använda kollektivtrafik istället för bil.",
        "känsloargument": "Att åka kollektivtrafik ger en känsla av gemenskap och bidrar till en renare miljö för framtida generationer.",
        "sakargument": "Kollektivtrafik minskar trafikstockningar och utsläpp av växthusgaser jämfört med bilåkande."
    },
    {
        "tes": "Sverige borde satsa mer på kärnkraft.",
        "känsloargument": "Kärnkraft ger oss en känsla av säkerhet och stabilitet i energiförsörjningen.",
        "sakargument": "Kärnkraft är en effektiv och pålitlig energikälla som producerar låga mängder växthusgaser."
    },
    {
        "tes": "Sociala medier borde regleras hårdare.",
        "känsloargument": "Sociala medier skapar ångest och ensamhet hos många unga, och det känns viktigt att skydda dem.",
        "sakargument": "Reglering av sociala medier kan minska spridningen av falsk information och skydda användarnas integritet."
    },
    {
        "tes": "Alla borde ha rätt att arbeta hemifrån.",
        "känsloargument": "Att arbeta hemifrån ger en känsla av frihet och balans mellan arbete och privatliv.",
        "sakargument": "Hemarbete minskar pendlingstid och kan öka produktiviteten genom att anpassa arbetsmiljön efter individens behov."
    },
    {
        "tes": "Plastpåsar borde förbjudas.",
        "känsloargument": "Att förbjuda plastpåsar gör att vi kan känna stolthet över att skydda hav och djur från plastavfall.",
        "sakargument": "Plastpåsar tar hundratals år att bryta ner och är en stor källa till miljöföroreningar."
    },
    {
        "tes": "Universell basinkomst borde införas.",
        "känsloargument": "Basinkomst ger människor hopp och möjlighet att leva ett värdigt liv utan ekonomisk stress.",
        "sakargument": "Basinkomst kan minska byråkrati och ge människor större ekonomisk trygghet, vilket gynnar samhällsekonomin."
    },
    {
        "tes": "Djur borde inte hållas i fångenskap i djurparker.",
        "känsloargument": "Att se djur i burar gör oss ledsna och får oss att undra om vi verkligen behandlar dem med respekt.",
        "sakargument": "Djur i fångenskap lider ofta av stress och hälsoproblem på grund av begränsat utrymme och onaturliga miljöer."
    }
]

# Initialize session state
if "current_tes_index" not in st.session_state:
    st.session_state.current_tes_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "correct_answer" not in st.session_state:
    st.session_state.correct_answer = None

# Function to show the next tes
def show_next_tes():
    if st.session_state.current_tes_index < len(teser):
        tes = teser[st.session_state.current_tes_index]
        st.write(f"### Tes: {tes['tes']}")
        argument_type = random.choice(["känsloargument", "sakargument"])
        st.write(f"**Argument:** {tes[argument_type]}")
        st.session_state.correct_answer = argument_type
    else:
        st.write(f"### Du fick {st.session_state.score} av {len(teser)} rätt!")
        if st.button("Börja om"):
            st.session_state.current_tes_index = 0
            st.session_state.score = 0
            st.session_state.correct_answer = None
            st.experimental_rerun()

# Function to handle user's answer
def handle_answer(user_answer):
    if user_answer == st.session_state.correct_answer:
        st.session_state.score += 1
        st.success("Rätt!")
    else:
        st.error("Fel.")
    st.session_state.current_tes_index += 1
    if st.session_state.current_tes_index < len(teser):
        st.experimental_rerun()

# Streamlit app layout
st.title("Argumenttest")
st.write("Välj om argumentet är ett känsloargument eller ett sakargument.")

if st.session_state.current_tes_index < len(teser):
    show_next_tes()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Känsloargument"):
            handle_answer("känsloargument")
    with col2:
        if st.button("Sakargument"):
            handle_answer("sakargument")
else:
    show_next_tes()

import streamlit as st

st.set_page_config(page_title="🎄 Weihnachtsfeier Adventure", page_icon="🎁")

st.title("🎄 Das große Weihnachtsfeier-Adventure")
st.markdown("""
Du bist Eventmanager:in und planst die interne Weihnachtsfeier. 
Alles scheint perfekt vorbereitet – bis du kurz vor Beginn in der Location eintriffst. 

🚨 **Vor Ort stellst du fest, dass der Caterer nicht da ist.** Was tust du jetzt?
""")

# Session State zum Speichern des Spielstands
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.choice1 = ""
    st.session_state.choice2 = ""

# --- Entscheidungspunkt 1 ---
if st.session_state.step == 0:
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("a) Ganz klar, ich bewahre erst einmal Ruhe und kümmere mich um andere Dinge. Er wird bestimmt noch auftauchen."):
            st.session_state.choice1 = "a"
            st.session_state.step = 1
    with col2:
        if st.button("b) Das läuft ganz klar etwas schief. Ich rufe ihn sofort an."):
            st.session_state.choice1 = "b"
            st.session_state.step = 1
    with col3:
        if st.button("c) Ich verschwende keine Zeit und suche direkt nach möglichen Alternativen. Vorbereitung ist alles."):
            st.session_state.choice1 = "c"
            st.session_state.step = 1

# --- Entscheidungspunkt 2 ---
if st.session_state.step == 1:
    choice1 = st.session_state.choice1
    st.markdown("---")
    if choice1 == "a":
        st.markdown("30 Minuten später – der Caterer ist immer noch nicht da. Was tust du jetzt?")
        opts = [
            "1. Okay, das ist nicht so gut. Dann suche ich jetzt doch noch schnell nach einer Alternative. Hoffentlich finde ich noch etwas.",
            "2. Ich schiebe die Schuld auf die Praktikantin, immerhin sollte sie sich eigentlich um das Thema kümmern.",
            "3. Jetzt ist das ganze Team gefragt - ich rufe alle zusammen um gemeinsam einen Notfallplan auszuarbeiten."
        ]
    elif choice1 == "b":
        st.markdown("Der Caterer meldet sich – leider gab es wohl ein Missverständnis hinsichtlich des Termins. Fakt ist: Er kommt nicht. Wie reagierst du?")
        opts = [
            "1. Ich schicke eine Pizza-Party-Mail an alle Kontakte und hoffe, dass irgendwer sich meldet.",
            "2. Den nächstbesten Lieferservice anrufen, der muss es jetzt richten – koste es, was es wolle.",
            "3. Ich schiebe das Event um 1 Stunde nach hinten um erst mal ein bisschen mehr Zeit zu gewinnen."
        ]
    elif choice1 == "c":
        st.markdown("Du hast es geschafft und einen Pizzaservice organisiert – Ankunft in 90 Minuten. Was machst du bis dahin?")
        opts = [
            "1. Ich starte ein paar spontane Icebreaker-Spiele, um die Zeit zu überbrücken.",
            "2. Ob das wirklich gutgeht? Ich kümmere mich darum, zur Sicherheit auch noch ein kaltes Supermarkt-Buffet zu improvisieren.",
            "3. Ich gebe dem DJ das Signal schon mal zu starten. Mit Musik ist einfach alles besser."
        ]

    for i, opt in enumerate(opts):
        if st.button(opt):
            st.session_state.choice2 = str(i + 1)
            st.session_state.step = 2

# --- Ende ---
if st.session_state.step == 2:
    st.markdown("---")
    c1 = st.session_state.choice1
    c2 = st.session_state.choice2
    st.subheader("🎬 Ausgang deiner Weihnachtsfeier:")

    if (c1 == "c" and c2 in ["1", "3"]) or (c1 == "b" and c2 == "1") or (c1 == "a" and c2 == "3"):
        st.success("🎉 Die Feier war ein voller Erfolg – anders als geplant, aber unvergesslich!")
    elif (c1 == "a" and c2 == "1") or (c1 == "b" and c2 == "2") or (c1 == "c" and c2 == "2"):
        st.warning("🥴 Du hast es irgendwie gerettet – aber ganz ohne Chaos ging’s nicht ab.")
    else:
        st.error("😬 Leider gescheitert – fehlendes Essen, Schuldzuweisungen und leere Mägen. Versuch’s nochmal!")

    if st.button("🔄 Nochmal spielen"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

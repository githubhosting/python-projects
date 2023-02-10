import streamlit as st
import time

st.title("WELCOME TO MY FRONT PAGE")
st.header("-Made By Siddharth Rao")
time.sleep(1)
st.subheader("Here are some really good books and if u have read them.....Rate them !!")
st.write("Before we begin..... solve my captcha")
time.sleep(1)
st.text_input("Which number is prime but even?", key='ans')
sol = st.session_state.ans
if sol == '2':
    st.write("GR8...u r not a bot ")
    st.write("Alright let us begin !")
    st.subheader("So all u have to do is rate the books given below (Thas it!!)")

    col1, col2 = st.columns([3, 1], gap="large")

    with col1:
        st.title("𝘛𝘩𝘦 𝘋𝘢 𝘝𝘪𝘯𝘤𝘪 𝘊𝘰𝘥𝘦")
        st.header("-Dan Brown")
        st.write("Genre : Mystery ,Crime ,Fiction Thriller")
        st.write(
            "'While in Paris on business, Harvard symbologist Robert Langdon receives an urgent late-night phone "
            "call: the elderly curator of the Louvre has been murdered inside the museum. Near the body, police have "
            "found a baffling cipher. Solving the enigmatic riddle, Langdon is stunned to discover it leads to a "
            "trail of clues hidden in the works of da Vinci…clues visible for all to see…and yet ingeniously "
            "disguised by the painter.' ")
        st.slider("Rate this book :", 0, 10, key='one')
        rate1 = st.session_state.one
    with col2:
        st.image(
            "https://user-images.githubusercontent.com/88105873/202715815-1076f957-d529-4476-be96-78cfa994a1f0.jpg")

    col1, col2 = st.columns([3, 1], gap="large")

    with col1:
        st.title("12 𝘙𝘶𝘭𝘦𝘴 𝘍𝘰𝘳 𝘓𝘪𝘧𝘦")
        st.subheader("-Jordan Peterson")
        st.write("Genre : Psychology ,Self-help")
        st.write(
            "'12 Rules For Life is a stern, story-based, and entertaining self-help manual for young people that lays "
            "out a set of simple principles that can help us become more disciplined, behave better, "
            "act with integrity, and balance our lives while enjoying them as much as we can.' ")
        st.slider("Rate this book :", 0, 10, key='two')
        rate2 = st.session_state.two
    with col2:
        st.image(
            "https://user-images.githubusercontent.com/88105873/202716768-8d02e232-445d-47a1-9c5b-342ce052d80a.jpg")

    col1, col2 = st.columns([3, 1], gap="large")

    with col1:
        st.title("𝘛𝘩𝘦 𝘚𝘩𝘦𝘳𝘭𝘰𝘤𝘬 𝘏𝘰𝘭𝘮𝘦𝘴")
        st.subheader("-Sir Conan Doyle")
        st.write("Genre : Mystery Crime Fiction ")
        st.write(
            "'Referring to himself as a 'Consulting detective' in the stories, Holmes is known for his proficiency "
            "with observation, deduction, forensic science and logical reasoning that borders on the fantastic, "
            "which he employs when investigating cases for a wide variety of clients, including Scotland Yard.' ")
        st.slider("Rate this book :", 0, 10, key='three')
        rate3 = st.session_state.three
    with col2:
        st.image(
            "https://user-images.githubusercontent.com/88105873/202718812-d15f078f-f181-407e-ae46-f4c261912927.jpg")

    col1, col2 = st.columns([3, 1], gap="large")

    with col1:
        st.title("𝘎𝘢𝘮𝘦 𝘰𝘧 𝘛𝘩𝘳𝘰𝘯𝘦𝘴")
        st.subheader("-George R. R. Martin")
        st.write("Genre : High Fantasy ,Fantasy Fiction ,Political Fiction")
        st.write(
            "'While in Paris on business, Harvard symbologist Robert Langdon receives an urgent late-night phone "
            "call: the elderly curator of the Louvre has been murdered inside the museum. Near the body, police have "
            "found a baffling cipher. Solving the enigmatic riddle, Langdon is stunned to discover it leads to a "
            "trail of clues hidden in the works of da Vinci…clues visible for all to see…and yet ingeniously "
            "disguised by the painter.' ")
        st.slider("Rate this book :", 0, 10, key='four')
        rate4 = st.session_state.four
    with col2:
        st.image(
            "https://user-images.githubusercontent.com/88105873/202735040-93f02e0e-8490-4758-bf37-1eba1d014bf1.jpg")

    col1, col2 = st.columns([3, 1], gap="large")

    with col1:
        st.title("𝘐 𝘢𝘮 𝘓𝘦𝘨𝘦𝘯𝘥")
        st.subheader("-Richard Matheson")
        st.write("Genre : Horror ,Fiction ,Vampires")
        st.write(
            "'Robert Neville is the last living man on Earth... but he is not alone. Every other man, woman and child "
            "on the planet has become a vampire, and they are hungry for Neville's blood.By day he is the hunter, "
            "stalking the undead through the ruins of civilisation. By night, he barricades himself in his home and "
            "prays for the dawn.' ")
        st.slider("Rate this book :", 0, 10, key='five')
        rate5 = st.session_state.five
    with col2:
        st.image(
            "https://user-images.githubusercontent.com/88105873/202736371-6a7880ef-c78b-478c-8b37-70b60903531d.jpg")

    with st.sidebar:
        st.header("Enter ur info plz")
        st.text_input("Name ", max_chars=20, key='info1')
        st.text_input("email id ", max_chars=50, key='info2')
        st.text_input("age ", max_chars=3, key='info3')
        name = st.session_state.info1
        email = st.session_state.info2
        age = st.session_state.info3

    st.button("After u enter the details ,hit me!!!", key='op')
    if st.session_state.op:
        st.write("Here is a mini reader id we made ... happy reading!")
        st.header('Name :' + name)
        st.subheader('email id :' + email)
        st.subheader('Age :' + age)
        review = {
            "𝘛𝘩𝘦 𝘋𝘢 𝘝𝘪𝘯𝘤𝘪 𝘊𝘰𝘥𝘦": rate1,
            "12 𝘙𝘶𝘭𝘦𝘴 𝘍𝘰𝘳 𝘓𝘪𝘧𝘦": rate2,
            "𝘛𝘩𝘦 𝘚𝘩𝘦𝘳𝘭𝘰𝘤𝘬 𝘏𝘰𝘭𝘮𝘦𝘴": rate3,
            "𝘎𝘢𝘮𝘦 𝘰𝘧 𝘛𝘩𝘳𝘰𝘯𝘦𝘴": rate4,
            "𝘐 𝘢𝘮 𝘓𝘦𝘨𝘦𝘯𝘥": rate5
        }
        for i in review:
            st.write(i + '|------> \t' + str(review[i]) + ' sid points\n')
        st.balloons()
else:
    st.error("Kindly contact ur admin ", icon="🤖")
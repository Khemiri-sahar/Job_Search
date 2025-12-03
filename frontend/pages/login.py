import streamlit as st

def login_page():
    st.title("Connexion")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        if username == "admin" and password == "1234":  
            st.session_state['logged_in'] = True
            st.success("Connecté !")
            st.rerun()
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")

    elif st.button("Connexion en tant qu'invité"):
            st.session_state['logged_in'] = True
            st.session_state['username'] = "Invité"
            st.success("Connexion en tant qu'invité")
            st.rerun() 
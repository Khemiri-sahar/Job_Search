import streamlit as st
import time

def search_page():
    st.title("Chercher des offres d'emploi")

    if st.button("Se déconnecter"):
        st.session_state['logged_in'] = False
        st.rerun()


    st.write("Dites nous ce que vous cherchez ..." )
    
    query = st.text_input("Votre recherche")
    num_results = st.number_input("Nombre de résultats", min_value=1, max_value=50, value=5)
    
    if st.button("🔎 Chercher des annonces"):
        if query.strip():
            with st.spinner("🔄 Recherche en cours..."):
                time.sleep(1)  
                
                # MOCK DATA 
                job_offers = [
                    {
                        "title": "Développeur Python Senior",
                        "company": "TechCorp",
                        "sector": "Technologie",
                        "salary": "80000-120000"
                    },
                    {
                        "title": "Ingénieur Machine Learning",
                        "company": "AI Solutions",
                        "sector": "Intelligence Artificielle",
                        "salary": "90000-130000"
                    },
                    {
                        "title": "Data Scientist",
                        "company": "DataCo",
                        "sector": "Analytique",
                        "salary": "75000-110000"
                    },
                    {
                        "title": "Développeur Full Stack",
                        "company": "WebDev Ltd",
                        "sector": "Développement Web",
                        "salary": "70000-100000"
                    },
                    {
                        "title": "Ingénieur DevOps",
                        "company": "CloudTech",
                        "sector": "Cloud Computing",
                        "salary": "85000-115000"
                    }
                ]
                
                job_offers = job_offers[:num_results]
                
                if job_offers:
                    st.success(f" {len(job_offers)} offres trouvées!")
                    st.subheader("Résultats de recherche:")
                    
                    for i, job in enumerate(job_offers, 1):
                        with st.container():
                            col1, col2 = st.columns([3, 1])
                            
                            with col1:
                                st.markdown(f"### {i}. {job.get('title', 'N/A')}")
                                st.write(f"**Entreprise:** {job.get('company', 'N/A')}")
                                st.write(f"**Secteur:** {job.get('sector', 'N/A')}")
                            
                            with col2:
                                st.metric("Salaire", job.get('salary', 'N/A'))
                            
                            st.divider()
                else:
                    st.info("Aucune offre trouvée")
        else:
            st.warning("Veuillez entrer une recherche")
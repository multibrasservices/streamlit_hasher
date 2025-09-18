import streamlit as st
import bcrypt
import base64
from pathlib import Path

st.set_page_config(page_title="Générateur de Hash", layout="centered")

# --- VERSION CORRIGÉE ---
# Cette fonction trouve le chemin du script actuel et construit un chemin
# complet et fiable vers l'image.
def img_to_bytes(img_path):
    try:
        # Construit le chemin absolu à partir de l'emplacement du script
        script_dir = Path(__file__).resolve().parent
        full_path = script_dir / img_path
        
        img_bytes = full_path.read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded
    except FileNotFoundError:
        # Au cas où le fichier ne serait vraiment pas trouvé, on évite que l'app plante.
        st.error(f"L'image du logo '{img_path}' est introuvable. Assurez-vous qu'elle est sur GitHub.")
        return ""


st.title("🔑 Générateur de Hash de Mot de Passe")

st.write("""
Utilisez cet outil pour générer un hash sécurisé pour un mot de passe. 
Le hash généré utilise l'''algorithme **bcrypt**, qui est la norme recommandée 
pour le stockage de mots de passe.
""")
st.info("Entrez un mot de passe ci-dessous, puis cliquez sur le bouton pour obtenir le hash correspondant.", icon="ℹ️")


# Champ de saisie pour le mot de passe
password_to_hash = st.text_input("Mot de passe à hacher", type="password")

# Bouton pour lancer le hachage
if st.button("Hacher le mot de passe"):
    if password_to_hash:
        try:
            password_bytes = password_to_hash.encode('utf-8')
            hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            hashed_password_str = hashed_password.decode('utf-8')

            st.success("Voici votre mot de passe haché :")
            st.code(hashed_password_str, language="text")

            st.warning("""
            **Important :** Copiez ce hash et collez-le dans votre fichier de configuration 
            (par exemple, le fichier YAML pour `streamlit-authenticator`). 
            Ne stockez jamais les mots de passe en clair !
            """, icon="⚠️")

        except Exception as e:
            st.error(f"Une erreur est survenue lors du hachage : {e}")
    else:
        st.error("Veuillez entrer un mot de passe avant de cliquer sur le bouton.")

# --- CORRECTION DE L'APPEL ---
# On passe maintenant juste le nom du fichier, car la fonction s'occupe du chemin.
logo_base64 = img_to_bytes("mon_logo.png")
if logo_base64: # On n'affiche le logo que si l'image a été trouvée
    st.sidebar.markdown(f'''
    <a href="https://zoomali.io/" target="_blank">
        <img src="data:image/png;base64,{logo_base64}" width="100">
    </a>
    ''', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("version 18.09.25")
st.sidebar.markdown("© [multibraservices@gmail.com](https://zoomali.io/)")
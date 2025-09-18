import streamlit as st
import bcrypt

st.set_page_config(page_title="Générateur de Hash", layout="centered")

st.title("🔑 Générateur de Hash de Mot de Passe")

st.write("""
Utilisez cet outil pour générer un hash sécurisé pour un mot de passe. 
Le hash généré utilise l'algorithme **bcrypt**, qui est la norme recommandée 
pour le stockage de mots de passe.
""")
st.info("Entrez un mot de passe ci-dessous, puis cliquez sur le bouton pour obtenir le hash correspondant.", icon="ℹ️")


# Champ de saisie pour le mot de passe
# L'attribut type="password" permet de masquer la saisie
password_to_hash = st.text_input("Mot de passe à hacher", type="password")

# Bouton pour lancer le hachage
if st.button("Hacher le mot de passe"):
    if password_to_hash:
        try:
            # Bcrypt attend des bytes, donc on encode le mot de passe en UTF-8
            password_bytes = password_to_hash.encode('utf-8')

            # Génération du "sel" (salt) et hachage du mot de passe
            hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            
            # On décode le hash en string pour pouvoir l'afficher et le copier
            hashed_password_str = hashed_password.decode('utf-8')

            st.success("Voici votre mot de passe haché :")
            
            # st.code permet d'afficher le hash dans un bloc formaté, facile à copier
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
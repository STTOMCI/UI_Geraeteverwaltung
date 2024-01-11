import streamlit as st
from streamlit_option_menu import option_menu
import roman

# -------------- SETTINGS --------------
page_title = "Geräteverwaltung"
page_icon = ":books:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Geräte verwalten", "Geräte resvieren", "Geräte anzeigen"],
    icons=["pencil-fill", "clock-history", "bar-chart-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)

# --- MANAGE DEVICES ---
if selected == "Geräte verwalten":

    manage_selected = option_menu(
        menu_title=None,
        options=["Geräte hinzufügen", "Geräte bearbeiten", "Geräte entfernen"],
        icons=["plus-square", "wrench", "dash-square"],  # https://icons.getbootstrap.com/
        orientation="horizontal",
    )

    # --- ADD DEVICES ---
    if manage_selected == "Geräte hinzufügen":
        st.header(f"Anlegen eines neuem Gerät")
        with st.form("entry_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            col1.selectbox("MCI:", list(map(roman.toRoman,range(1,7))), key="mci")
            tool_types = ["Office", "EDV", "Labore", "Diverses"]
            col2.selectbox("Geräte Art:", tool_types, key="type")
            st.text_input("Gerätename:", max_chars=64, placeholder="Gerätename hier einfügen ...", key="name")

            "---"

            with st.expander("Geräteeigenschaften"):
                st.number_input("Preis:", min_value=0, format="%i", step=10, key="cost")
                st.selectbox("Verantwortlicher:", ["Person A", "Person B"], key="person")
                st.radio("Beweglichkeit:", ["Feststehend", "Beweglich"], horizontal=True, key="mobility")
            with st.expander("Wartung und Reservierung"):
                st.radio(
                    "Wartungsabstände:",
                    options=["keine Wartung notwendig", "täglich", "wöchentlich", "monatlich", "jährlich"],
                    key="intervals")
                st.number_input("Kosten pro Wartung:", min_value=0, format="%i", step=1, key="maintenancecost")
                st.radio("Resavierbarkeit:", ["Resavierbar", "Nicht resavierbar"], horizontal=True, key="resavable")
            with st.expander("Kommentar"):
                comment = st.text_area("", placeholder="Kommentar hier einfügen ...")

            "---"

            submitted = st.form_submit_button("Neues Gerät anlegen")
            if submitted:
                st.success("Neues Gerät erfolgreich anlegen!")

    # --- MANAGE DEVICE ---
                
    if manage_selected == "Geräte bearbeiten":
            st.header(f"Geräte bearbeiten")
            current_device_example = st.selectbox(
                'Gerät auswählen',
                options = ["Gerät_A", "Gerät_B"], key="sbDevice_example")

    # --- REMOVE DEVICES ---


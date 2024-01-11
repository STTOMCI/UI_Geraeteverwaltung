import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_calendar import calendar
import roman

# -------------- SETTINGS --------------
page_title = "Geräteverwaltung"
page_icon = ":books:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"

events = [
    {
        "title": "Event 1",
        "color": "#FF6C6C",
        "start": "2023-07-03",
        "end": "2023-07-05",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "color": "#FFBD45",
        "start": "2023-07-01",
        "end": "2023-07-10",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "color": "#FF4B4B",
        "start": "2023-07-20",
        "end": "2023-07-20",
        "resourceId": "c",
    },
    {
        "title": "Event 4",
        "color": "#FF6C6C",
        "start": "2023-07-23",
        "end": "2023-07-25",
        "resourceId": "d",
    },
    {
        "title": "Event 5",
        "color": "#FFBD45",
        "start": "2023-07-29",
        "end": "2023-07-30",
        "resourceId": "e",
    },
    {
        "title": "Event 6",
        "color": "#FF4B4B",
        "start": "2023-07-28",
        "end": "2023-07-20",
        "resourceId": "f",
    },
    {
        "title": "Event 7",
        "color": "#FF4B4B",
        "start": "2023-07-01T08:30:00",
        "end": "2023-07-01T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 8",
        "color": "#3D9DF3",
        "start": "2023-07-01T07:30:00",
        "end": "2023-07-01T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 9",
        "color": "#3DD56D",
        "start": "2023-07-02T10:40:00",
        "end": "2023-07-02T12:30:00",
        "resourceId": "c",
    },
    {
        "title": "Event 10",
        "color": "#FF4B4B",
        "start": "2023-07-15T08:30:00",
        "end": "2023-07-15T10:30:00",
        "resourceId": "d",
    },
    {
        "title": "Event 11",
        "color": "#3DD56D",
        "start": "2023-07-15T07:30:00",
        "end": "2023-07-15T10:30:00",
        "resourceId": "e",
    },
    {
        "title": "Event 12",
        "color": "#3D9DF3",
        "start": "2023-07-21T10:40:00",
        "end": "2023-07-21T12:30:00",
        "resourceId": "f",
    },
    {
        "title": "Event 13",
        "color": "#FF4B4B",
        "start": "2023-07-17T08:30:00",
        "end": "2023-07-17T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 14",
        "color": "#3D9DF3",
        "start": "2023-07-17T09:30:00",
        "end": "2023-07-17T11:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 15",
        "color": "#3DD56D",
        "start": "2023-07-17T10:30:00",
        "end": "2023-07-17T12:30:00",
        "resourceId": "c",
    },
    {
        "title": "Event 16",
        "color": "#FF6C6C",
        "start": "2023-07-17T13:30:00",
        "end": "2023-07-17T14:30:00",
        "resourceId": "d",
    },
    {
        "title": "Event 17",
        "color": "#FFBD45",
        "start": "2023-07-17T15:30:00",
        "end": "2023-07-17T16:30:00",
        "resourceId": "e",
    },
]
calendar_resources = [
    {"id": "a", "building": "Building A", "title": "Room A"},
    {"id": "b", "building": "Building A", "title": "Room B"},
    {"id": "c", "building": "Building B", "title": "Room C"},
    {"id": "d", "building": "Building B", "title": "Room D"},
    {"id": "e", "building": "Building C", "title": "Room E"},
    {"id": "f", "building": "Building C", "title": "Room F"},
]
calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "resources": calendar_resources,
    "selectable": "true",
}

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

# --- RESERVE DEVICES ---
            
# --- SHOW DEVICES ---
if selected == "Geräte anzeigen":

    show_selected = option_menu(
        menu_title=None,
        options=["Geräte Anzeigen", "Wartungen Anzeigen"],
        icons=["search", "tools"],  # https://icons.getbootstrap.com/
        orientation="horizontal",
    )

    # --- SHOW DEVICE ---
    if show_selected == "Geräte Anzeigen":
        st.header(f"Geräteanzeige")
        current_device = st.selectbox(
                'Gerät auswählen',
                options = ["Gerät_A", "Gerät_B"], key="sbDevice_example")
        calendar_options = {
            **calendar_options,
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
            },
            "initialDate": "2023-07-01",
            "initialView": "resourceTimelineDay",
            "resourceGroupField": "building",
        }

    # --- SHOW MAINTENANCE ---
    if show_selected == "Wartungen Anzeigen":
        st.header(f"Gerätewartungen")
        calendar_options = {
            **calendar_options,
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "timelineDay,timelineWeek,timelineMonth",
            },
            "initialDate": "2023-07-01",
            "initialView": "timelineMonth",
        }

    state = calendar(
        events=st.session_state.get("events", events),
        options=calendar_options,
        custom_css="""
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
        """,
        key=show_selected,
    )

    if state.get("eventsSet") is not None:
        st.session_state["events"] = state["eventsSet"]

import streamlit as st
import math

pg_bg_img = f"""
<style>
[data-testid="stApp"] {{
background-image: url("https://i.imgur.com/6NwtL8l.png");
background-size: cover;
background-repeat: no-repeat;
background-attachment: local;
background-position: top left;
}}
[data-testid="stHeader"]{{
background-color: rgba(0,0,0,0);
}}

[data-testid="stSidebar"]{{
background-color: rgba(255,255,243,0.50);
}}
</style>
"""

st.markdown(pg_bg_img, unsafe_allow_html=True)

st.markdown(f"""
<h1 style="font-family:Courier; color:white; font-size: 80px;", align="center">BunkMaster</h1>
                <br>""",
                unsafe_allow_html=True)
option = st.selectbox("Select one",["Maintain Minimum attendance percentage","Flexible Attendance Tracking"])

try:
    if option == "Maintain Minimum attendance percentage":

        attendance = st.number_input(label="Enter the minimum attendance percentage: :red[*]",
                             min_value=0,
                             max_value=100,
                             value=None,
                             format="%d",

                            )
        total = st.number_input(label="Enter the total number of classes: :red[*]",
                        min_value=0,
                        value=None,
                        format="%d",

                        )

        attended = st.number_input(label="Enter the total number of classes you attended: :red[*]",
                                 min_value=0,
                                 value=None,
                                 format="%d",

                           )

        col4, col5, col6 = st.columns([1.4,0.6,1.4])
        with col5:
            calculate = st.button("Calculate")
        if calculate == True:
            atten_percent = float((attended / total) * 100)
            classes_attended = int(attendance * (total / 100))
            bunk = (abs(classes_attended - attended))
            bunked = float((attended / (total + bunk) * 100))
            if total < attended:
                st.warning("invalid input")


            elif atten_percent >= attendance and bunked >= attendance:






                with st.container(height=110,border=True):
                    col1, col2, col3, col7 = st.columns([1.5, 1.7,2.2, 1.5])
                    col2.metric("Current attendance", f"{round(atten_percent,2)}%")
                    col3.metric("Attendance after bunking", f"{round(bunked,2)}%")
                if bunk == 1:

                    st.markdown(f"""
                                <h1 style="font-family:Monospace; color:black; font-size: 40px;", align="center">You can bunk {int(bunk)} class</h1>
                                <br>""",
                            unsafe_allow_html=True)
                    st.markdown(f"""
                                    <h6 style="font-family:Monospace; color:black; font-size: 35px;", align="center">Have fun!</h6>
                                    br>""",
                            unsafe_allow_html=True)
                else:
                        st.markdown(f"""
                                        <h1 style="font-family:Monospace; color:black; font-size: 40px;", align="center">You can bunk {int(bunk)} classes</h1>
                                        <br>""",
                                    unsafe_allow_html=True)
                        st.markdown(f"""
                                    <h6 style="font-family:Monospace; color:black; font-size: 35px;", align="center">Have fun!</h6>
                                    <br>""",
                                    unsafe_allow_html=True)






            elif atten_percent > attendance and bunked < attendance:

                while bunked < attendance:
                    bunk = bunk - 1
                    bunked = float((attended / (total + bunk) * 100))
                    with st.container(height=110,border=True):
                        col1, col2, col3, col7 = st.columns([1.5, 1.7,2.2, 1.5])
                    col2.metric("Current attendance", round(atten_percent,2) )
                    col3.metric("Attendance after bunking", round(bunked,2))

                    if bunk == 1:

                        st.markdown(f"""
                                                    <h1 style="font-family:Monospace; color:black; font-size: 40px;",align="center">You can bunk {int(bunk)} class</h1>
                                                    <br>""",
                                    unsafe_allow_html=True)
                        st.markdown(f"""
                                                                <h1 style="font-family:Monospace; color:black; font-size: 35px;", align="center">Have fun!</h1>
                                                                <br>""",
                                    unsafe_allow_html=True)
                    elif bunk == 0:
                        st.markdown(f"""
                            <h1 style="font-family:Monospace; color:black; font-size: 40px; text-align: center;">You can bunk {int(bunk)} classes</h1>
                            <br>""",
                                    unsafe_allow_html=True)


                    else:
                        st.markdown(f"""
                                    <h1 style="font-family:Monospace; color:black; font-size: 40px;", align="center">You can bunk {int(bunk)} classes</h1>
                                    <br>""",
                                    unsafe_allow_html=True)
                        st.markdown(f"""
                                    <h1 style="font-family:Monospace; color:black; font-size: 35px;", align="center">Have fun!</h1>
                                    <br>""",
                                    unsafe_allow_html=True)

            elif atten_percent < attendance:
               st.warning("Your attendance percentage is below 75% , you cannot bunk any classes")




    if option == "Flexible Attendance Tracking":
        attendance = st.number_input(label="Enter the minimum attendance percentage: :red[*]",
                                     min_value=0,
                                     max_value=100,
                                     value=None,
                                     format="%d",

                                       )
        total = st.number_input(label="Enter the total number of classes: :red[*]",
                                min_value=0,
                                value=None,
                                format="%d",

                                  )

        current_classes = st.number_input(label="Enter the number of classes completed till date: :red[*]",
                                             min_value=0,
                                             value=None,
                                             format="%d",
                                             key="current_classes_input_1"
                                            )

        current_attendance = st.number_input(label="Enter your current attendance percentage: :red[*]",
                                   min_value=0,
                                   value=None,
                                   format="%d",
                                   key="current_attendance_input_1"
                                               )
        col4, col5, col6 = st.columns([1.4, 0.6, 1.4])
        with col5:
            calculate_1 = st.button("Calculate")

        if calculate_1 == True:
            a = math.floor(current_attendance)
            b = int((a / 100) * current_classes)
            user_classes = math.floor(
                int(current_classes) - ((a / 100) * current_classes))
            minimum_classes = total - int((attendance / 100) * total)

            if current_classes > total:
                st.warning("Current number of classes cannot be greater than the total number of classes")
            else:
                while True:
                    final = float(((total - minimum_classes) / total) * 100)

                    if final >= attendance:
                        break

                    else:
                        minimum_classes = minimum_classes - 1

                if user_classes < minimum_classes:
                    a = minimum_classes - user_classes
                    if a == 1:
                        st.markdown(f"""
                            <h1 style="font-family:Monospace; color:black; font-size: 30px;", align="center">You can bunk {int(a)} more class</h1>
                            <br>""",
                                    unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                            <h1 style="font-family:Monospace; color:black; font-size: 30px;", align="center">You can bunk {int(a)} more classes</h1>
                            <br>""",
                                    unsafe_allow_html=True)

                elif user_classes == minimum_classes:
                    st.warning(f"You have to attend all classes to maintain {attendance}%")

                elif user_classes > minimum_classes:
                    st.error(f"You cannot maintain {attendance}%")



except ZeroDivisionError:
        st.warning("Please enter the values")

except TypeError:
    st.warning("Please enter a value in this field")










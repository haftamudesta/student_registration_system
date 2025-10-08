import customtkinter as ctk
from PIL import Image
from tkinter.ttk import Treeview, Style
from tkinter.filedialog import askopenfile

window = ctk.CTk()
window.title("Student Registration")
window.geometry("600x600")


def ask_open_profile_picture():
    ask_open_file = askopenfile()


main_frame = ctk.CTkFrame(
    master=window,
    width=550,
    height=570,
    fg_color="#091927",
    border_color="#0078d7",
    border_width=1.5,
    corner_radius=10)

heading_tag = ctk.CTkLabel(
    master=main_frame,
    font=("Bold", 25),
    text="Student Registration System",
    width=400,
    height=30,
    bg_color="#0078d7")
heading_tag.place(x=23, y=10)
add_custom_btn_frame = ctk.CTkFrame(
    master=main_frame,
    width=100,
    height=100,
    border_width=1,
    border_color="pink"
)
profile_image = ctk.CTkImage(Image.open("images/profile.jpg"), size=(80, 80))
add_picture_button = ctk.CTkButton(
    master=add_custom_btn_frame, text="", image=profile_image, width=0, height=0, fg_color="transparent", command=ask_open_profile_picture)

add_picture_button.place(x=5, y=5)
add_custom_btn_frame.place(x=400, y=80)

student_id_number_entry = ctk.CTkEntry(
    master=main_frame, font=("Bold", 15), width=280, placeholder_text="Enter Student Id Number")
student_id_number_entry.place(x=25, y=80)

student_full_name_entry = ctk.CTkEntry(
    master=main_frame, font=("Bold", 15), width=280, placeholder_text="Enter Student Full Name")
student_full_name_entry.place(x=25, y=120)

student_age_entry = ctk.CTkEntry(
    master=main_frame, font=("Bold", 15), width=280, placeholder_text="Enter Student Age")
student_age_entry.place(x=25, y=160)

select_student_gender_lb = ctk.CTkLabel(
    master=main_frame,
    font=("Bold", 15),
    text="Select Student gender:", text_color="WHITE")
select_student_gender_lb.place(x=25, y=220)


gender_var = ctk.StringVar(value="")

gender_male_btn = ctk.CTkRadioButton(
    master=main_frame,
    text="Male",
    variable=gender_var,
    value="Male",
    font=("Bold", 15),
    text_color="white",
    fg_color="#0078d7",
    hover_color="#005a9e"
)
gender_male_btn.place(x=200, y=225)

gender_female_btn = ctk.CTkRadioButton(
    master=main_frame,
    text="Female",
    variable=gender_var,
    value="Female",
    font=("Bold", 15),
    text_color="white",
    fg_color="#0078d7",
    hover_color="#005a9e"
)
gender_female_btn.place(x=260, y=225)

student_classes = ["Select Class", "4th", "5th",
                   "6th", "7th", "8th", "9th", "10th", "11th", "12th"]


select_student_class_lb = ctk.CTkLabel(
    master=main_frame,
    font=("Arial", 15, "bold"),
    text="Select Student Class:",
    text_color="white"
)
select_student_class_lb.place(x=25, y=260)
select_student_class_box = ctk.CTkComboBox(
    master=main_frame,
    values=student_classes,
    state="readonly",
    width=200,
    height=35,
    font=("Arial", 14),
    dropdown_font=("Arial", 14),
    fg_color="#2b2b2b",
    border_color="#0078d7",
    border_width=2,
    text_color="white",
    button_color="#0078d7",
    button_hover_color="#005a9e",
    dropdown_fg_color="#2b2b2b",
    dropdown_text_color="white",
    dropdown_hover_color="#0078d7"
)
select_student_class_box.place(x=200, y=260)
select_student_class_box.set("Select Class")

register_btn = ctk.CTkButton(
    master=main_frame, fg_color="#09a511", text_color="White", font=("Arial", 15, "bold"), text="Register", width=100)
register_btn.place(x=25, y=320)

update_btn = ctk.CTkButton(
    master=main_frame, fg_color="#bed116", text_color="White", font=("Arial", 15, "bold"), text="Update", width=100)
update_btn.place(x=160, y=320)


clear_btn = ctk.CTkButton(
    master=main_frame, fg_color="#d1162f", text_color="White", font=("Arial", 15, "bold"), text="Clear", width=100)
clear_btn.place(x=280, y=320)

find_student_entry = ctk.CTkEntry(
    master=main_frame, font=("Bold", 15), width=180, placeholder_text="Search Student:")
find_student_entry.place(x=25, y=360)

find_student_options = ["Id", "Name", "Class"]

find_student_option_box = ctk.CTkComboBox(
    master=main_frame,
    values=find_student_options,
    state="readonly",
    width=200,
    height=35,
    font=("Arial", 14),
    dropdown_font=("Arial", 14),
    fg_color="#2b2b2b",
    border_color="#0078d7",
    border_width=2,
    text_color="white",
    button_color="#0078d7",
    button_hover_color="#005a9e",
    dropdown_fg_color="#413e3e",
    dropdown_text_color="white",
    dropdown_hover_color="#0078d7"
)
find_student_option_box.place(x=210, y=360)
find_student_option_box.set("Search By")

theme_configuration = {
    "Treeview": {
        "configure": {
            "background": "white",
            "fieldbackground": "white",
            "foreground": "black",
            "rowheight": 25,
            "font": ('Arial', 10)
        },
        "map": {
            "background": [('selected', '#347083')],
            "foreground": [('selected', 'white')]
        }
    },
    "Treeview.Heading": {
        "configure": {
            "background": "lightblue",
            "foreground": "darkblue",
            "relief": "raised",
            "padding": (5, 2),
            "font": ('Arial', 10, 'bold')
        },
        "map": {
            "background": [
                ('pressed', 'darkblue'),
                ('active', '#a6d4f2')
            ],
            "foreground": [
                ('pressed', 'white'),
                ('active', 'darkred')
            ]
        }
    },
    "TButton": {
        "configure": {
            "background": "lightgreen",
            "foreground": "darkgreen",
            "padding": (10, 5)
        },
        "map": {
            "background": [
                ('pressed', 'darkgreen'),
                ('active', '#90EE90'),
                ('disabled', 'lightgray')
            ],
            "foreground": [
                ('pressed', 'white'),
                ('active', 'black'),
                ('disabled', 'gray')
            ]
        }
    }
}

style = Style()
style.theme_create(themename="custom", parent="clam",
                   settings=theme_configuration)
style.theme_use(themename="custom")


records_table = Treeview(master=main_frame, columns=(
    "ID", "Name", "Age", "Gender", "Class"), show="headings")
records_table.column(column="ID", width=80, anchor="w")
records_table.heading(column="ID", text="Id Number", anchor="w")
records_table.column(column="Name", width=120, anchor="w")
records_table.heading(column="Name", text="Full Nmae", anchor="w")
records_table.column(column="Age", width=60, anchor="w")
records_table.heading(column="Age", text="Age", anchor="w")
records_table.column(column="Gender", width=80, anchor="w")
records_table.heading(column="Gender", text="Gender", anchor="w")
records_table.column(column="Class", width=80, anchor="w")
records_table.heading(column="Class", text="Class", anchor="w")
records_table.place(x=25, y=400, width=500, height=100)
clear_selection_btn = ctk.CTkButton(
    master=main_frame, text="Clear Selection", fg_color="#ff7f27", text_color="black", font=("Bold", 20), width=100)
clear_selection_btn.place(x=50, y=510)

delete_record_btn = ctk.CTkButton(
    master=main_frame, text="Delete Record", fg_color="#f50505", text_color="black", font=("Bold", 20), width=100)
delete_record_btn.place(x=240, y=510)
main_frame.place(x=25, y=5)
window.resizable(width=False, height=False)
window.mainloop()

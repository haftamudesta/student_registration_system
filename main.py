import customtkinter as ctk
from PIL import Image

window = ctk.CTk()
window.title("Student Registration")
window.geometry("600x600")

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
    master=add_custom_btn_frame, text="", image=profile_image, width=0, height=0, fg_color="transparent")

add_picture_button.place(x=5, y=5)
add_custom_btn_frame.place(x=400, y=80)

student_id_number_entry = ctk.CTkEntry(
    master=main_frame, font=("Bold", 15), width=280, placeholder_text="Enter Student Number Id")
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
    button_color="#0078d7",
    button_hover_color="#005a9e",
    dropdown_fg_color="#2b2b2b",
    dropdown_text_color="white",
    dropdown_hover_color="#0078d7"
)
select_student_class_box.place(x=200, y=260)
select_student_class_box.set("Select Class")


main_frame.place(x=25, y=5)
window.resizable(width=False, height=False)
window.mainloop()

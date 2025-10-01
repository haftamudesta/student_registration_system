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


main_frame.place(x=25, y=5)
window.resizable(width=False, height=False)
window.mainloop()

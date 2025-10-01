import customtkinter as ctk

window = ctk.CTk()
window.title("Student Registration")
window.geometry("600x600")

main_frame = ctk.CTkFrame(
    master=window,
    width=550,
    height=570,
    border_color="#0078d7",
    border_width=1.5,
    corner_radius=10
)

heading_tag = ctk.CTkLabel(
    master=main_frame,
    font=("Bold", 25),
    text="Student Registration System",
    width=400,
    height=30,
    bg_color="#0078d7")
heading_tag.place(x=23, y=5)
main_frame.place(x=25, y=10)

window.mainloop()

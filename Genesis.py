import customtkinter as ctk
from PIL import Image

# Configurações iniciais
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Janela principal
app = ctk.CTk()
app.geometry("800x500")
app.title("Image Example")

# Frame lateral
sidebar = ctk.CTkFrame(app, width=200, corner_radius=0)
sidebar.pack(side="left", fill="y")

# Ícones (certifique-se de que esses arquivos existem)
home_icon = ctk.CTkImage(Image.open("home.png"), size=(20, 20))
chat_icon = ctk.CTkImage(Image.open("chat.png"), size=(20, 20))
lock_icon = ctk.CTkImage(Image.open("lock.png"), size=(20, 20))

# Menu lateral
ctk.CTkLabel(sidebar, text="Image Example", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=20)

ctk.CTkButton(sidebar, text="Home", image=home_icon, anchor="w").pack(pady=5, padx=10, fill="x")
ctk.CTkButton(sidebar, text="Frame 2", image=chat_icon, anchor="w").pack(pady=5, padx=10, fill="x")
ctk.CTkButton(sidebar, text="Frame 3", image=lock_icon, anchor="w").pack(pady=5, padx=10, fill="x")

# Tema switcher
tema_combo = ctk.CTkOptionMenu(sidebar, values=["System", "Light", "Dark"], command=ctk.set_appearance_mode)
tema_combo.set("System")
tema_combo.pack(side="bottom", pady=10, padx=10)

# Área principal
main_frame = ctk.CTkFrame(app, corner_radius=10)
main_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

# Imagem grande
img_grande = ctk.CTkLabel(main_frame, text="Large Test Image", height=100, width=400,
                          font=ctk.CTkFont(size=24, weight="bold"),
                          corner_radius=20, fg_color=("#1E88E5", "#1976D2"))
img_grande.pack(pady=20)

# Ícone para os botões
img_icon = ctk.CTkImage(Image.open("image_icon.png"), size=(20, 20))

# Botões com ícone
for _ in range(4):
    ctk.CTkButton(main_frame, text="CTkButton", image=img_icon).pack(pady=10)

app.mainloop()

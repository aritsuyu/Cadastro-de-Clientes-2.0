import customtkinter as ctk

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

# Título do menu
ctk.CTkLabel(sidebar, text="Image Example", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=20)

# Botões do menu lateral (sem ícones)
ctk.CTkButton(sidebar, text="🏠  Home", anchor="w").pack(pady=5, padx=10, fill="x")
ctk.CTkButton(sidebar, text="💬  Frame 2", anchor="w").pack(pady=5, padx=10, fill="x")
ctk.CTkButton(sidebar, text="🔒  Frame 3", anchor="w").pack(pady=5, padx=10, fill="x")

# Tema switcher
tema_combo = ctk.CTkOptionMenu(sidebar, values=["System", "Light", "Dark"], command=ctk.set_appearance_mode)
tema_combo.set("System")
tema_combo.pack(side="bottom", pady=10, padx=10)

# Área principal
main_frame = ctk.CTkFrame(app, corner_radius=10)
main_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

# Caixa grande com texto (simulando a imagem grande da interface)
big_box = ctk.CTkLabel(
    main_frame,
    text="Large Test Image",
    height=100,
    width=400,
    font=ctk.CTkFont(size=24, weight="bold"),
    corner_radius=20,
    fg_color=("#2196F3", "#1976D2"),  # degrade azul
    text_color="white"
)
big_box.pack(pady=30)

# Botões empilhados (sem imagens)
for _ in range(4):
    ctk.CTkButton(main_frame, text="CTkButton").pack(pady=10)

app.mainloop()

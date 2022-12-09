from tkinter import *
from tkinter import filedialog as fido
from PIL import Image, ImageDraw, ImageFont, ImageTk

img_path = ''

def bt_upload_clicked():
    global img_path
    img_path = fido.askopenfilename(title="Pick your image", filetypes=(('png', '*.png'), ('jpg', '*.jpg')))
    if img_path:
        image = PhotoImage(file=img_path)
        w, h = image.width(), image.height()
        canvas.config(width=w, height=h)
        canvas.itemconfig(cv_image, image=image)
        canvas.mainloop()

def bt_add_watermark_clicked():
    global img_path
    image = Image.open(img_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 13)

    # add watermark
    pos = (image.width/2, image.height/2)
    draw.text(pos, "this is watermark", (0, 0, 255), font=font)

    # convert Image to PhotoImage
    show_image = ImageTk.PhotoImage(image)
    canvas.itemconfig(cv_image, image=show_image)
    canvas.mainloop()


# ===================== GUI ==========================
BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Courier", 13, "bold")

tk = Tk()
tk.title('Add Watermark GUI')
tk.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

######## row 0 ########
canvas = Canvas(highlightthickness=0)
cv_image = canvas.create_image(100, 100)
canvas.grid(column=0, columnspan=2, row=0)

######## row 1 ########
bt_UploadImage = Button(text="Upload Image", width=15, font=FONT, command=bt_upload_clicked)
bt_UploadImage.grid(column=0, row=1, pady=15)

bt_AddWatermark = Button(text="Add Watermark", width=15, font=FONT, command=bt_add_watermark_clicked)
bt_AddWatermark.grid(column=1, row=1, pady=15)

tk.mainloop()
# ===================== GUI ==========================

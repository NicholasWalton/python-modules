####################################################
# This code still neeed to be completed
###################################################


from tkinter import Tk, Canvas, PhotoImage
from PIL import Image, ImageTk
import os

WIDTH = 750
HEIGHT = 600


def main():
    root = Tk()
    root.title("Googly Eyes")
    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    face = load_image("big_eye_bird.png", (WIDTH, HEIGHT))
    app = GooglyEyes(canvas, face)
    root.mainloop()


class GooglyEyes:
    def __init__(self, canvas, face):
        self.canvas = canvas
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor="nw", image=face)

        # Define eye positions and sizes relative to image size
        self.left_eye_x, self.left_eye_y = 240, 212
        self.right_eye_x, self.right_eye_y = 520, 212
        self.eye_radius = 140

        # Draw initial pupils and store references
        self.left_eye_pupil = self.draw_eye(
            self.left_eye_x, self.left_eye_y, self.eye_radius, "left"
        )
        self.right_eye_pupil = self.draw_eye(
            self.right_eye_x, self.right_eye_y, self.eye_radius, "right"
        )

        # Bind mouse click event to move_eye function
        self.canvas.bind("<Motion>", self.move_eye)
        self.canvas.bind("<Button-1>", print)

    def draw_eye(self, eye_center_x, eye_center_y, eye_radius, side):
        # Calculate pupil positions
        if side == "left":
            pupil_x, pupil_y = eye_center_x - eye_radius, eye_center_y
        else:
            pupil_x, pupil_y = eye_center_x + eye_radius, eye_center_y

        # Draw pupil
        pupil = self.canvas.create_oval(
            pupil_x - 15, pupil_y - 15, pupil_x + 15, pupil_y + 15, fill="black"
        )
        return pupil

    def move_eye(self, event):
        # Move left pupil
        self.canvas.coords(
            self.left_eye_pupil, event.x - 15, event.y - 15, event.x + 15, event.y + 15
        )

        # Move right pupil
        self.canvas.coords(
            self.right_eye_pupil, event.x - 15, event.y - 15, event.x + 15, event.y + 15
        )


def load_image(file, size):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, file)
    image = Image.open(image_path)
    image = image.resize(size, resample=Image.BILINEAR)  # Adjust image size
    return ImageTk.PhotoImage(image)


if __name__ == "__main__":
    main()

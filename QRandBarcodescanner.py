import cv2
from tkinter import Tk, Label, Button, filedialog, messagebox
from pyzbar.pyzbar import decode
import os

# Function to scan codes using the webcam
def scan_from_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Unable to access webcam.")
        return

    print("Starting webcam. Press 'q' to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Unable to read from webcam.")
            break

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            data = obj.data.decode("utf-8")
            obj_type = obj.type
            print(f"Data: {data}, Type: {obj_type}")
            # Draw bounding box
            points = obj.polygon
            if points:
                points = [(int(point.x), int(point.y)) for point in points]
                for i in range(len(points)):
                    cv2.line(frame, points[i], points[(i + 1) % len(points)], (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    f"{obj_type}: {data}",
                    (points[0][0], points[0][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2,
                )

        cv2.imshow("Webcam Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to scan codes from an image file
def scan_from_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")],
    )
    if not file_path:
        return

    if not os.path.exists(file_path):
        messagebox.showerror("Error", "File not found.")
        return

    image = cv2.imread(file_path)
    decoded_objects = decode(image)

    if decoded_objects:
        result = []
        for obj in decoded_objects:
            data = obj.data.decode("utf-8")
            obj_type = obj.type
            result.append(f"{obj_type}: {data}")
        messagebox.showinfo("Decoded Data", "\n".join(result))
    else:
        messagebox.showinfo("No Codes Found", "No QR codes or barcodes found in the image.")

# Function to quit the application
def quit_app():
    root.destroy()

# Initialize Tkinter GUI
root = Tk()
root.title("Barcode & QR Code Scanner")
root.geometry("400x300")
root.resizable(False, False)

# GUI Labels and Buttons
Label(root, text="Barcode & QR Code Scanner", font=("Helvetica", 16)).pack(pady=20)

Button(root, text="Scan from Webcam", command=scan_from_webcam, font=("Helvetica", 14), width=20).pack(pady=10)
Button(root, text="Scan from Image", command=scan_from_image, font=("Helvetica", 14), width=20).pack(pady=10)
Button(root, text="Exit", command=quit_app, font=("Helvetica", 14), width=20).pack(pady=10)

# Run the Tkinter main loop
root.mainloop()

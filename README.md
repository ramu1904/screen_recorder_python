# 🖥️ Screen Recorder (Python + Flask + HTML/JS)

A simple screen recorder application built with **Python**, **Flask**, and **HTML/CSS/JavaScript**.  
It allows you to record either **full screen** or a **custom crop region**, and saves the recording as a video file with a unique name.

---

## 🚀 Features
- 🎥 Record **full screen** or **selected crop region**  
- 💾 Save video with **random unique filename**  
- 🌐 Frontend built with **HTML, CSS, JavaScript**  
- ⚡ Backend built with **Flask, OpenCV, PyAutoGUI**  
- ✅ Start/Stop recording buttons  
- ✅ Live status: frames captured and elapsed time  

---

## 🛠️ Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```
flask
opencv-python
pyautogui
pillow
numpy
pywin32


## ▶️ Run the App

Clone the repository:
```bash
git clone https://github.com/ramu1904/screen_recorder_python.git
cd screen_recorder_python
```

(Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the Flask server:
```bash
python app.py
```
Open in browser:
```bash
http://127.0.0.1:5000
```

## 📂 Project Structure

<img width="453" height="284" alt="image" src="https://github.com/user-attachments/assets/1a2c9f59-0a3a-4d56-8463-55f333e01205" />

## Demo

<img width="1919" height="970" alt="image" src="https://github.com/user-attachments/assets/10bbce71-100e-45e3-96b5-6c6d8087fd22" />

<img width="915" height="672" alt="image" src="https://github.com/user-attachments/assets/3fdd6f23-60fd-443b-848d-6f51a76399d5" />

## 📹 Output

Recordings are saved as .mp4 files with random unique names 

for example :
recording_a1b2c3d4.mp4

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and improve the UI, add new features (like pause/resume, audio capture, or live preview).


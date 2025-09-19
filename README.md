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

project/
│── app.py
│── templates/
│    └── index.html
│── static/
│    ├── style.css
│    └── script.js
│── recordings/      # Folder where recorded videos are saved
│── requirements.txt
│── README.md
│── .gitignore

## 📹 Output

Recordings are saved as .mp4 files with random unique names 

for example :
recording_a1b2c3d4.mp4

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and improve the UI, add new features (like pause/resume, audio capture, or live preview).


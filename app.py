from flask import Flask, render_template, jsonify, request, send_from_directory
import threading, time, os, uuid
import cv2, pyautogui, numpy as np
from win32api import GetSystemMetrics
from datetime import datetime

app = Flask(__name__)

# Folder for recordings
RECORDINGS_DIR = os.path.join(os.path.dirname(__file__), "recordings")
os.makedirs(RECORDINGS_DIR, exist_ok=True)

# Screen dimensions
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

# Globals
is_recording = False
frames = []
start_time = None
stop_time = None
record_mode = "full"
crop_region = None
frame_count = 0
lock = threading.Lock()
current_filename = None

def select_region_opencv():
    """Open a window to drag a rectangle (crop region)."""
    global crop_region
    crop_region = None
    img = pyautogui.screenshot()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    clone = img.copy()

    start_point, end_point, selecting = None, None, False

    def mouse_cb(event, x, y, flags, param):
        nonlocal start_point, end_point, selecting, img, clone
        global crop_region
        if event == cv2.EVENT_LBUTTONDOWN:
            selecting = True
            start_point = (x, y)
            end_point = (x, y)
        elif event == cv2.EVENT_MOUSEMOVE and selecting:
            end_point = (x, y)
            img = clone.copy()
            cv2.rectangle(img, start_point, end_point, (0, 255, 0), 2)
        elif event == cv2.EVENT_LBUTTONUP:
            selecting = False
            end_point = (x, y)
            x1, y1 = start_point
            x2, y2 = end_point
            crop_region = (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
            cv2.destroyWindow("Select Region")

    cv2.namedWindow("Select Region")
    cv2.setMouseCallback("Select Region", mouse_cb)
    while True:
        cv2.imshow("Select Region", img)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC
            crop_region = None
            break
        if crop_region is not None:
            break
    cv2.destroyAllWindows()
    return crop_region

def record_loop():
    global is_recording, frames, start_time, stop_time, frame_count, crop_region, record_mode, current_filename
    frames, frame_count = [], 0

    if record_mode == "full" or crop_region is None:
        region = (0, 0, screen_width, screen_height)
        dim = (screen_width, screen_height)
    else:
        region = crop_region
        dim = (region[2], region[3])

    start_time = time.time()
    print(f"--- Recording started ({record_mode}) ---")

    while True:
        with lock:
            if not is_recording:
                break
        img = pyautogui.screenshot(region=region)
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        frames.append(frame)
        frame_count += 1

    stop_time = time.time()
    recorded_time = stop_time - start_time
    actual_fps = frame_count / recorded_time if recorded_time > 0 else 1.0

    filename = f"recording_{uuid.uuid4().hex[:8]}.mp4"
    current_filename = filename
    out_path = os.path.join(RECORDINGS_DIR, filename)

    writer = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*"mp4v"), actual_fps, dim)
    for f in frames:
        writer.write(f)
    writer.release()
    print(f"--- Saved {filename} ---")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start_record():
    global is_recording, record_mode, crop_region
    with lock:
        if is_recording:
            return jsonify({"status": "already_recording"}), 400
        record_mode = request.json.get("mode", "full")
        if record_mode == "crop":
            sel = select_region_opencv()
            if sel is None:
                return jsonify({"status": "selection_cancelled"}), 400
            crop_region = sel
        is_recording = True
        threading.Thread(target=record_loop, daemon=True).start()
        return jsonify({"status": "started", "mode": record_mode})

@app.route("/stop", methods=["POST"])
def stop_record():
    global is_recording
    with lock:
        if not is_recording:
            return jsonify({"status": "not_recording"}), 400
        is_recording = False
    return jsonify({"status": "stopping"})

@app.route("/status")
def status():
    global is_recording, start_time, stop_time, frame_count
    now = time.time()
    elapsed = (now - start_time) if (start_time and is_recording) else (stop_time - start_time if stop_time else 0)
    return jsonify({
        "recording": is_recording,
        "frames": frame_count,
        "elapsed_seconds": round(elapsed, 2) if elapsed else 0
    })

@app.route("/recordings")
def list_recordings():
    return jsonify(sorted(os.listdir(RECORDINGS_DIR), reverse=True))

@app.route("/download/<path:filename>")
def download(filename):
    return send_from_directory(RECORDINGS_DIR, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

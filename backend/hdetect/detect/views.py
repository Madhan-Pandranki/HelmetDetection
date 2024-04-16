from django.shortcuts import render, redirect,get_object_or_404
from .form import VideoUploadForm,ImageUploadForm,NameURLForm
from .models import Frame,NameURL
import cv2
import os
import subprocess
from django.http import HttpResponse

def home(request):
      return render(request, 'home.html')

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            video_path=video.video.path
            command_v=f"python /home/jitu/Projects/Hdetect/backend/hdetect/yolov9/detect.py --weights /home/jitu/Projects/Hdetect/backend/hdetect/yolov9/best.pt --conf 0.5 --source {video.video.path} --device cpu"
            return_code = os.system(command_v)
            print("Return code:", return_code)
            file_path="/home/jitu/Projects/Hdetect/backend/hdetect/temp.txt"
            line1=""
            with open(file_path, 'r') as file:
                line1 = file.readline()
                print("Line 1:", line1)
            cap = cv2.VideoCapture(line1)
            if not cap.isOpened():
                print("Error: Unable to open video file.")
                return
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to read frame.")
                return
            cv2.imshow('Video', frame)
            while True:
                ret, frame = cap.read()
                if ret:
                    cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
            return redirect('upload_video') 
    else:
        form = VideoUploadForm()
    return render(request, 'upload.html', {'form': form})

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            video_path=video.image.path
            command_v=f"python /home/jitu/Projects/Hdetect/backend/hdetect/yolov9/detect.py --weights /home/jitu/Projects/Hdetect/backend/hdetect/yolov9/best.pt --conf 0.5 --source {video.image.path} --device cpu "
            return_code = os.system(command_v)
            file_path="/home/jitu/Projects/Hdetect/backend/hdetect/temp.txt"
            line1=""
            with open(file_path, 'r') as file:
                line1 = file.readline()
                print("Line 1:", line1)
            image = cv2.imread(line1)
            if image is None:
                print("Error: Unable to read image.")
                return
            cv2.imshow('Image', image)
            while True:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cv2.destroyAllWindows()
            print("Return code:", return_code)
            return redirect('upload_i')
    else:
        form = VideoUploadForm()
    return render(request, 'upload_i.html', {'form': form})
 
def livedetect(request):
    command = ["python", "/home/jitu/Projects/Hdetect/backend/hdetect/yolov9/detect.py", "--weights", "/home/jitu/Projects/Hdetect/backend/hdetect/yolov9/best.pt", "--conf", "0.1", "--source", "0", "--device", "cpu"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout_str = stdout.decode("utf-8")
    stderr_str = stderr.decode("utf-8")
    print("Standard output:")
    print(stdout_str)
    print("Standard error:")
    print(stderr_str)
    return_code = process.returncode
    response_content = f"Return code: {return_code}\n\nStandard output:\n{stdout_str}\n\nStandard error:\n{stderr_str}"
    print("Return code:", return_code)
    return redirect('home')

def add(request):
    if request.method == 'POST':
        form = NameURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = NameURLForm()
    return render(request, 'upload_data.html', {'form': form})

def data(request):
    data_list = NameURL.objects.all()
    return render(request, 'display_data.html', {'data_list': data_list})

def cam_detect(request,pk):
    name_url = get_object_or_404(NameURL, pk=pk)
    url=name_url.url
    print(url)
    command_v=f"python /home/jitu/Projects/Hdetect/backend/hdetect/yolov9/detect.py --weights /home/jitu/Projects/Hdetect/backend/hdetect/yolov9/best.pt --conf 0.5 --source {url} --device cpu"
    return_code = os.system(command_v)
    print("Return code:", return_code)
    return redirect('home')
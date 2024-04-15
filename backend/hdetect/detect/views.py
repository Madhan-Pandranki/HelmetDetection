from django.shortcuts import render, redirect
from .form import VideoUploadForm,ImageUploadForm
from .models import Frame
import cv2
import os
import subprocess
from django.http import HttpResponse

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
            command_v=f"python /home/jitu/Projects/Hdetect/backend/hdetect/yolov9/detect.py --weights /home/jitu/Projects/Hdetect/backend/hdetect/yolov9/best.pt --conf 0.5 --source {video.image.path} --device cpu"
            return_code = os.system(command_v)
            print("Return code:", return_code)
            return redirect('upload_i')
    else:
        form = VideoUploadForm()
    return render(request, 'upload_i.html', {'form': form})

def livedetect(request):
    command = ["python", "/home/jitu/Projects/Hdetect/backend/hdetect/yolov9/detect.py", "--weights", "/home/jitu/Projects/Hdetect/backend/hdetect/yolov9/best.pt", "--conf", "0.5", "--source", "0", "--device", "cpu"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout_str = stdout.decode("utf-8")
    stderr_str = stderr.decode("utf-8")
    print("Standard output:")
    print(stdout_str)
    print("Standard error:")
    print(stderr_str)
    return_code = process.returncode
    print("Return code:", return_code)
    response_content = f"Return code: {return_code}\n\nStandard output:\n{stdout_str}\n\nStandard error:\n{stderr_str}"
    return HttpResponse(response_content)

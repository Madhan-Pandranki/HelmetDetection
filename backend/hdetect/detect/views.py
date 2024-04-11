from django.shortcuts import render, redirect
from .form import VideoUploadForm
from .models import Frame
import cv2

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            convert_to_frames(video)
            return redirect('frame_list')
    else:
        form = VideoUploadForm()
    return render(request, 'upload.html', {'form': form})

def convert_to_frames(video):
    cap = cv2.VideoCapture(video.video.path)
    frame_number = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_number += 1
        # print(frame_number)
        # frame_path = f'frames/{frame_number}.jpg'
        frame_path = f'frames/{frame_number}.jpg'
        cv2.imwrite(frame_path, frame) 

        # Save the frame to database
        frame_obj=Frame(video=video.video, frame_number=frame_number, image=frame_path)
        frame_obj.save()
 
    cap.release()
    cv2.destroyAllWindows()

def frame_list(request):
    frames = Frame.objects.all()
    for frame in frames:
        print(frame.image)
    return render(request, 'frame_list.html', {'frames': frames})

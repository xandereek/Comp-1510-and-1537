video_length = float(input("Enter the video length (minutes): "))
video_frame_rate = int(input("Enter the frame rate (frames per second): "))
video_size = float(input("Enter the size of each frame (MB): "))

total_frames = video_length * 60 * video_frame_rate
total_size_mb = total_frames * video_size
total_size_gb = total_size_mb / 1024

print("Total frames: ", total_frames)
print("Total size(MB): ", total_size_mb)
print("Total size(GB): ", total_size_gb)

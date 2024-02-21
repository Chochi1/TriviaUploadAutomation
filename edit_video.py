from moviepy.editor import VideoFileClip
import os

def cut_video_seconds(start_second, end_second, video_path):
    """
    Cuts the given video to 26 seconds and saves the cut version in the same folder
    with '_cut' appended to the original filename. Returns the path of the cut video.

    :param video_path: Path to the original video
    :return: Path to the cut video
    """
    try:
        # Load the video
        clip = VideoFileClip(video_path)
        
        # Cut the first 26 seconds
        cut_clip = clip.subclip(start_second, end_second)
        
        # Generate new video path
        base, ext = os.path.splitext(video_path)
        new_video_path = f"{base}_cut{ext}"
        
        # Save the cut clip
        cut_clip.write_videofile(new_video_path, codec="libx264", audio_codec="aac")
        
        # Return the new video path
        return new_video_path
    except Exception as e:
        print(f"Error processing video: {e}")
        return None

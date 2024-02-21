# TriviaUploadAutomation
A suite of Python scripts designed to automate the creation, uploading, and SEO optimization of trivia-related video content on YouTube. It simplifies managing video descriptions, tags, and Google API interactions, streamlining the workflow for trivia content creators.

Function, cut_video_seconds, provides a simple and efficient way to trim a video to a specific duration between start_second and end_second,

Utilizing moviepy.editor library, it reads the specified video file from the video_path, extracts a segment of the video as defined by the user, and saves this new, cut version in the same directory as the original file, appending '_cut' to the filename to distinguish it.

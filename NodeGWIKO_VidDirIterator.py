import os
import numpy as np

class NodeGWIKO_VidDirIterator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "directory_path": ("STRING", {}),
                "video_index": ("INT", {"default": 0})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_video_path_by_index"
    CATEGORY = "NodeGWIKO"

    def get_video_path_by_index(self, directory_path, video_index):
        # Get list of video files sorted by modification time (most recent first)
        video_files = sorted(
            [os.path.join(directory_path, f) for f in os.listdir(directory_path)
             if f.lower().endswith(('.mov', '.mp4'))],
            key=lambda x: os.path.getmtime(x),
            reverse=True
        )

        # Wrap the index around using modulo
        video_index = video_index % len(video_files)

        # Return the video file path as a string
        return (video_files[video_index],)
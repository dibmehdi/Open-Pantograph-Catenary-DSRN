# Open-Pantograph-Catenary-DSRN
This GitHub project automates train pantograph analysis, detecting positions, contact points, speed, and kilometer markers in videos. Utilizing OpenCV, it consolidates videos, streamlining railway professionals' workflow.


### Automated Pantograph Analysis with OpenCV

This Python project offers automated analysis of train pantograph movements, contact points, approximate speed, and kilometer markers in videos. The project consists of several modules:

#### 1. `arcs.py`:
   - Detects and highlights arcs in a given video using edge detection and contour analysis techniques.
   - Useful for industries requiring accurate detection of curved objects, such as robotics and quality control systems.

#### 2. `combine.py`:
   - Automates the process of combining multiple video files into a single consolidated video.
   - Provides an organized solution for managing video content efficiently.

#### 3. `decrement.py`:
   - Contains functions to calculate and display the decrement in pantograph movements.
   - Utilizes computer vision techniques to track and analyze the bottom line status of the pantograph system.

#### 4. `increment.py`:
   - Implements algorithms to calculate and display the increment in pantograph movements.
   - Utilizes computer vision techniques for tracking specific points of interest in the pantograph system.

#### 5. `split.py`:
   - Splits the combined video into individual frames for further analysis if needed.
   - Facilitates detailed examination of specific segments of the video content.

#### Key Features:
- **Pantograph Analysis:** Detects pantograph positions and contact points with overhead power lines.
- **Speed Detection:** Approximate speed calculation based on reference points.
- **Kilometer Point Identification:** Determines kilometer markers using reference markers.
- **Video Consolidation:** Automates the process of combining multiple videos into a single consolidated video.
  
#### How to Use:
1. **Setup Environment:**
   - Ensure Python is installed.
   - Install required libraries: `pip install opencv-python matplotlib`.

2. **Run Modules:**
   - Execute the respective Python files based on your analysis needs.
   - Adjust parameters and file paths within each module as required.

#### Sample Usage:
```python
python arcs.py --input video_file.mp4
python combine.py --folder_path video_folder_path
python decrement.py --input video_file.mp4
python increment.py --input video_file.mp4
python split.py --input combined_video.mp4
```

#### Contributors:
- Dib Mehdi

#### Disclaimer:
This project is intended for educational and professional use, specifically for railway industry experts. Please ensure compliance with legal regulations and ethical guidelines while applying these techniques. Refer to the individual module documentation and code comments for detailed information.

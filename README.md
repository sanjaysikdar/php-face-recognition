# PHP Face Recognition Setup

## Requirements

1. **Dlib:**
   - Follow the instructions in [How to Install Dlib Library for Python in Windows 10](https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f) to install Dlib on your system.
   - To check if Dlib is installed, run the following Python code:
     ```python
     import dlib
     print(dlib.__version__)
     ```

2. **face-recognition:**
   - Install the face-recognition library using pip:
     ```bash
     pip install face-recognition
     ```

## File Replacement

1. **Open `face_compare.php`:**
   - Open the `face_compare.php` file in a text editor.

2. **Replace Image Paths:**
   - Locate the lines containing:
     ```php
     $knownImage = "img/real.jpg";
     $unknownImage = "img/fake (2).jpg";
     ```
   - Replace `"img/real.jpg"` and `"img/fake (2).jpg"` with the actual paths to your known and unknown images.
   - **OR** Replace with Image URL 
    ```php
     $knownImage = "https://picsum.photos/200/300";
     $unknownImage = "https://picsum.photos/200/300";
     ```

3. **Save the Changes:**
   - Save the changes to the `face_compare.php` file and execute.


#### Ouput Example:
```bash
OUTPUT: (True, 0.8908031769038957)

User authenticated with confidence level: 89.08%
-------------------------------------
Script execution time: 2.23 seconds
-------------------------------------
```
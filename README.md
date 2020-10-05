#### Image Processing Module

---

This module consists of 3 programs: 

1. imageprocessing.py
2. smoothimage.py 
3. zoomandenhance.py 

###### All programs utilize the [cImage](https://pypi.org/project/cImage/) python module to manipulate inidivudal pixels.

###### Supported file types are: .jpeg; .gif; .tif; .png;

- [Read more](https://pypi.org/project/cImage/) 

---

> ###### imageprocessing.py
>
> The script provides the following functionalities:
>
> 1. Apply negative filter
> 2. Apply gray scale filter 
> 3. Multiply picture size 
> 4. Horizontal flip 
> 5. Vertical flip
>
> How to use: 
>
> 1. Download the image_processing directory
> 2. Run: _python3 imageprocessing.py <filename>_ 
> 3. Follow the Terminal instructions 
> 4. You can test the program using the provided **Earth.gif** and **balloons.gif** 

---

> ###### smoothimage.py
>
> Smooothes out the image. Works by replacing the value of each pixel with the average of 
> the values of the **8 neighboring pixels and itself**.
>
> How to use: 
>
> 1. Download the smooth_zoom directory
> 2. Run: _python3 smoothimage.py <filename>_ 
> 3. You can test the program using the provided **earth-rise.gif** 

---

> ###### zoomandenhance.py
>
> Zooms in on the specified region of the image using a user-defines scaling factor. 
> A valid region is defined by **upper-left** and **lower-right** corners (creates a rectanlge). The program will continue prompting for a valid region until one is chosen.
>
> How to use: 
>
> 1. Download the smooth_zoom directory
> 2. Run: _python3 zoomandenhance.py <filename>_ 
> 3. Follow the Terminal instructions 
> 4. You can test the program using the provided **ferrari.gif** (try the license plate!)


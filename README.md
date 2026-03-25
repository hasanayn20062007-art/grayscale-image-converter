# ⬛ Image to Grayscale Converter

A Python script that converts RGB color images into grayscale using pure matrix math and NumPy broadcasting. 

## 🧠 Concepts Learned & Applied
I built this project to deepen my understanding of how computers process digital images as 3D matrices. Instead of relying on pre-built conversion tools, this script manually calculates the grayscale values.
* **NumPy Arrays:** Handling multidimensional data structures.
* **Array Slicing:** Extracting individual Red, Green, and Blue color channels from a 3D matrix.
* **Matrix Broadcasting:** Applying mathematical operations across entire matrices simultaneously without using slow `for` loops.
* **The Luminosity Method:** Using the weighted formula `(0.299 * R) + (0.587 * G) + (0.114 * B)` to account for human eye sensitivity to different colors.

## 🖼️ Before and After
*(Note: Upload your color image and black & white image to your repo, then put them here!)*
![Original](assets/original_image.jpg) 
![Grayscale](assets/grayscale_result.jpg)

## 🚀 How to Run It
1. Clone this repository to your local machine.
2. Install the required libraries:
   `pip install -r requirements.txt`
3. Add your own image to the `assets` folder.
4. Run the script:
   `python grayscale_converter.py`

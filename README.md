# Barcode and QR Code Scanning

### Project Description:
#### Summary - 
This project implements a barcode and QR code scanning system using digital image processing techniques. It utilizes OpenCV and pyzbar for detecting and decoding codes from both live webcam feeds and static images, with preprocessing methods like edge detection and morphological transformations to enhance accuracy.

#### Course concepts used - 
1. - Morphological transformations
2. - Edge detection
   
#### Additional concepts used -
1. - Bounding box
2. - Decoding algorithms
   
#### Dataset - 
- na

#### Novelty - 
1. - Dynamic Input Selection
2. - Enhanced User Experience
   
### Contributors:
1. Amit Rao (PES1UG22EC023)
2. Arjun Gowda B P (PES1UG22EC046)
3. Jaikumar Emannuel Dcosta (PES1UG22EC101)

### Steps:
1. Clone Repository
```git clone https://github.com/Digital-Image-Processing-PES-ECE/Barcode-and-QR-Code-Scanning.git ```

2. Install Dependencies
```pip install -r requirements.txt```

3. Run the Code
```python QRandBarcodescanner.py ```

### Outputs:
The system outputs the decoded information from detected barcodes or QR codes, displaying it in the user interface or console. For visual feedback, it marks the detected codes with a green bounding box in the live video feed or static image. If no code is detected, an appropriate message is displayed to the user. The decoded data can be directly viewed or further processed for specific applications like inventory management or digital access.

### References:
1. - https://www.geeksforgeeks.org/boundary-extraction-of-image-using-matlab/?ref=lbp
2. - https://youtu.be/Qb4wq2auXXk?si=bV6krsdaw_pvzX8A
3. - https://youtu.be/qYBxIcsr2oY?si=l-V00zpfDuiP5FY-

   
### Limitations and Future Work:
Lighting Sensitivity: The system's accuracy can decrease under poor lighting or extreme glare conditions, affecting barcode/QR code detection.
Limited Formats: The system primarily supports standard barcode and QR code formats; other types, like DataMatrix or Aztec codes, are not implemented.
Partial Obstructions: Heavily damaged or partially obscured barcodes/QR codes may not be detected or decoded successfully.

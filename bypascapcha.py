from PIL import Image
import pytesseract

def decode_captcha(image_path):
    """Decode a CAPTCHA image using Tesseract OCR.

    Args:
        image_path (str): Path to the CAPTCHA image.

    Returns:
        str: The decoded text from the image.
    """
    img = Image.open(image_path)
    # Convert to grayscale
    img = img.convert('L')
    # Binarize the image (thresholding)
    threshold = 150
    img = img.point(lambda p: 255 if p > threshold else 0)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(img, config='--psm 6')  # --psm 6 is generally better for single-line text
    return text.strip()

# Example usage:
image_path = 'GetCaptcha.jpg'  # Replace with the path to your image
decoded_text = decode_captcha(image_path)
print(f"Decoded CAPTCHA: {decoded_text}")

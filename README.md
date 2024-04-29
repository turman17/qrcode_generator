
# QR Code Generator

This Python script allows you to generate QR codes with customizable foreground and background colors.

## Requirements

Before you run the script, make sure to install the required packages:

```bash
pip install qrcode[pil]
```

## Usage

To use the script, simply run it via the command line. Follow the prompts to input the data you want to encode, as well as your desired colors for the QR code:

```bash
python qr_code_generator.py
```

You will be prompted to:
- Enter the data to encode in the QR code (e.g., a URL or text).
- Specify the fill color for the QR code (e.g., 'black').
- Choose a background color for the QR code (e.g., 'white').

## Output

The script will generate a QR code as a PNG file named `qrcode.png` in the same directory as the script. If there is an error with the color inputs, it will default to black on white and print an error message.

## Customization

You can adjust the `version`, `error_correction`, `box_size`, and `border` parameters within the script to customize the QR code's size and resilience to errors.

## Note

Please ensure that the color names or hex values are valid as recognized by PIL. Invalid colors will revert to the default black foreground on a white background.

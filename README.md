# MRZ Extraction Project

This project serves a twofold objective by leveraging the capabilities of MRZ (Machine Readable Zone) technology to flawlessly extract vital data from images, which is then seamlessly presented. Additionally, it empowers the extraction of essential information from Kuwaiti tickets found within PDF files, all while operating within the  Django framework.

## Getting Started

To use this project, follow these steps:

1. Clone the repository:
- git clone https://github.com/abedalkarim99/MRZ_Project

2. Enter the base dir:
- cd MRZ_Project

3. Create a virtual environment and activate it:
- Unix/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
- Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```

4. Install project dependencies using `pip`:
- pip install -r requirements.txt

5. install tesseract:
- Unix/Linux: sudo apt install tesseract-ocr
- Windows: download it from this link https://github.com/UB-Mannheim/tesseract/wiki

6. Run the Django development server:
- python manage.py runserver

7. Open your web browser and go to `http://localhost:8000` to access the application.



## Usage

**Extracting MRZ Information**


1. Upload an image containing MRZ information using the provided form.
2. The MRZ information will be extracted from the image and displayed on the webpage.


**Extracting Kuwaiti Ticket Information**

1. Upload a PDF of a Kuwaiti ticket using the provided form.
2. The relevant information from the Kuwaiti ticket will be extracted and displayed on the webpage.

## Notes

- Make sure you have Python 3.x installed on your system.
- The virtual environment (`venv/`) and any environment-specific files are excluded from version control using `.gitignore`.
- If you encounter any issues or have questions, please refer to the project's documentation or open an issue on the GitHub repository.

## Screenshots
![example](https://github.com/abedalkarim99/MRZ_Project/assets/42090313/46d36ab8-ae64-42c8-aebe-c74e96c7cedd)


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin new-feature`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


# MRZ Extraction Project

This project allows you to extract MRZ (Machine Readable Zone) information from an image and display it using Django.

## Getting Started

To use this project, follow these steps:

1. Clone the repository:
git clone https://github.com/abedalkarim99/MRZ_Project
cd MRZ_Project

2. Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate # On Unix/Linux
venv\Scripts\activate # On Windows

3. Install project dependencies using `pip`:
pip install -r requirements.txt


4. Run the Django development server:
python manage.py runserver


5. Open your web browser and go to `http://localhost:8000` to access the application.

## Usage

1. Upload an image containing MRZ information using the provided form.
2. The MRZ information will be extracted from the image and displayed on the webpage.

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


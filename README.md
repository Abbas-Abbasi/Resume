# Resume Website

This is a resume website created using Python Django and the Pillow library for image processing. The website is built upon a free template obtained from [startbootstrap.com](https://startbootstrap.com/themes), which serves as the foundation for the website's design and layout.

## Technologies Used

- Python Django: Django is a high-level web framework that follows the Model-View-Controller (MVC) architectural pattern. It provides a powerful and flexible toolkit for building web applications.
- Pillow: Pillow is a Python library for image processing. It is used in this project to handle image uploads and perform various image-related operations.
- HTML/CSS/JavaScript: The website utilizes HTML, CSS, and JavaScript to create the user interface and provide interactivity.

## Features

- User-friendly interface: The website features a clean and intuitive user interface, allowing visitors to navigate through the content easily.
- Responsive design: The template used as a base is designed to be responsive, ensuring that the website adapts and looks great on various devices and screen sizes.
- Dynamic content: The backend built with Django enables dynamic content generation, allowing you to easily update and manage your resume information.
- Image processing: The Pillow library is used to handle image uploads, resize and optimize images for display, and perform other image-related operations.
- Customizable: Since the website is built using Django, it is highly customizable. You can easily modify the content, layout, and styling to suit your preferences.

## Installation

To run the resume website locally, follow these steps:

1. Install Python: Make sure Python is installed on your system. You can download it from the official Python website (https://www.python.org) and follow the installation instructions.

2. Clone the repository: Clone the repository containing your Django project to your local machine.

3. Install dependencies: Navigate to the project directory and install the required dependencies using pip. Run the following command:

   ```
   pip install -r requirements.txt
   ```

4. Database setup: Configure the database settings in the Django project's settings.py file. You can choose to use SQLite for development or any other supported database.

5. Apply migrations: Apply the database migrations to create the necessary tables in the database. Run the following command:

   ```
   python manage.py migrate
   ```

6. Run the development server: Start the Django development server by running the following command:

   ```
   python manage.py runserver
   ```

7. Access the website: Open a web browser and enter the URL `http://localhost:8000` to access the locally running resume website.

## Customization

To customize the website for your own resume information, follow these steps:

1. Update resume data: Open the Django project's code and navigate to the relevant files (views, templates) where the resume data is stored. Modify the content to reflect your own resume information.

2. Modify templates: Customize the templates (HTML, CSS, JavaScript) to match your desired layout and design. You can modify the existing templates or create new ones as needed.

3. Add images: Replace the existing images with your own profile picture or other images used on the website. Ensure that the images are stored in the correct directory and update the file paths accordingly.

4. Static files: If you make any changes to the static files (CSS, JavaScript, images), collect the static files by running the following command:

   ```
   python manage.py collectstatic
   ```

5. Test and deploy: Test the customized website locally to ensure everything works as expected. Once satisfied, you can deploy the website to a web server of your choice following Django deployment guidelines.

## License

The specific license terms for the base template used in this project can be found on the [startbootstrap.com](

https://startbootstrap.com/themes) website. Make sure to review and comply with the licensing requirements when using the template.

For the Django code and modifications made for this project, you can choose an appropriate open-source license or customize it as per your preferences.

## Credits

- [startbootstrap.com](https://startbootstrap.com/themes) for providing the base template used in this project.
- Python Django community for the powerful web framework.
- Pillow library developers for the image processing capabilities.
- The open-source community for creating and maintaining the tools and libraries used in this project.

## Disclaimer

This resume website is created for educational and personal use only. Make sure to review and comply with any licensing terms associated with the base template used. Additionally, consider implementing security measures when deploying the website to a production environment.
# Django Dependent Form Tutorial

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Testing](#Testing)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Contact](#contact)

## Overview

This repository contains the code and resources for the Django dependent form tutorial. The tutorial walks you through the process of creating a dependent form using Django and jQuery, offering a more efficient and straightforward approach than a previous method.

## Getting Started

Follow the steps outlined in the article to set up your Django project and implement the dependent form feature.

### Prerequisites

- Python and pip installed
- Basic knowledge of Django

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Afeez1131/dependent-form.git
   cd django-dependent-form-tutorial
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```
5. Create a superuser for the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up your superuser.

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/admin/`.

## Testing

- Visit `http://127.0.0.1:8000/create-person`.

## Contributing

If you'd like to contribute or share your feedback, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [Lawal Afeez](https://www.linkedin.com/in/lawal-afeez/)

## Contact

For inquiries or further information, please contact me at [your.email@example.com](mailto:lawalafeez052@gmail.com).

Happy coding!
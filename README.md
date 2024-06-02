# Home Furniture Store

## Description
"Home" is a sophisticated web application designed for an online furniture store. It enables users to explore a diverse catalog of furniture products, add items to their shopping cart, and complete purchases seamlessly. The application also includes user authentication, a robust cart system, and an admin panel for efficient management of products, users, and orders.

## Installation Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL
- Django 4.2.7

### Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-repository/home-furniture-store.git
    ```

2. **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Create a PostgreSQL database:**
    ```sql
    CREATE DATABASE home;
    ```

4. **Configure the database settings in `settings.py`:**
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'home',
            'USER': 'yourusername',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Run migrations:**
    ```sh
    python manage.py migrate
    ```

6. **Start the server:**
    ```sh
    python manage.py runserver
    ```

## Usage

- Visit `http://127.0.0.1:8000` to access the application.
- Browse through the product catalog.
- Register or login to manage your cart and place orders.

## Features

- **Product Catalog:** Browse a wide variety of furniture products with search functionality.
- **User Authentication:** Secure registration and login system.
- **Shopping Cart:** Add products to your cart and manage them with session integration.
- **Admin Panel:** Manage users, orders, and products efficiently.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Information

- **Email:** [your-email@example.com](mailto:your-email@example.com)
- **GitHub:** [https://github.com/your-username](https://github.com/your-username)

<div align="center">

# 🛒 GreatKart — Production-Oriented Django Ecommerce Platform

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=24&pause=1000&color=2563EB&center=true&vCenter=true&width=900&lines=Production-Oriented+Django+Ecommerce+Project;Authentication%2C+Cart%2C+Checkout%2C+PayPal+Integration;PostgreSQL+Powered+and+Deployed+on+Render" alt="Typing SVG" />

<p>
  <strong>A backend-focused ecommerce project built with Django, PostgreSQL, PayPal Sandbox, and Render deployment.</strong>
</p>

<p>
  This project demonstrates a complete ecommerce workflow including authentication, product browsing, cart and checkout, payment handling, order history, profile management, reviews, and production-style deployment.
</p>

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![PayPal](https://img.shields.io/badge/PayPal-Sandbox-003087?style=for-the-badge&logo=paypal&logoColor=white)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)

</div>

---

## 🚀 Live Demo

**Live Project:**  
[https://ecommerce-django-backend-xnws.onrender.com](https://ecommerce-django-backend-xnws.onrender.com)

---

## 📌 Project Overview

GreatKart is a production-oriented Django ecommerce application built to demonstrate practical backend development through a real purchase lifecycle.

It covers the full customer journey:

- user registration and login
- forgot password and password reset flow
- product browsing and category filtering
- product detail pages with reviews and ratings
- cart and checkout workflow
- PayPal Sandbox payment integration
- payment success and invoice-like order detail pages
- order history tracking
- profile editing and password management
- live deployment on Render with PostgreSQL

The frontend is intentionally simple and usable, while the main focus remains on backend flow, business logic, and production-style project structure.

---

## ✨ Key Features

### 🔐 Authentication & Account Management
- User registration
- User login and logout
- Forgot password flow
- Password reset support
- Change password page
- User dashboard
- Edit profile page
- Profile image fallback handling

### 🛍️ Store & Product Experience
- Homepage with featured products
- Store listing page
- Category-based filtering
- Product detail pages
- Product reviews and star ratings
- Product variations such as color and size

### 🛒 Cart & Checkout
- Add to cart
- Update quantity
- Remove items from cart
- Cart total and tax calculation
- Billing address form
- Checkout summary
- Review order before payment

### 💳 Payments & Orders
- PayPal Sandbox payment integration
- Payment success page
- Order detail / invoice view
- My Orders page with order history

### 🛡️ Backend & Security Highlights
- Modular Django app structure
- PostgreSQL-backed data storage
- Environment-based configuration
- Admin honeypot protection
- Media fallback handling for free-hosting limitations
- Render deployment workflow

---

## 🛠️ Tech Stack

| Category | Technology |
|:--|:--|
| Language | Python |
| Framework | Django |
| Database | PostgreSQL |
| Frontend | Django Templates, Bootstrap, jQuery, JavaScript |
| Payment Gateway | PayPal Sandbox |
| Image Handling | Pillow |
| Deployment | Render |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
ecommerce-django-backend/
│
├── Ecommerce/        # Project configuration (settings, urls, wsgi, asgi)
├── accounts/         # Authentication, profile management
├── store/            # Products, reviews, product detail
├── carts/            # Cart operations and quantity logic
├── category/         # Product categories
├── orders/           # Checkout, payment, and order flow
├── templates/        # Django templates
├── static/           # CSS, JS, and images
├── screenshots/      # README screenshots
└── manage.py
```

---

## 📸 Screenshots

### 🏠 Home Page
![Home Top](screenshots/home_top.png)
![Home Products](screenshots/home_products.png)

### 🛍️ Store Page
![Store](screenshots/store.png)

### 📦 Product Detail
![Product Detail](screenshots/product_detail.png)

### ⭐ Review Section
![Review Section](screenshots/review_section.png)

### 🛒 Cart
![Cart](screenshots/cart.png)

### 🧾 Checkout
![Checkout](screenshots/checkout.png)

### ✅ Review Order & Payment
![Order Review](screenshots/order_review.png)

### 💰 PayPal Sandbox Payment
![PayPal Payment](screenshots/paypal_payment.png)

### 🎉 Payment Successful
![Payment Success](screenshots/payment_success.png)

### 👤 User Dashboard
![Dashboard](screenshots/dashboard.png)

### 📜 My Orders
![My Orders](screenshots/my_orders.png)

### 🧾 Order Detail
![Order Detail](screenshots/order_detail.png)

### ✏️ Edit Profile
![Edit Profile](screenshots/edit_profile.png)

### 🔒 Change Password
![Change Password](screenshots/change_password.png)

### 🔑 Login
![Login](screenshots/login.png)

### 📝 Register
![Register](screenshots/register.png)

### ❓ Forgot Password
![Forgot Password](screenshots/forgot_password.png)

---

## ⚙️ Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/itesh-singh/ecommerce-django-backend.git
cd ecommerce-django-backend
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

For Windows:
```bash
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file and add the required values.

Example:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

GMAIL_CLIENT_ID=your_gmail_client_id
GMAIL_CLIENT_SECRET=your_gmail_client_secret
GMAIL_REFRESH_TOKEN=your_gmail_refresh_token
GMAIL_SENDER_EMAIL=your_sender_email
```

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Create a superuser
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Important Notes

- This project uses **PayPal Sandbox** for payment testing.
- The project is configured with **PostgreSQL**.
- On free hosting platforms like Render, uploaded media files may not always persist permanently, so a fallback profile image is used to keep the UI stable.
- Sensitive values should always be stored in environment variables, not hardcoded in source files.

---

## 🎯 Why This Project Stands Out

This project demonstrates real backend development through a complete ecommerce workflow:

- authentication and account handling
- product browsing and detail logic
- cart and checkout flow
- payment gateway integration
- order persistence and order history
- review and rating functionality
- production deployment and environment configuration

It is a strong portfolio project for Python and Django backend roles because it goes beyond CRUD and shows practical business flow handling.

---

## 👨‍💻 Author

**Itesh Singh**  
Backend Developer focused on Python and Django

- GitHub: [https://github.com/itesh-singh](https://github.com/itesh-singh)
- LinkedIn: [https://www.linkedin.com/in/itesh-singh-113b55323](https://www.linkedin.com/in/itesh-singh-113b55323)
- Email: itesh5906@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

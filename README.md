<div align="center">

# 🛒 GreatKart — Django Ecommerce Platform

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=24&pause=1000&color=2563EB&center=true&vCenter=true&width=700&lines=Production-ready+Django+Ecommerce+Project;Authentication%2C+Cart%2C+Checkout%2C+PayPal+Integration;PostgreSQL+Powered+and+Deployed+on+Render" alt="Typing SVG" />

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

🔗 **Live Project:**  
[https://ecommerce-django-backend-xnws.onrender.com](https://ecommerce-django-backend-xnws.onrender.com)

---

## 📌 Project Overview

GreatKart is a full-featured Django ecommerce project built to demonstrate real backend development skills through a complete shopping workflow.

This project covers:

- user authentication and account management
- product catalog and category browsing
- product detail pages with ratings and reviews
- cart and checkout flow
- PayPal Sandbox payment integration
- order success, order detail, and order history
- profile management and password change
- forgot password flow
- PostgreSQL database integration
- live deployment on Render

The UI is kept simple and practical, while the core focus stays on backend logic, data flow, and real ecommerce functionality.

---

## ✨ Features

### 🔐 Authentication & Account Management
- User registration
- User login and logout
- Forgot password page
- Password reset flow
- Change password page
- User dashboard
- Edit profile page
- Profile image fallback handling

### 🛍️ Store & Product Features
- Homepage with featured products
- Store listing page
- Category-based browsing
- Product detail page
- Product review and rating system
- Color and size selection

### 🛒 Cart & Checkout
- Add to cart
- Update quantity
- Remove items from cart
- Billing address form
- Checkout summary
- Order review before payment

### 💳 Payment & Orders
- PayPal Sandbox integration
- Payment success page
- Order detail / invoice page
- My Orders history page

### 🧠 Backend Highlights
- Modular Django app structure
- Environment-based configuration
- PostgreSQL integration
- Media fallback handling for free hosting limitations
- Real deployed ecommerce flow

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
├── orders/           # Checkout, payment, order flow
├── templates/        # Django templates
├── static/           # CSS, JS, images
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

### 📦 Product Detail Page
![Product Detail](screenshots/product_detail.png)

### ⭐ Reviews Section
![Review Section](screenshots/review_section.png)

### 🛒 Cart Page
![Cart](screenshots/cart.png)

### 🧾 Checkout Page
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

### 🧾 Order Detail / Invoice
![Order Detail](screenshots/order_detail.png)

### ✏️ Edit Profile
![Edit Profile](screenshots/edit_profile.png)

### 🔒 Change Password
![Change Password](screenshots/change_password.png)

### 🔑 Login Page
![Login](screenshots/login.png)

### 📝 Register Page
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
Create a `.env` file and add your required environment variables.

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

## 🔐 Notes

- This project uses **PayPal Sandbox** for payment testing.
- The project is configured with **PostgreSQL**.
- On free hosting platforms like Render, uploaded media files may not always persist permanently, so a fallback profile image is used for a better user experience.
- Sensitive values should always be stored in environment variables.

---

## 🎯 Why This Project Matters

This project demonstrates practical backend development through a real ecommerce workflow:

- authentication
- product management flow
- cart and checkout handling
- payment gateway integration
- order persistence
- review system
- account management
- deployment

It is a strong portfolio project for Python and Django backend roles.

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
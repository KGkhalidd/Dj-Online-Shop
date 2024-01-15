# Online Shopping Platform

## Overview
Developed a feature-rich online shopping platform that enables clients to seamlessly browse products, manage their cart, apply discount codes, complete the checkout process, pay securely with a credit card, and obtain a detailed invoice in PDF format.

## User Interaction
- Each user is assigned a personalized session with a dynamically created cart.
- Users can modify quantities or remove products from their carts.

## Checkout Process
- The checkout process involves creating an order.
- Payment status is determined based on the user's completion of the payment transaction.

## Key Features
- **Asynchronous Email:** Implemented using Celery and RabbitMQ to notify users via email after placing an order.
- **Payment Integration:** Integrated with the Stripe payment gateway.
- **Webhook Endpoint:** Implemented to handle Stripe events and mark orders as paid or pending payment.

## Email Notifications
- Users receive an email with a PDF attachment containing details of the payment and the order.
- Weasyprint library is used to generate and attach the PDF to the email.

## Coupon System
- Implemented a coupon system that users can apply to their carts.
- The discount seamlessly integrates with the Stripe payment system.

## Technologies Used
- Celery
- RabbitMQ
- Stripe Payment Gateway
- Weasyprint

## Usage
1. Clone the repository.
2. Set up virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Configure environment variables for sensitive information.
5. Run the application: `python manage.py runserver`

Feel free to explore and contribute to this online shopping project!

Creative Arts 2024

Creative Arts 2024 is a Django-powered e-commerce platform specializing in graphic design services. The site offers customers options to purchase and inquire about design work like logos, posters, and social media graphics.

Table of Contents

Features

Tech Stack

Setup Instructions

Testing

Usage

Author

License

Features

Dynamic Navigation:

Links to pages such as Home, Shop, Services, and Contact.

User authentication with login and logout.

Shop Functionality:

Display of graphic design options (logos, posters, and social media graphics).

Inquiry section for custom design requests.

Checkout System:

Integration with Stripe for payment processing.

Contact Form:

Users can leave inquiries or feedback, captured via a form.

Responsive Design:

Styled for desktops, tablets, and mobile screens using Bootstrap.

Tech Stack

Backend: Python (Django)

Frontend: HTML, CSS (Bootstrap), JavaScript

Database: SQLite (default, can switch to PostgreSQL for production)

Payment: Stripe API

Setup Instructions

Clone the repository:

git clone <repository-url>
cd CreativeArts2024

Install dependencies:

pip install -r requirements.txt

Run database migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Start the development server:

python manage.py runserver

Access the app at http://127.0.0.1:8000/.

Testing

Here is a checklist of manual and automated tests to ensure the platform functions correctly:

General

Home Page:

Ensure navigation links direct users to the correct pages (Shop, Services, Contact).

Verify that the hero section and featured content display correctly.

Shop Page

Ensure all design options (logos, posters, and social media graphics) are displayed with descriptions.

Verify that clicking on a design redirects to the appropriate detailed page.

Confirm that the inquiry section allows submission of custom design requests.

Contact Page

Test form validation by submitting:

Empty fields (should show validation errors).

Valid inputs (should submit and redirect to a success page).

Verify email and phone capture functionality in the form backend.

Authentication

Login:

Test valid and invalid credentials.

Ensure users are redirected to the correct page post-login.

Logout:

Verify logout functionality clears the session.

Registration:

Ensure new users are added to the database upon successful signup.

Test for duplicate email or username errors.

Checkout

Test payment processing via Stripe:

Use test Stripe API keys.

Ensure successful redirection to Stripe’s hosted checkout page.

Verify that invalid payment information is rejected gracefully.

Forms and Buttons

Click through all buttons and links to ensure:

They are styled correctly.

They navigate to the intended destination.

Submit buttons trigger the correct backend logic.

Error Handling

Check 404 and 500 error pages are styled and informative.

Mobile Responsiveness

Resize the browser to test responsiveness across different screen sizes.

Test navigation menus and buttons on mobile devices.

Automated Tests (Optional)

Write Django tests for:

Models: Validate data constraints.

Views: Ensure correct templates and status codes.

Forms: Test validation logic.

URLs: Verify correct URL mapping.

Usage

Navigate the site using the menu.

Browse the shop to view available design options.

Use the inquiry form for custom graphic design requests.

Register/login to access additional features like checkout.

Complete purchases via the Stripe payment system.

Author

Creative Arts 2024 was developed by Tamarie M. Feel free to reach out with questions or contributions!

**The site is incomplete as can be seen with the shopping basket process not complete. This will be worked on in the near future and updated**

Credits
GitHub Template: Code Institute
ChatGPT: Helpful in providing solutions to occuring erorrs.
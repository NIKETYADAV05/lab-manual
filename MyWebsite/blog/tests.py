from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Book, Product


class HomeViewTests(TestCase):
    def test_homepage_renders_home_template(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/home.html")
        self.assertContains(response, "<title>Home Page</title>")
        self.assertContains(response, "Welcome to the Home Page!")
        self.assertContains(response, "This is the main page of our website")

    def test_about_page_renders_about_template(self):
        response = self.client.get('/about/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/about.html")
        self.assertContains(response, "<title>About Us</title>")
        self.assertContains(response, "About Our Team")
        self.assertContains(response, "We are learning how to build awesome websites using Django!")

    def test_unknown_path_returns_json_404(self):
        response = self.client.get('/missing/')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "404 Not Found")


class BookListViewTests(TestCase):
    def test_book_list_displays_books_from_database(self):
        Book.objects.create(
            title="Pride and Prejudice",
            author="Jane Austen",
            published_date="1813-01-28",
        )

        response = self.client.get(reverse("book_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/book_list.html")
        self.assertContains(response, "Pride and Prejudice")

    def test_book_list_shows_empty_message_when_no_books_exist(self):
        response = self.client.get(reverse("book_list"))

        self.assertContains(response, "No books have been added yet!")


class ContactFormViewTests(TestCase):
    def test_contact_form_renders_form(self):
        response = self.client.get(reverse("contact_form"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/form_page.html")
        self.assertContains(response, "Enter Your Details")

    def test_valid_submission_shows_submitted_values(self):
        response = self.client.post(
            reverse("contact_form"),
            {"name": "Alex Reader", "email": "alex@example.com"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/success.html")
        self.assertContains(response, "Alex Reader")
        self.assertContains(response, "alex@example.com")

    def test_invalid_submission_rerenders_form_with_errors(self):
        response = self.client.post(
            reverse("contact_form"),
            {"name": "Alex Reader", "email": "not-an-email"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/form_page.html")
        self.assertContains(response, "Enter a valid email address.")


class AuthenticationViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="reader",
            password="a-strong-test-password-123",
        )

    def test_login_page_renders_and_loads_site_stylesheet(self):
        response = self.client.get(reverse("login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/login.html")
        self.assertContains(response, "Log In")
        self.assertContains(response, "/static/blog/style.css")

    def test_successful_login_shows_authenticated_user_controls(self):
        response = self.client.post(
            reverse("login"),
            {"username": "reader", "password": "a-strong-test-password-123"},
        )

        self.assertRedirects(response, reverse("home"))
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Welcome, reader!")
        self.assertContains(response, "Log Out")

    def test_logout_requires_post_and_ends_authenticated_session(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 405)

        response = self.client.post(reverse("logout"))
        self.assertRedirects(response, reverse("home"))
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Log In")
        self.assertNotContains(response, "Welcome, reader!")


class ProductAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Notebook",
            description="A ruled notebook",
            price="4.50",
            stock=12,
        )
        self.list_url = "/api/products/"
        self.detail_url = f"{self.list_url}{self.product.pk}/"

    def test_list_products(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Notebook")

    def test_create_update_and_delete_product(self):
        create_response = self.client.post(
            self.list_url,
            {
                "name": "Pen",
                "description": "Blue ink pen",
                "price": "1.25",
                "stock": 20,
            },
            format="json",
        )

        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        product_url = f"{self.list_url}{create_response.data['id']}/"

        update_response = self.client.patch(
            product_url,
            {"stock": 18},
            format="json",
        )
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data["stock"], 18)

        delete_response = self.client.delete(product_url)
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Product.objects.filter(pk=create_response.data["id"]).exists()
        )

    def test_invalid_product_is_rejected(self):
        response = self.client.post(
            self.list_url,
            {
                "name": "",
                "description": "",
                "price": "2.00",
                "stock": 1,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

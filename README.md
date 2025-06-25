# 📝 Blog Stack Backend

A secure and feature-rich Django REST Framework API for managing blogs, categories, and user-submitted reviews — all with full authentication, role-based access, filtering, and throttling.

---

## 🌐 Live Demo

**Base URL:** [`https://blog-13xa.onrender.com`](https://blog-13xa.onrender.com)

> 🔒 All endpoints require a **token** (including `GET` requests).  
> 🎯 Only **admins** can manage categories.  
> ✍️ Blogs and reviews can only be edited or deleted by their **owners**.

---

## ✨ Features

- 🔐 Token-based authentication (DRF)
- 🧑 User registration, login, and self-deletion
- 📚 Blog CRUD with multi-category tagging
- ✍️ User-owned blog reviews
- 🔎 Filtering and search support on all major endpoints
- 🧾 Human-readable API fields (e.g., category names, usernames)
- 🚦 Per-user throttling to avoid abuse
- 🔄 Automatic token generation on user creation
- ⚙️ Deployed on Render with SQLite + WhiteNoise

---

## 🚀 Getting Started Locally

```bash
git clone https://github.com/bitsbuild/blog-stack-backend.git
cd blog-stack-backend/blog

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r ../requirements.txt
python manage.py migrate
python manage.py runserver
````

---

## 🔐 Authentication

Token-based authentication is required for **all endpoints**.

### How to Use in Postman

1. Register or log in to get the token.
2. Add this in **Headers**:

```
Key: Authorization
Value: Token <your_token_here>
```

✅ Example:

```
Authorization: Token 476c9091bb812dc1121fc8abc...
```

---

## 📫 API Overview

> Base paths:
>
> * `/user/` → User authentication (create, login, delete)
> * `/api/` → Blog, Review, Category management

---

### 👤 User Endpoints

#### 🔸 Register

`POST /user/create/`

```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "secure123",
  "confirm_password": "secure123"
}
```

🔁 Response:

```json
{
  "status": "Account Created Successfully",
  "token": "<your_token_here>"
}
```

---

#### 🔸 Login

`POST /user/token/`

```json
{
  "username": "johndoe",
  "password": "secure123"
}
```

🔁 Response:

```json
{
  "token": "<your_token_here>"
}
```

---

#### 🔸 Delete Account

`POST /user/delete/`
🔒 Requires Token Authentication

---

### 📄 Blog Endpoints

> Base: `/api/blogs/`

#### 🔹 List Blogs

`GET /api/blogs/`
🔒 Token Required

Supports:

* Filtering: `?blog_writer=<user_id>&blog_categories=<category_id>`
* Search: `?search=django`

📘 Sample:

```json
{
  "blog_title": "Why Django?",
  "blog_writer": "johndoe",
  "blog_categories": ["Web", "Python"],
  "reviews": [...]
}
```

---

#### 🔹 Create Blog

`POST /api/blogs/`
🔒 Token Required

```json
{
  "blog_title": "Intro to APIs",
  "blog_body": "This is a great intro...",
  "blog_categories": ["Python", "DRF"]
}
```

> 👤 The logged-in user is automatically set as the blog writer.

---

#### 🔹 Update/Delete Blog

`PUT /api/blogs/<id>/`
`DELETE /api/blogs/<id>/`
🔒 Only the blog owner can modify or delete it.

---

### 📝 Review Endpoints

> Base: `/api/review/`

#### 🔹 List Reviews

`GET /api/review/`
🔒 Token Required

Supports:

* Filtering: `?for_blog=<blog_id>&review_writer=<user_id>`
* Search: `?search=great`

---

#### 🔹 Create Review

`POST /api/review/`
🔒 Token Required

```json
{
  "review_title": "Loved it",
  "review_body": "This blog is helpful!",
  "for_blog": "<blog_id>"
}
```

> 👤 The logged-in user is automatically set as the review writer.

---

#### 🔹 Update/Delete Review

`PUT /api/review/<id>/`
`DELETE /api/review/<id>/`
🔒 Only the review author can modify or delete it.

---

### 🏷️ Category Endpoints

> Base: `/api/category/`

#### 🔹 List Categories

`GET /api/category/`
🔒 Admin Only

#### 🔹 Create/Update/Delete Category

`POST /api/category/`
🔒 Admin Only

```json
{
  "category_name": "Tech"
}
```

---

## 🔍 Filters & Search

| Endpoint       | Filters                          | Search Fields                 |
| -------------- | -------------------------------- | ----------------------------- |
| `/api/blogs/`  | `blog_writer`, `blog_categories` | `blog_title`, `blog_body`     |
| `/api/review/` | `for_blog`, `review_writer`      | `review_title`, `review_body` |

---

## 🛡️ Permissions

| Resource   | Read Access       | Write Access      |
| ---------- | ----------------- | ----------------- |
| Users      | 🔒 Token Required | 🔒 Token Required |
| Blogs      | 🔒 Token Required | 🔒 Owner Only     |
| Reviews    | 🔒 Token Required | 🔒 Owner Only     |
| Categories | 🔒 Admin Only     | 🔒 Admin Only     |

✅ Custom permission classes enforce ownership logic.

---

## 🚦 Throttling

| Scope  | Rate    |
| ------ | ------- |
| `anon` | 200/day |
| `user` | 200/sec |

DRF's default throttling is configured in `settings.py`.

---

## ⚙️ Tech Stack

* Python 3.10
* Django 5.x
* Django REST Framework
* SQLite (Dev + Production)
* WhiteNoise (Static files)
* Render.com (Deployment)
* Postman (API testing)

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

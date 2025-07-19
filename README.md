# HROne Backend Intern Task – E-commerce API

This is a backend application built using **FastAPI** and **MongoDB Atlas** as part of the HROne Backend Intern Hiring Challenge. It simulates a basic e-commerce backend system similar to Flipkart/Amazon and includes APIs to manage products and orders.

---

## 🚀 Tech Stack

- **Python 3.10**
- **FastAPI** for web framework
- **MongoDB Atlas (M0 cluster)** as the database
- **Pymongo** as the MongoDB client
- **Railway** for deployment

---

## 📦 Features

### ✅ Products APIs

- **POST `/products`** – Create a new product  
- **GET `/products`** – List products with filters:
  - `name` (regex/partial search)
  - `size` (e.g., `large`)
  - `limit` and `offset` for pagination

### ✅ Orders APIs

- **POST `/orders`** – Create a new order with:
  - `user_id`
  - List of items (`product_id`, `quantity`)
  
- **GET `/orders/{user_id}`** – Get all orders for a user  
  - Supports pagination with `limit` and `offset`

---

## 🛠️ Local Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/hrone-fastapi-task.git
cd hrone-fastapi-task

# 📘 Pydantic Learning

This repository contains my hands-on practice while learning **Pydantic**, a powerful Python library for data validation and serialization.

The examples in this repository cover the fundamental concepts of Pydantic that are widely used in modern Python applications and FastAPI development.

---

## 📚 Topics Covered

- BaseModel
- Field
- Annotated
- Literal
- Field Constraints
- Field Validator
- Model Validator
- Computed Fields
- Nested Models
- Serialization using `model_dump()`

---

## 📂 Repository Structure

```text
.
├── 1_pydantic_why.py
├── 2_field_validator.py
├── 3_model_validator.py
├── 4_computed_fields.py
├── 5_nested_models.py
├── 6_serialization.py
├── requirements.txt
└── README.md
```

---

## 📖 File Description

### 1. Pydantic Introduction

**File:** `1_pydantic_why.py`

Topics covered:

- Why Pydantic is used
- BaseModel
- Type Validation
- Field()
- Annotated
- Literal

---

### 2. Field Validator

**File:** `2_field_validator.py`

Topics covered:

- Custom field validation
- `@field_validator`
- Input validation
- Validation errors

---

### 3. Model Validator

**File:** `3_model_validator.py`

Topics covered:

- Cross-field validation
- `@model_validator`
- Business rule validation

---

### 4. Computed Fields

**File:** `4_computed_fields.py`

Topics covered:

- `@computed_field`
- `@property`
- Dynamic field calculation
- BMI calculation example

---

### 5. Nested Models

**File:** `5_nested_models.py`

Topics covered:

- Nested BaseModels
- Complex request models
- Object composition

---

### 6. Serialization

**File:** `6_serialization.py`

Topics covered:

- `model_dump()`
- Exporting models
- Converting models to dictionaries
- Serialization concepts

---

## 🛠️ Technologies Used

- Python 3
- Pydantic

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/pydantic-learning.git
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🎯 Learning Outcomes

After completing these examples, I gained practical experience with:

- Creating data models using BaseModel
- Validating input data
- Applying field constraints
- Using Annotated and Literal
- Writing custom validators
- Performing cross-field validation
- Creating computed fields
- Working with nested models
- Serializing Pydantic models

---

## 👨‍💻 Purpose

The purpose of this repository is to build a strong foundation in **Pydantic** before developing REST APIs with **FastAPI**. These examples demonstrate the core concepts required for data validation and serialization in modern Python backend development.

---

## ⭐ Future Improvements

- Configuration using `BaseSettings`
- Generic Models
- Custom Types
- Alias Generator
- JSON Schema Generation
- Advanced Serialization
- Integration with FastAPI

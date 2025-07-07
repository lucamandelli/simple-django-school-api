# Simple Django School API

A RESTful API built with Django and Django REST Framework for managing a school system. This API provides endpoints for managing students, courses, and enrollments.

## 🚀 Features

- **Student Management**: Create, read, update, and delete student records
- **Course Management**: Manage courses with different difficulty levels (Basic, Intermediate, Advanced)
- **Enrollment System**: Handle student enrollments in courses with different time periods
- **RESTful API**: Full CRUD operations with proper HTTP methods
- **Filtered Queries**: Get enrollments by student or course
- **Admin Interface**: Built-in Django admin for data management

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd simple-django-school-api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## 📚 API Documentation

### Base URL
```
http://localhost:8000/
```

### Authentication
The API uses Basic Authentication. You'll need to provide credentials for all requests.

### Endpoints

#### Students
- `GET /students/` - List all students
- `POST /students/` - Create a new student
- `GET /students/{id}/` - Get a specific student
- `PUT /students/{id}/` - Update a student
- `DELETE /students/{id}/` - Delete a student

#### Courses
- `GET /courses/` - List all courses
- `POST /courses/` - Create a new course
- `GET /courses/{id}/` - Get a specific course
- `PUT /courses/{id}/` - Update a course
- `DELETE /courses/{id}/` - Delete a course

#### Enrollments
- `GET /enrollments/` - List all enrollments
- `POST /enrollments/` - Create a new enrollment
- `GET /enrollments/{id}/` - Get a specific enrollment
- `PUT /enrollments/{id}/` - Update an enrollment
- `DELETE /enrollments/{id}/` - Delete an enrollment

#### Filtered Queries
- `GET /students/{id}/enrollments/` - Get all enrollments for a specific student
- `GET /courses/{id}/enrollments/` - Get all enrollments for a specific course

### Data Models

#### Student
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "cpf": "12345678901",
  "birth_date": "1990-01-01",
  "phone": "11987654321"
}
```

#### Course
```json
{
  "id": 1,
  "code": "MATH101",
  "description": "Introduction to Mathematics",
  "level": "B"
}
```

**Level Options:**
- `B` - Basic
- `I` - Intermediate
- `A` - Advanced

#### Enrollment
```json
{
  "id": 1,
  "student": 1,
  "course": 1,
  "period": "M"
}
```

**Period Options:**
- `M` - Morning
- `A` - Afternoon
- `N` - Night

## 🔧 Usage Examples

### Creating a Student
```bash
curl -X POST http://localhost:8000/students/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic <base64-encoded-credentials>" \
  -d '{
    "name": "Jane Smith",
    "email": "jane@example.com",
    "cpf": "98765432109",
    "birth_date": "1995-05-15",
    "phone": "11987654321"
  }'
```

### Creating a Course
```bash
curl -X POST http://localhost:8000/courses/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic <base64-encoded-credentials>" \
  -d '{
    "code": "ENG101",
    "description": "English Literature",
    "level": "I"
  }'
```

### Enrolling a Student in a Course
```bash
curl -X POST http://localhost:8000/enrollments/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic <base64-encoded-credentials>" \
  -d '{
    "student": 1,
    "course": 1,
    "period": "M"
  }'
```

## 🗄️ Database

The project uses SQLite as the default database. The database file (`db.sqlite3`) will be created automatically when you run migrations.

## 🔐 Admin Interface

Access the Django admin interface at `http://localhost:8000/admin/` to manage data through a web interface.

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 📦 Dependencies

- **Django 5.0.3** - Web framework
- **Django REST Framework 3.16.0** - REST API framework
- **asgiref 3.9.0** - ASGI utilities
- **Markdown 3.8.2** - Markdown support
- **sqlparse 0.5.3** - SQL parsing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Django Documentation
- Django REST Framework Documentation
- Python Community

## 📞 Support

If you have any questions or need help, please open an issue in the repository.
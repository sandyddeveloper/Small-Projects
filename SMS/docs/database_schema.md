Here's the **`database_schema`** file for CMS project, detailing all models, their fields, relationships, and constraints.  

---

### 📄 **`database_schema.md`**  
#### **Course Management System - Database Schema**

---

## **🛠 User Model**
**Table Name:** `authentication_user`  
**Description:** Stores admin and student details.  

| Column Name   | Data Type     | Constraints                     | Description                  |
|--------------|--------------|--------------------------------|------------------------------|
| id           | UUID (Primary Key) | Auto-generated                 | Unique identifier for user   |
| email        | VARCHAR(255) | Unique, Not Null              | Used for login               |
| phone        | VARCHAR(15)  | Unique, Not Null              | Contact number               |
| password     | VARCHAR(255) | Not Null                      | Hashed password              |
| first_name   | VARCHAR(100) | Optional                      | User’s first name            |
| last_name    | VARCHAR(100) | Optional                      | User’s last name             |
| role         | ENUM('admin', 'student') | Default: 'student' | Defines user role            |
| is_active    | BOOLEAN      | Default: True                 | Controls user status         |
| is_staff     | BOOLEAN      | Default: False                | Admin privileges             |
| date_joined  | DATETIME     | Auto-generated                | Account creation timestamp   |

✅ **Relationships:**  
- **One-to-Many:** Admin can manage multiple students.  

---

## **📚 Course Category Model**  
**Table Name:** `courses_category`  
**Description:** Stores course categories.  

| Column Name | Data Type      | Constraints  | Description              |
|------------|---------------|-------------|--------------------------|
| id         | UUID (Primary Key) | Auto-generated | Unique category ID      |
| name       | VARCHAR(255)  | Unique, Not Null | Category name (e.g., "Programming") |
| description | TEXT         | Optional     | Category details         |

✅ **Relationships:**  
- **One-to-Many:** A category can have multiple courses.  

---

## **📖 Course Model**  
**Table Name:** `courses_course`  
**Description:** Stores courses under categories.  

| Column Name | Data Type      | Constraints      | Description              |
|------------|---------------|-----------------|--------------------------|
| id         | UUID (Primary Key) | Auto-generated  | Unique course ID        |
| name       | VARCHAR(255)  | Unique, Not Null | Course name             |
| category_id | UUID (FK → `courses_category.id`) | Not Null | Belongs to a category  |
| description | TEXT         | Optional        | Course details          |
| created_at | DATETIME      | Auto-generated  | Course creation date    |

✅ **Relationships:**  
- **One-to-Many:** A category can have multiple courses.  

---

## **👨‍🏫 Teacher Model**  
**Table Name:** `courses_teacher`  
**Description:** Stores teachers who handle courses.  

| Column Name  | Data Type      | Constraints       | Description                   |
|-------------|---------------|------------------|-------------------------------|
| id          | UUID (Primary Key) | Auto-generated | Unique teacher ID            |
| name        | VARCHAR(255)  | Not Null         | Teacher’s name                |
| email       | VARCHAR(255)  | Unique, Not Null | Contact email                 |
| phone       | VARCHAR(15)   | Unique, Not Null | Phone number                  |
| expertise   | TEXT          | Optional         | Teacher’s expertise           |

✅ **Relationships:**  
- **One-to-Many:** A teacher can handle multiple courses.  

---

## **🗓 Schedule Model**  
**Table Name:** `courses_schedule`  
**Description:** Stores course schedules assigned to teachers.  

| Column Name | Data Type      | Constraints                              | Description                   |
|------------|---------------|-----------------------------------------|-------------------------------|
| id         | UUID (Primary Key) | Auto-generated                          | Unique schedule ID            |
| course_id  | UUID (FK → `courses_course.id`) | Not Null | Linked to a course |
| teacher_id | UUID (FK → `courses_teacher.id`) | Not Null | Assigned teacher  |
| date       | DATE          | Not Null                              | Course start date             |
| time       | TIME          | Not Null                              | Course start time             |

✅ **Relationships:**  
- **One-to-One:** Each schedule is linked to one course and one teacher.  

---

## **🧑‍🎓 Student Course Enrollment Model**  
**Table Name:** `courses_studentenrollment`  
**Description:** Links students to their enrolled courses.  

| Column Name | Data Type      | Constraints                              | Description                   |
|------------|---------------|-----------------------------------------|-------------------------------|
| id         | UUID (Primary Key) | Auto-generated                          | Unique enrollment ID         |
| student_id | UUID (FK → `authentication_user.id`) | Not Null | Student enrolled in the course |
| course_id  | UUID (FK → `courses_course.id`) | Not Null | Enrolled course |
| schedule_id | UUID (FK → `courses_schedule.id`) | Not Null | Linked to schedule  |
| acknowledged | BOOLEAN      | Default: False                          | Student acknowledgment status |

✅ **Relationships:**  
- **Many-to-Many:** A student can enroll in multiple courses, and a course can have multiple students.  

---

## **📂 Other Tables**
- **Django Default Tables:**  
  - `django_migrations`
  - `django_session`
  - `django_admin_log`
  - `django_content_type`
  - `auth_permission`
  - `auth_group`
  - `auth_group_permissions`
  - `auth_user_groups`
  - `auth_user_user_permissions`

---

### **📝 Notes:**
1. **`email` is the primary login field** instead of `username`.
2. **Foreign Keys (`FK`) enforce relationships** between models.
3. **UUIDs used for Primary Keys** for better scalability and security.
4. **Students must acknowledge their schedules** to confirm attendance.


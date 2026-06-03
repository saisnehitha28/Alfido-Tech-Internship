# ============================================================
# Alfido Tech Internship - Task 2
# API Integration & JSON Handling using Python
# Name: Goudampally Sai Snehitha
# ID: BS/REG/120205
# ============================================================

import requests
import json
from datetime import datetime

print("=" * 60)
print("      API INTEGRATION & JSON HANDLING PROJECT")
print("      Alfido Tech Internship - Task 2")
print("      Intern: Goudampally Sai Snehitha")
print("=" * 60)

BASE_URL = "https://jsonplaceholder.typicode.com"

# ============================================================
# PART 1 - FETCH USERS DATA
# ============================================================

print("\nPART 1 : FETCHING USERS DATA")
print("-" * 45)

try:
    response = requests.get(f"{BASE_URL}/users")

    if response.status_code == 200:
        users = response.json()

        print("API connected successfully")
        print("Status Code :", response.status_code)
        print("Total Users :", len(users))

        print("\nFirst 3 Users Information:\n")

        for user in users[:3]:
            print("Name    :", user["name"])
            print("Email   :", user["email"])
            print("City    :", user["address"]["city"])
            print("Company :", user["company"]["name"])
            print()

except requests.exceptions.ConnectionError:
    print("Internet connection problem")

except Exception as e:
    print("Error :", e)

# ============================================================
# PART 2 - FETCH POSTS
# ============================================================

print("\nPART 2 : FETCHING POSTS")
print("-" * 45)

try:
    response = requests.get(f"{BASE_URL}/posts")

    if response.status_code == 200:

        posts = response.json()

        print("Posts fetched successfully")
        print("Total Posts :", len(posts))

        print("\nShowing First 3 Posts:\n")

        for post in posts[:3]:
            print("Post ID :", post["id"])
            print("User ID :", post["userId"])
            print("Title   :", post["title"][:45])
            print()

except Exception as e:
    print("Error :", e)

# ============================================================
# PART 3 - FILTERING POSTS
# ============================================================

print("\nPART 3 : FILTERING AND SEARCHING")
print("-" * 45)

try:

    # filter posts by user id
    user_id = 1

    filtered_posts = []

    for post in posts:
        if post["userId"] == user_id:
            filtered_posts.append(post)

    print("Posts by User 1 :", len(filtered_posts))

    # search posts using keyword
    keyword = "qui"

    matched_posts = []

    for post in posts:
        if keyword.lower() in post["title"].lower():
            matched_posts.append(post)

    print("Posts containing keyword 'qui' :", len(matched_posts))

    print("\nSample Matching Posts:\n")

    for item in matched_posts[:2]:
        print("-", item["title"])

except Exception as e:
    print("Error :", e)

# ============================================================
# PART 4 - GROUP USERS BY CITY
# ============================================================

print("\nPART 4 : GROUP USERS BY CITY")
print("-" * 45)

try:

    city_data = {}

    for user in users:

        city = user["address"]["city"]

        if city not in city_data:
            city_data[city] = []

        city_data[city].append(user["name"])

    for city, names in list(city_data.items())[:4]:

        print("\nCity :", city)

        for name in names:
            print(" -", name)

except Exception as e:
    print("Error :", e)

# ============================================================
# PART 5 - POST REQUEST
# ============================================================

print("\nPART 5 : SENDING DATA USING POST")
print("-" * 45)

try:

    new_post = {
        "title": "Learning API Integration",
        "body": "I am learning Python APIs during internship",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=new_post
    )

    if response.status_code == 201:

        result = response.json()

        print("New Post Created Successfully")
        print("New ID :", result["id"])
        print("Title  :", result["title"])

except Exception as e:
    print("Error :", e)

# ============================================================
# PART 6 - UPDATE DATA USING PUT
# ============================================================

print("\nPART 6 : UPDATE DATA USING PUT")
print("-" * 45)

try:

    updated_data = {
        "id": 1,
        "title": "Updated Internship Learning",
        "body": "Learning REST API methods using Python",
        "userId": 1
    }

    response = requests.put(
        f"{BASE_URL}/posts/1",
        json=updated_data
    )

    result = response.json()

    print("Post Updated Successfully")
    print("Updated ID    :", result["id"])
    print("Updated Title :", result["title"])

except Exception as e:
    print("Error :", e)

# ============================================================
# PART 7 - DELETE REQUEST
# ============================================================

print("\nPART 7 : DELETE REQUEST")
print("-" * 45)

try:

    response = requests.delete(f"{BASE_URL}/posts/1")

    if response.status_code == 200:

        print("Post Deleted Successfully")
        print("Status Code :", response.status_code)

except Exception as e:
    print("Error :", e)

# ============================================================
# PART 8 - SAVE USERS DATA INTO JSON FILE
# ============================================================

print("\nPART 8 : SAVE DATA INTO JSON FILE")
print("-" * 45)

try:

    save_data = {
        "student_name": "Goudampally Sai Snehitha",
        "candidate_id": "BS/REG/120205",
        "course": "B.Tech 2nd Year Completed",
        "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "total_users": len(users),
        "users": []
    }

    for user in users:

        temp = {
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"]
        }

        save_data["users"].append(temp)

    with open("api_users.json", "w") as file:
        json.dump(save_data, file, indent=4)

    print("Data saved into api_users.json")

    # reading file again

    with open("api_users.json", "r") as file:

        data = json.load(file)

        print("Saved Users :", data["total_users"])

except Exception as e:
    print("Error :", e)

# ============================================================
# PART 9 - TODO ANALYSIS
# ============================================================

print("\nPART 9 : ANALYZING TODO DATA")
print("-" * 45)

try:

    response = requests.get(f"{BASE_URL}/todos")

    todos = response.json()

    total_todos = len(todos)

    completed = 0

    for todo in todos:

        if todo["completed"] == True:
            completed += 1

    pending = total_todos - completed

    percentage = (completed / total_todos) * 100

    print("Total Todos      :", total_todos)
    print("Completed Todos  :", completed)
    print("Pending Todos    :", pending)
    print("Completion %     :", round(percentage, 2))

    summary = {
        "total_todos": total_todos,
        "completed": completed,
        "pending": pending,
        "completion_percentage": round(percentage, 2)
    }

    with open("todos_summary.json", "w") as file:
        json.dump(summary, file, indent=4)

    print("Todo summary saved successfully")

except Exception as e:
    print("Error :", e)

# ============================================================
# PART 10 - ERROR HANDLING
# ============================================================

print("\nPART 10 : API ERROR HANDLING")
print("-" * 45)

# checking 404 error

try:

    response = requests.get(f"{BASE_URL}/posts/99999")

    if response.status_code == 404:
        print("404 Error Handled Successfully")

except Exception as e:
    print("Error :", e)

# timeout handling

try:

    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=10
    )

    print("Timeout test completed successfully")

except requests.exceptions.Timeout:
    print("Request Timeout Error")

except requests.exceptions.ConnectionError:
    print("No Internet Connection")

except Exception as e:
    print("Unexpected Error :", e)

# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("               TASK 2 COMPLETED")
print("=" * 60)

print("\nTopics Practiced:\n")

topics = [
    "GET Request",
    "POST Request",
    "PUT Request",
    "DELETE Request",
    "JSON Handling",
    "Filtering API Data",
    "Searching Data",
    "Grouping Users",
    "Saving JSON Files",
    "Error Handling in APIs"
]

for topic in topics:
    print("+", topic)

print("\nFiles Created:")
print("+ api_users.json")
print("+ todos_summary.json")

print("\nStudent Details:")
print("Name  : Goudampally Sai Snehitha")
print("ID    : BS/REG/120205")
print("Course: B.Tech 2nd Year Completed")

print("\nThank You")
print("=" * 60)
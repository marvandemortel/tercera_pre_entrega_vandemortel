import sqlite3

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.id}"


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="images")
    title = models.CharField(max_length=50)
    summary = models.TextField()
    content = models.TextField()
    date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.id}"
    
    def get_all(self):

        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM post")

        posts = cursor.fetchall()

        try:
            posts = list(posts)
        except:
            posts = []

        return posts
    
    def get_by_category(self, category):
            
        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM post WHERE category_id = SELECT id FROM category WHERE name = '{category}' ORDER BY date DESC")

        posts = cursor.fetchall()

        try:
            posts = list(posts)
        except:
            posts = []

        return posts
    
    def get_by_search(self, search):
            
        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM post WHERE title LIKE '%{search}%' ORDER BY date DESC")

        posts = cursor.fetchall()

        try:
            posts = list(posts)
        except:
            posts = []

        return posts
    
    def get_by_id(self, id):
        
        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM post WHERE id = {id} ORDER BY date DESC")

        post = cursor.fetchone()

        return post
    
    def get_by_author(self, author):
        
        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM post WHERE author_id = SELECT id FROM user WHERE username = '{author}' ORDER BY date DESC")

        posts = cursor.fetchall()

        try:
            posts = list(posts)
        except:
            posts = []

        return posts
    
    def create_post(self, image, title, summary, content, user_id, category_id):
        
        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute(f"INSERT INTO post (image, title, summary, content, date, author_id, category_id) VALUES ('{image}', '{title}', '{summary}', '{content}', date('now'), '{user_id}', '{category_id}')")

        conn.commit()

    def delete_post(self, id):
        
        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute(f"DELETE FROM post WHERE id = {id}")

        conn.commit()

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatars")
    password = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.username}"
    
    def get_user(self, user_id):
        
        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM user WHERE id = '{user_id}'")

        user = cursor.fetchone()

        return user
    
    def create_user(self, username, avatar, password):
        
        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute(f"INSERT INTO user (username, avatar, password, date) VALUES ('{username}', '{avatar}', '{password}', date('now'))")

        conn.commit()

        return f"{username} has been created successfully!"

    def delete_user(self, id):

        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute(f"DELETE FROM user WHERE id = {id}")

        conn.commit()

        return f"User with id: {id} has been deleted successfully!"
    
    def user_login(self, username, password):
        
        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'")

        user = cursor.fetchone()

        if len(user) == 0:
            return {"value" : False,"status" : "User not found!"}

        return user
    
    def user_logout(self, username):
        
        conn = sqlite3.connect("selfcare_blog.db")

        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM user WHERE username = '{username}'")

        user = cursor.fetchone()

        if len(user) == 0:
            return {"value" : False,"status" : "User not found!"}

        return {"value" : True,"status" : f"{username} has been logged out successfully!"}
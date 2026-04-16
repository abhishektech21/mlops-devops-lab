def greet(name):
    return f"""
Hello, {name}! Welcome to MLOps Lab 🚀
Hi {name}, this is your ML experiment!
Greetings {name}! Let's learn MLOps.
"""

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
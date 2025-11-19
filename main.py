from UserFactory import UserFactory

def main():
    types = ["customer", "delivery", "restaurant", "unknown"]

    for t in types:
        user = UserFactory.create_user(t)
        if user:
            print(f"Created -> {user.__class__.__name__}: ", end="")
            user.describe()
        else:
            print(f"Type '{t}' not recognized.")

if __name__ == "__main__":
    main()


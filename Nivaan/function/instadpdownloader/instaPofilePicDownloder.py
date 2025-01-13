import instaloader as insta

# Create an instance of Instaloader class
ig = insta.Instaloader()

# Get the username from the user
username = input("Enter the username of the profile: ")
ig.download_profile(username, profile_pic_only=True)
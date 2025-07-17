import instaloader

def download_profile_pic(username):
    try:
        loader = instaloader.Instaloader()

        # Only download the profile picture
        loader.download_profile(username, profile_pic_only=True)
        print(f"✅ Profile picture of @{username} downloaded successfully!")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    user = input("Enter Instagram username: ")
    download_profile_pic(user)



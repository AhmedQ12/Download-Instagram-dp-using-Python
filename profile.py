from colored import stylize, fg
import instaloader

print(stylize("\n ==| Download Instagram Profile Picture |== \n",fg("red")))

class Downloader:
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        try:
            self.get_profile_picture(self.username)
            return stylize(f"\nProfile picture of \"{self.username}\" downloaded successfully.\n", fg("green"))
        except:
            return stylize(f"\nUser \"{self.username}\" does not exist.\n", fg("red"))

    def get_profile_picture(self,user):
        session = instaloader.Instaloader()
        session.download_profile(user, profile_pic_only=True)
        return 0
if __name__ == "__main__":
    username = input("Enter your Insta User: ")
    print(Downloader(username))
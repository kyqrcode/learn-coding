def provideAccess(user):
	return {"username": user, "password": "admin"}

def runMatch():
	user = input("Username: ")
	
#check if username matches with users we want to have access
	match user:
		case "Om":
			print("You're account has been suspended. You may access your account again after 3 days.")
		case "Vishal":
			print("Your account has been compromised! Please report to the admin immediately!")
		case "Ky":
			print("Welcome Ky!")
			print(provideAccess("Ky"))
		case _:
			print("You do not have access!")

if __name__ == "__main__":
	for _ in range(3):
		runMatch()
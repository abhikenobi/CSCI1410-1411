# Abhi
# Shrestha
# Date: 02/23/22

def main():
    # Ask user for first name
    firstName = input("Please enter your first name: ")
    # Ask user for last name
    lastName = input("Please enter your last name: ")
    
    # Generate username: lastname with first letter of first name madhuri debnath = debnathm
    userName = lastName.lower()+firstName[0].lower()
    print(f"\nYour username is: {userName}")
    
    # Generate email address: firstname.lastname@ucdenver.edu
    emailDomain = "@ucdenver.edu"
    userEmail = firstName.lower()+"."+lastName.lower()+emailDomain
    print(f"\nYour email is: {userEmail}")
    
main()
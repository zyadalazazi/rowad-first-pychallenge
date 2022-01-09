subjects = ["Math", "Physics", "Chemistry", "Biology", "Geology", "English"]

print("\nThe available subjects:", subjects)

subject_removed = input("\nEnter the subject you would like to remove:")

while(subject_removed.title() not in subjects):
    subject_removed = input("\nEnter a subject that is in the list:")

subjects.remove(subject_removed.title())

print("The new list of subjects after removing {0}: {1}".format(subject_removed, subjects))

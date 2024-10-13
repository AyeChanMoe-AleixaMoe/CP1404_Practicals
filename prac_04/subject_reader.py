FILENAME = "subject_data.txt"

def main():
    """Read subject data and display subject details."""
    subjects = load_data()
    display_subject_details(subjects)


def load_data():
    """Read data from file and return it as a list of lists."""
    input_file = open(FILENAME, "r")
    subjects = []
    for line in input_file:
        parts = line.strip().split(',')  # Split the line into parts
        parts[2] = int(parts[2])  # Convert the number of students to an integer
        subjects.append(parts)  # Add the parts list to the subjects list
    input_file.close()
    return subjects


def display_subject_details(subjects):
    """Display subject details from the list of subjects."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()

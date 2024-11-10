import csv
from datetime import datetime

from project import Project

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    projects = load_projects(FILENAME)  # Modified: load directly from FILENAME
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)  # Modified: load from chosen filename
        elif choice == "S":
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)  # Modified: save to chosen filename
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)  # Placeholder for filtering
        elif choice == "A":
            add_project(projects)  # Placeholder for adding a new project
        elif choice == "U":
            update_project(projects)  # Placeholder for updating a project
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, "r", newline="") as file:
        file.readline()  # Skip the header line
        reader = csv.reader(file, delimiter='\t')  # Modified: Use csv.reader with tab delimiter
        for row in reader:
            projects.append(Project(row[0], row[1], int(row[2]), float(row[3]),
                                    int(row[4])))  # Modified: Correctly create Project with row data
    return projects


def save_projects(filename, projects):
    """Save the list of projects to a file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, delimiter='\t')  # Modified: Use tab delimiter for saving
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])  # Write header
        for project in projects:
            writer.writerow([project.name, project.start_date, project.priority, project.cost_estimate,
                             project.completion_percentage])


def display_projects(projects):
    """Display all projects."""
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]
    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Complete projects:")
    for project in sorted(complete):
        print(f"  {project}")


# Placeholder functions for other options in the menu
def filter_projects_by_date(projects):
    date_string = input("Show projects that start by date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    print("Filtered projects:")
    for project in sorted(filtered_projects, key=lambda project: project.start_date):
        print(f"  {project}")


def add_project(projects):



def update_project(projects):



if __name__ == "__main__":
    main()

import csv
from datetime import datetime
from project import Project

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"

def main():
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
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
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            projects.append(Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4])))
    return projects

def save_projects(filename, projects):
    """Save the list of projects to a file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
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

def filter_projects_by_date(projects):
    """Filter projects by date."""
    date_string = input("Show projects that start by date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    print("Filtered projects:")
    for project in sorted(filtered_projects, key=lambda project: project.start_date):
        print(f"  {project}")

def add_project(projects):
    """Add a new project to the project list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.strptime(start_date_string, "%d/%m/%Y").date()  # Convert to date
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date.strftime("%d/%m/%Y"), priority, cost_estimate, completion_percentage))

def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_index = int(input("Project choice: "))
    project = projects[project_index]
    new_completion_percentage = input("New Percentage (leave blank to keep current): ")
    new_priority = input("New Priority (leave blank to keep current): ")
    project.update(int(new_completion_percentage) if new_completion_percentage else None, int(new_priority) if new_priority else None)


if __name__ == "__main__":
    main()
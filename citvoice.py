# ============================================================
# CITIZENVOICE (CITVOICE)
# Citizen Reporting and Public Infrastructure Response System
# PROG211 - Object-Oriented Programming 1
# ============================================================

# Tuple: fixed list of permitted report statuses.
# This demonstrates the use of a tuple for validation.

REPORT_STATUSES = (
    "Submitted",
    "Under Review",
    "Assigned",
    "In Progress",
    "Resolved",
    "Rejected"
)


class PublicReport:
    """Represents an individual public infrastructure report."""

    def __init__(
        self,
        report_id,
        category,
        problem_type,
        location,
        description,
        priority
    ):
        self.report_id = report_id
        self.category = category
        self.problem_type = problem_type
        self.location = location
        self.description = description
        self.priority = priority
        self.status = "Submitted"

    # Static method
    @staticmethod
    def validate_priority(priority):
        """Check whether a priority value is valid."""

        valid_priorities = ("Low", "Medium", "High", "Urgent")
        return priority.title() in valid_priorities

    # Instance method
    def update_status(self, new_status):
        """Update the status of this report."""

        formatted_status = new_status.title()

        if formatted_status not in REPORT_STATUSES:
            return False

        self.status = formatted_status
        return True

    # Instance method
    def display_details(self):
        """Display the details of this report."""

        print("\n" + "=" * 55)
        print("              CITVOICE REPORT DETAILS")
        print("=" * 55)
        print("Report ID:", self.report_id)
        print("Category:", self.category)
        print("Problem:", self.problem_type)
        print("Location:", self.location)
        print("Description:", self.description)
        print("Priority:", self.priority)
        print("Status:", self.status)
        print("=" * 55)


class ServiceDepartment:
    """Represents a department handling a service category."""

    def __init__(self, department_id, department_name, service_category):
        self.department_id = department_id
        self.department_name = department_name
        self.service_category = service_category

    # Instance method
    def handles_category(self, category):
        """Check whether this department handles a category."""

        return self.service_category == category

    # Instance method
    def display_department(self):
        """Display department information."""

        print("Department ID:", self.department_id)
        print("Department Name:", self.department_name)
        print("Service Category:", self.service_category)


class ReportRecord:
    """Connects a report to its reference and assigned department."""

    next_number = 1

    def __init__(self, report, department):
        self.report = report
        self.department = department

        self.reference_number = "CIT" + str(ReportRecord.next_number)
        ReportRecord.next_number += 1

    # Class method
    @classmethod
    def create_record(cls, report, department):
        """Alternative constructor for creating a report record."""

        return cls(report, department)

    # Instance method
    def assign_department(self, department):
        """Assign a department that handles this report category."""

        if department.handles_category(self.report.category):
            self.department = department
            return True

        return False

    # Instance method
    def display_record(self):
        """Display the report and its assigned department."""

        self.report.display_details()

        if self.department is not None:
            print("Assigned Department:", self.department.department_name)
        else:
            print("Assigned Department: Needs Review")

        print("Reference Number:", self.reference_number)
        print("=" * 55)


class CITVOICE:
    """Main system for registering and managing public reports."""

    def __init__(self):
        # One main list stores all ReportRecord objects.
        self.reports = []

        # Department objects are individual attributes,
        # not another collection of report records.
        self.electricity_department = ServiceDepartment(
            "DEP001",
            "Electricity Services",
            "Electricity"
        )

        self.road_safety_department = ServiceDepartment(
            "DEP002",
            "Road Safety Services",
            "Road Safety"
        )

        self.road_infrastructure_department = ServiceDepartment(
            "DEP003",
            "Road Infrastructure Services",
            "Road Infrastructure"
        )

    def find_department(self, category):
        """Return the department associated with a category."""

        if category == "Electricity":
            return self.electricity_department

        elif category == "Road Safety":
            return self.road_safety_department

        elif category == "Road Infrastructure":
            return self.road_infrastructure_department

        return None

    def register_report(self):
        """Collect information and register a new report."""

        print("\n--- REGISTER A PUBLIC REPORT ---")

        print("\nCategories:")
        print("1. Electricity")
        print("2. Road Safety")
        print("3. Road Infrastructure")

        category_options = {
            "1": "Electricity",
            "2": "Road Safety",
            "3": "Road Infrastructure"
        }

        category_choice = input("Choose a category: ").strip()

        if category_choice not in category_options:
            print("Invalid category. Report was not registered.")
            return

        category = category_options[category_choice]

        problem_type = input("Enter problem type: ").strip()
        location = input("Enter problem location: ").strip()
        description = input("Describe the problem: ").strip()

        if not problem_type or not location or not description:
            print("All report fields must be completed.")
            return

        while True:
            priority = input(
                "Enter priority (Low, Medium, High, Urgent): "
            ).strip()

            if PublicReport.validate_priority(priority):
                priority = priority.title()
                break

            print("Invalid priority. Please try again.")

        department = self.find_department(category)

        report_id = "RPT" + str(ReportRecord.next_number).zfill(3)

        report = PublicReport(
            report_id,
            category,
            problem_type,
            location,
            description,
            priority
        )

        # Demonstrate the class method.
        record = ReportRecord.create_record(report, department)

        # Add the record to the one main list.
        self.reports.append(record)

        print("\nReport registered successfully!")
        print("Your reference number is:", record.reference_number)
        print("Please keep this number for future tracking.")

    def view_all_reports(self):
        """Display all reports stored in the list."""

        print("\n--- ALL PUBLIC REPORTS ---")

        if not self.reports:
            print("No reports have been registered yet.")
            return

        for record in self.reports:
            record.display_record()

    def search_report(self):
        """Search for a report using its reference number."""

        reference = input(
            "Enter the reference number, e.g. CIT1: "
        ).strip().upper()

        for record in self.reports:
            if record.reference_number == reference:
                print("\nReport found!")
                record.display_record()
                return

        print("No report found with that reference number.")

    def update_report(self):
        """Find a report and update its status."""

        reference = input(
            "Enter the report reference number: "
        ).strip().upper()

        for record in self.reports:
            if record.reference_number == reference:

                print("\nCurrent status:", record.report.status)
                print("\nPermitted statuses:")

                for status in REPORT_STATUSES:
                    print("-", status)

                new_status = input(
                    "Enter the new status: "
                ).strip()

                if record.report.update_status(new_status):
                    print("Report status updated successfully.")
                else:
                    print("Invalid status. No changes were made.")

                return

        print("Report not found.")

    def show_statistics(self):
        """Calculate and display a summary of registered reports."""

        total = len(self.reports)

        electricity = 0
        road_safety = 0
        road_infrastructure = 0

        submitted = 0
        under_review = 0
        assigned = 0
        in_progress = 0
        resolved = 0
        rejected = 0

        for record in self.reports:

            report = record.report

            if report.category == "Electricity":
                electricity += 1
            elif report.category == "Road Safety":
                road_safety += 1
            elif report.category == "Road Infrastructure":
                road_infrastructure += 1

            if report.status == "Submitted":
                submitted += 1
            elif report.status == "Under Review":
                under_review += 1
            elif report.status == "Assigned":
                assigned += 1
            elif report.status == "In Progress":
                in_progress += 1
            elif report.status == "Resolved":
                resolved += 1
            elif report.status == "Rejected":
                rejected += 1

        print("\n" + "=" * 45)
        print("          CITVOICE STATISTICS")
        print("=" * 45)

        print("Total Reports:", total)

        print("\nReports by Category")
        print("Electricity:", electricity)
        print("Road Safety:", road_safety)
        print("Road Infrastructure:", road_infrastructure)

        print("\nReports by Status")
        print("Submitted:", submitted)
        print("Under Review:", under_review)
        print("Assigned:", assigned)
        print("In Progress:", in_progress)
        print("Resolved:", resolved)
        print("Rejected:", rejected)

        print("=" * 45)

    def menu(self):
        """Display the main application menu."""

        while True:
            print("\n" + "=" * 55)
            print("              CITIZENVOICE (CITVOICE)")
            print("     Citizen Reporting and Response System")
            print("=" * 55)

            print("1. Register a Report")
            print("2. View All Reports")
            print("3. Search for a Report")
            print("4. Update Report Status")
            print("5. Display Report Statistics")
            print("6. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.register_report()

            elif choice == "2":
                self.view_all_reports()

            elif choice == "3":
                self.search_report()

            elif choice == "4":
                self.update_report()

            elif choice == "5":
                self.show_statistics()

            elif choice == "6":
                print("\nThank you for using CITVOICE.")
                print("Your voice matters!")
                break

            else:
                print("Invalid menu choice. Please select 1-6.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    system = CITVOICE()
    system.menu()
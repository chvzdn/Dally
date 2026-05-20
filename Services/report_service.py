class ReportService:
    """
    Generates a summary
    Combines tasks, notes and schedules
    Can export reports to a text file
    """

    def __init__(self, task_service, note_service, schedule_service):
        # Dependency injection (OOP concept)
        self._task_service = task_service
        self._note_service = note_service
        self._schedule_service = schedule_service

    def generate_report(self):
        # Builds a formatted summary report
        report = []

        # TASK SECTION
        report.append("TASKS")
        for task in self._task_service.get_all():
            status = "✔" if task.completed else "○"
            report.append(f"{status} {task.title}")

        # NOTES SECTION
        report.append("\nNOTES")
        for note in self._note_service.get_all():
            report.append(f"- {note.content}")

        # SCHEDULE SECTION
        report.append("\nSCHEDULE")
        for sched in self._schedule_service.get_all():
            report.append(
                f"{sched.date} {sched.time} -> {sched.task}"
            )

        return "\n".join(report)

    def export_report(self, filename="report.txt"):
        # Export and saves report into a .txt file
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(self.generate_report())
        except Exception as e:
            raise Exception(f"Export failed: {str(e)}")

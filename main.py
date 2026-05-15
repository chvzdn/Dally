import tkinter as tk
from ui.main_gui import DallyPlannerApp

from services.task_service_impl import TaskService
from services.notes_service_impl import NotesService
from services.schedule_service_impl import ScheduleService
from services.report_service import ReportService

# APPLICATION START
def main():
    """
    Initializes all services
    Injects dependencies into UI
    Starts Tkinter main loop
    """

    root = tk.Tk()

    # Initialize services
    task_service = TaskService()
    note_service = NotesService()
    schedule_service = ScheduleService()

    # Report service depends on other services
    report_service = ReportService(
        task_service,
        note_service,
        schedule_service
    )

    # Launch UI
    app = DallyPlannerApp(
        root,
        task_service,
        note_service,
        schedule_service,
        report_service
    )

    root.mainloop()


if __name__ == "__main__":
    main()

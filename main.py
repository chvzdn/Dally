import tkinter as tk

from ui.main_gui import DallyPlannerApp
from services.task_service_impl import TaskService
from services.notes_service_impl import NotesService
from services.schedule_service_impl import ScheduleService

root = tk.Tk()

app = DallyPlannerApp(
    root,
    TaskService(),
    NotesService(),
    ScheduleService()
)

root.mainloop()
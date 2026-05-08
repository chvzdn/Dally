import tkinter as tk
from tkinter import messagebox

# THEME 
BG = "#eef2f7"
CARD = "#ffffff"
TEXT = "#1f2937"
MUTED = "#6b7280"
ROW = "#f9fafb"

PRIMARY = "#6366f1"
DANGER = "#ef4444"

# MAIN APPLICATION CLASS
class DallyPlannerApp:
    """
    Builds the entire Tkinter application
    Handles navigation between pages
    Connects UI to services (dependency injection)
    """
    def __init__(
        self,
        root,
        task_service,
        note_service,
        schedule_service,
        report_service
    ):

        self.root = root

        self.root.title("Dally Planner")
        self.root.geometry("520x650")
        self.root.configure(bg=BG)

        # Dependency Injection
        self.tasks = task_service
        self.notes = note_service
        self.schedule = schedule_service
        self.report_service = report_service

        # NAVIGATION 
        nav = tk.Frame(root, bg=CARD)
        nav.pack(fill="x")

        buttons = [
            ("Tasks", self.show_tasks),
            ("Notes", self.show_notes),
            ("Schedule", self.show_schedule),
            ("Report", self.show_dashboard)
        ]

        for text, command in buttons:

            tk.Button(
                nav,
                text=text,
                bg=PRIMARY,
                fg="white",
                relief="flat",
                command=command
            ).pack(side="left", padx=5, pady=5)

        # PAGES 
        self.container = tk.Frame(root, bg=BG)
        self.container.pack(fill="both", expand=True)

        self.task_page = tk.Frame(self.container, bg=BG)
        self.note_page = tk.Frame(self.container, bg=BG)
        self.schedule_page = tk.Frame(self.container, bg=BG)
        self.dashboard_page = tk.Frame(self.container, bg=BG)

        self.build_tasks()
        self.build_notes()
        self.build_schedule()
        self.build_dashboard()

        self.show_tasks()

    # PAGE NAVIGATION
    def hide_all(self):

        for page in [
            self.task_page,
            self.note_page,
            self.schedule_page,
            self.dashboard_page
        ]:
            page.pack_forget()

    def show_tasks(self):

        self.hide_all()
        self.task_page.pack(expand=True)
        self.render_tasks()

    def show_notes(self):

        self.hide_all()
        self.note_page.pack(expand=True)
        self.render_notes()

    def show_schedule(self):

        self.hide_all()
        self.schedule_page.pack(expand=True)
        self.render_schedule()

    def show_dashboard(self):

        self.hide_all()
        self.dashboard_page.pack(expand=True)
        self.generate_dashboard()

    # TASKS
    def build_tasks(self):

        card = tk.Frame(self.task_page, bg=CARD, padx=20, pady=20)
        card.pack(expand=True)

        tk.Label(
            card,
            text="TASKS",
            font=("Segoe UI", 16, "bold"),
            bg=CARD,
            fg=TEXT
        ).pack(pady=10)

        self.task_entry = tk.Entry(card, width=30)
        self.task_entry.pack()

        tk.Button(
            card,
            text="Add Task",
            bg=PRIMARY,
            fg="white",
            command=self.add_task
        ).pack(pady=5)

        self.task_list = tk.Frame(card, bg=CARD)
        self.task_list.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task.strip():
            self.tasks.add(task)
            self.task_entry.delete(0, tk.END)
            self.render_tasks()

    def render_tasks(self):

        for widget in self.task_list.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.tasks.get_all()):
            row = tk.Frame(self.task_list, bg=ROW)
            row.pack(fill="x", pady=2)

            value = tk.BooleanVar(value=task.completed)

            tk.Checkbutton(
                row,
                text=task.title,
                variable=value,
                bg=ROW,
                command=lambda i=index, v=value:
                self.tasks.toggle(i, v.get())
            ).pack(side="left")

            tk.Button(
                row,
                text="✕",
                bg=ROW,
                fg=DANGER,
                command=lambda i=index:
                self.delete_task(i)
            ).pack(side="right")

    def delete_task(self, index):

        self.tasks.delete(index)
        self.render_tasks()

    # NOTES
    def build_notes(self):

        card = tk.Frame(self.note_page, bg=CARD, padx=20, pady=20)
        card.pack(expand=True)

        tk.Label(
            card,
            text="NOTES",
            font=("Segoe UI", 16, "bold"),
            bg=CARD
        ).pack(pady=10)

        self.note_entry = tk.Entry(card, width=40)
        self.note_entry.pack()

        tk.Button(
            card,
            text="Add Note",
            bg=PRIMARY,
            fg="white",
            command=self.add_note
        ).pack(pady=5)

        self.note_list = tk.Frame(card, bg=CARD)
        self.note_list.pack()

    def add_note(self):

        note = self.note_entry.get()

        if note.strip():
            self.notes.add(note)
            self.note_entry.delete(0, tk.END)
            self.render_notes()

    def render_notes(self):

        for widget in self.note_list.winfo_children():
            widget.destroy()

        for index, note in enumerate(self.notes.get_all()):

            row = tk.Frame(self.note_list, bg=ROW)
            row.pack(fill="x", pady=2)

            tk.Label(
                row,
                text=note.content,
                bg=ROW
            ).pack(side="left")

            tk.Button(
                row,
                text="✕",
                bg=ROW,
                fg=DANGER,
                command=lambda i=index:
                self.delete_note(i)
            ).pack(side="right")

    def delete_note(self, index):

        self.notes.delete(index)
        self.render_notes()

    # SCHEDULE
    def build_schedule(self):

        card = tk.Frame(self.schedule_page, bg=CARD, padx=20, pady=20)
        card.pack(expand=True)

        tk.Label(
            card,
            text="SCHEDULE",
            font=("Segoe UI", 16, "bold"),
            bg=CARD
        ).pack(pady=10)

        def row(label):

            frame = tk.Frame(card, bg=CARD)
            frame.pack(pady=2)

            tk.Label(
                frame,
                text=label,
                width=8,
                anchor="w",
                bg=CARD,
                fg=MUTED
            ).pack(side="left")

            entry = tk.Entry(frame, width=25)
            entry.pack(side="left")

            return entry

        self.date = row("Date:")
        self.time = row("Time:")
        self.task = row("Task:")

        tk.Button(
            card,
            text="Add Schedule",
            bg=PRIMARY,
            fg="white",
            command=self.add_schedule
        ).pack(pady=5)

        tk.Button(
            card,
            text="Clear",
            bg=DANGER,
            fg="white",
            command=self.clear_schedule
        ).pack(pady=5)

        self.schedule_table = tk.Frame(card, bg=CARD)
        self.schedule_table.pack()

    def add_schedule(self):

        self.schedule.assign(
            self.task.get(),
            self.time.get(),
            self.date.get()
        )

        self.render_schedule()

    def clear_schedule(self):

        self.schedule.clear()
        self.render_schedule()

    def render_schedule(self):

        for widget in self.schedule_table.winfo_children():
            widget.destroy()

        for sched in self.schedule.get_all():

            row = tk.Frame(self.schedule_table, bg=ROW)
            row.pack(fill="x", pady=2)

            tk.Label(
                row,
                text=sched.date,
                width=10,
                bg=ROW
            ).pack(side="left")

            tk.Label(
                row,
                text=sched.time,
                width=10,
                bg=ROW
            ).pack(side="left")

            tk.Label(
                row,
                text=sched.task,
                width=20,
                bg=ROW
            ).pack(side="left")

    # REPORT
    def build_dashboard(self):

        card = tk.Frame(self.dashboard_page, bg=CARD)
        card.pack(expand=True, padx=20, pady=20)

        tk.Label(
            card,
            text="REPORT SUMMARY",
            font=("Segoe UI", 16, "bold"),
            bg=CARD
        ).pack(pady=10)

        self.report = tk.Text(card, width=45, height=20)
        self.report.pack()

        tk.Button(
            card,
            text="Export Report",
            bg=PRIMARY,
            fg="white",
            command=self.export_report
        ).pack(pady=10)
        

    def generate_dashboard(self):

        self.report.delete("1.0", tk.END)

        self.report.insert(
            tk.END,
            self.report_service.generate_report()
        )

    def export_report(self):

        self.report_service.export_report()

        messagebox.showinfo(
            "Export Success",
            "Report saved as report.txt"
        )

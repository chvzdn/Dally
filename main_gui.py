import tkinter as tk
import os
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
        self.task_service = task_service
        self.note_service = note_service
        self.schedule_service = schedule_service
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

        for text, cmd in buttons:
            tk.Button(nav, text=text, bg=PRIMARY, fg="white", command=cmd)\
                .pack(side="left", padx=5, pady=5)

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

    # ----------- PAGE NAVIGATION ------------
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

    # ---------------- TASKS ----------------
    def build_tasks(self):
        card = tk.Frame(self.task_page, bg=CARD, padx=20, pady=20)
        card.pack(expand=True)

        tk.Label(card, text="TASKS", font=("Segoe UI", 16, "bold"),
                 bg=CARD, fg=TEXT).pack(pady=10)

        self.task_entry = tk.Entry(card, width=30)
        self.task_entry.pack()

        tk.Button(card, text="Add Task", bg=PRIMARY, fg="white",
                  command=self.add_task).pack(pady=5)

        self.task_list = tk.Frame(card, bg=CARD)
        self.task_list.pack()

    def add_task(self):
        try:
            task = self.task_entry.get().strip()

            if not task:
                raise ValueError("Task cannot be empty")

            self.task_service.add(task)
            self.task_entry.delete(0, tk.END)
            self.render_tasks()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def render_tasks(self):
        for w in self.task_list.winfo_children():
            w.destroy()

        for index, task in enumerate(self.task_service.get_all()):
            row = tk.Frame(self.task_list, bg=ROW)
            row.pack(fill="x", pady=2)

            var = tk.BooleanVar(value=task.completed)

            tk.Checkbutton(
                row,
                text=task.title,
                variable=var,
                bg=ROW,
                command=lambda i=index, v=var:
                self.task_service.toggle(i, v.get())
            ).pack(side="left")

            tk.Button(
                row,
                text="✕",
                bg=ROW,
                fg=DANGER,
                command=lambda i=index: self.delete_task(i)
            ).pack(side="right")

    def delete_task(self, index):
        try:
            self.task_service.delete(index)
            self.render_tasks()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- NOTES ----------------
    def build_notes(self):
        card = tk.Frame(self.note_page, bg=CARD, padx=20, pady=20)
        card.pack(expand=True)

        tk.Label(card, text="NOTES", font=("Segoe UI", 16, "bold"),
                 bg=CARD).pack(pady=10)

        self.note_entry = tk.Entry(card, width=40)
        self.note_entry.pack()

        tk.Button(card, text="Add Note", bg=PRIMARY, fg="white",
                  command=self.add_note).pack(pady=5)

        self.note_list = tk.Frame(card, bg=CARD)
        self.note_list.pack()

    def add_note(self):
        try:
            note = self.note_entry.get().strip()

            if not note:
                raise ValueError("Note cannot be empty")

            self.note_service.add(note)
            self.note_entry.delete(0, tk.END)
            self.render_notes()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def render_notes(self):
        for w in self.note_list.winfo_children():
            w.destroy()

        for index, note in enumerate(self.note_service.get_all()):
            row = tk.Frame(self.note_list, bg=ROW)
            row.pack(fill="x", pady=2)

            tk.Label(row, text=note.content, bg=ROW).pack(side="left")

            tk.Button(
                row,
                text="✕",
                bg=ROW,
                fg=DANGER,
                command=lambda i=index: self.delete_note(i)
            ).pack(side="right")

    def delete_note(self, index):
        try:
            self.note_service.delete(index)
            self.render_notes()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- SCHEDULE ----------------
    def build_schedule(self):
        card = tk.Frame(self.schedule_page, bg=CARD, padx=20, pady=20)
        card.pack(expand=True)

        tk.Label(card, text="SCHEDULE", font=("Segoe UI", 16, "bold"),
                 bg=CARD).pack(pady=10)

        def row(label):
            f = tk.Frame(card, bg=CARD)
            f.pack(pady=2)

            tk.Label(f, text=label, width=8, bg=CARD,
                     fg=MUTED, anchor="w").pack(side="left")

            e = tk.Entry(f, width=25)
            e.pack(side="left")
            return e

        self.date = row("Date:")
        self.time = row("Time:")
        self.task = row("Task:")

        tk.Button(
            card,
            text="Add Schedule",
            bg=PRIMARY,
            fg="white",
            command=self.add_schedule
        ).pack(pady=5, fill="x")

        tk.Button(
            card,
            text="Clear",
            bg=DANGER,
            fg="white",
            command=self.clear_schedule
        ).pack(pady=5, fill="x")

        self.schedule_table = tk.Frame(card, bg=CARD)
        self.schedule_table.pack()

    def add_schedule(self):
        try:
            self.schedule_service.assign(
                self.task.get(),
                self.time.get(),
                self.date.get()
            )
            self.render_schedule()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def render_schedule(self):
        for w in self.schedule_table.winfo_children():
            w.destroy()

        for s in self.schedule_service.get_all():
            row = tk.Frame(self.schedule_table, bg=ROW)
            row.pack(fill="x", pady=2)

            tk.Label(row, text=s.date, width=10, bg=ROW).pack(side="left")
            tk.Label(row, text=s.time, width=10, bg=ROW).pack(side="left")
            tk.Label(row, text=s.task, width=20, bg=ROW).pack(side="left")
    def clear_schedule(self):
        try:
            self.schedule_service.clear()
            self.render_schedule()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- REPORT ----------------
    def build_dashboard(self):
        card = tk.Frame(self.dashboard_page, bg=CARD)
        card.pack(expand=True, padx=20, pady=20)

        tk.Label(card, text="REPORT SUMMARY",
                 font=("Segoe UI", 16, "bold"), bg=CARD).pack(pady=10)

        self.report = tk.Text(card, width=45, height=20)
        self.report.pack()

        tk.Button(card, text="Export Report", bg=PRIMARY, fg="white",
                  command=self.export_report).pack(pady=10)

    def generate_dashboard(self):
        self.report.delete("1.0", tk.END)
        self.report.insert(tk.END, self.report_service.generate_report())

    def export_report(self):
        try:
            filename = "report.txt"

            # force remove if file is locked or exists
            if os.path.exists(filename):
                try:
                    os.remove(filename)
                except PermissionError:
                    raise Exception("Close report.txt before exporting")

            self.report_service.export_report()

            messagebox.showinfo("Success", "Report exported successfully")

        except Exception as e:
            messagebox.showerror("Export Error", str(e))

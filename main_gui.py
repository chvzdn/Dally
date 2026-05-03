import tkinter as tk

# ===== THEME =====
BG = "#eef2f7"
CARD = "#ffffff"
TEXT = "#1f2937"
MUTED = "#6b7280"
ROW = "#f9fafb"

PRIMARY = "#6366f1"
DANGER = "#ef4444"


class DallyPlannerApp:

    def __init__(self, root, task_service, note_service, schedule_service):
        self.root = root
        self.root.title("Dally: Planner")
        self.root.geometry("520x650")
        self.root.configure(bg=BG)

        self.tasks = task_service
        self.notes = note_service
        self.schedule = schedule_service

        # ===== NAVBAR =====
        nav = tk.Frame(root, bg=CARD)
        nav.pack(fill="x")

        for name, cmd in [
            ("Tasks", self.show_tasks),
            ("Notes", self.show_notes),
            ("Schedule", self.show_schedule),
            ("Report", self.show_dashboard)
        ]:
            tk.Button(nav, text=name, bg=PRIMARY, fg="white",
                      relief="flat", padx=10,
                      command=cmd).pack(side="left", padx=5, pady=5)

        # ===== CONTAINER =====
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

    # ===== NAV =====
    def hide_all(self):
        for p in [self.task_page, self.note_page, self.schedule_page, self.dashboard_page]:
            p.pack_forget()

    def show_tasks(self):
        self.hide_all()
        self.task_page.pack(expand=True)

    def show_notes(self):
        self.hide_all()
        self.note_page.pack(expand=True)

    def show_schedule(self):
        self.hide_all()
        self.schedule_page.pack(expand=True)
        self.render_schedule()

    def show_dashboard(self):
        self.hide_all()
        self.dashboard_page.pack(expand=True)
        self.generate_dashboard()

    # ===== TASKS =====
    def build_tasks(self):
        card = tk.Frame(self.task_page, bg=CARD, padx=20, pady=20)
        card.pack(expand=True)

        tk.Label(card, text="TASKS", font=("Segoe UI", 16, "bold"),
                 bg=CARD, fg=TEXT).pack(pady=10)

        self.task_entry = tk.Entry(card, width=30)
        self.task_entry.pack(pady=5)

        tk.Button(card, text="Add Task", bg=PRIMARY, fg="white",
                  command=self.add_task).pack(pady=5)

        self.task_list = tk.Frame(card, bg=CARD)
        self.task_list.pack()

    def add_task(self):
        t = self.task_entry.get()
        if t:
            self.tasks.add(t)
            self.task_entry.delete(0, tk.END)
            self.render_tasks()

    def render_tasks(self):
        for w in self.task_list.winfo_children():
            w.destroy()

        for i, t in enumerate(self.tasks.get_all()):
            row = tk.Frame(self.task_list, bg=ROW)
            row.pack(fill="x", pady=3)

            var = tk.BooleanVar(value=t["completed"])

            tk.Checkbutton(row, text=t["task"], variable=var,
                           bg=ROW,
                           command=lambda i=i, v=var:
                           self.tasks.toggle(i, v.get())).pack(side="left")

            tk.Button(row, text="✕", bg=ROW, fg=DANGER,
                      command=lambda i=i: self.delete_task(i)
                      ).pack(side="right")

    def delete_task(self, i):
        self.tasks.delete(i)
        self.render_tasks()

    # ===== NOTES =====
    def build_notes(self):
        card = tk.Frame(self.note_page, bg=CARD, padx=20, pady=20)
        card.pack(expand=True)

        tk.Label(card, text="NOTES", font=("Segoe UI", 16, "bold"),
                 bg=CARD, fg=TEXT).pack(pady=10)

        self.note_entry = tk.Entry(card, width=40)
        self.note_entry.pack(pady=5)

        tk.Button(card, text="Add Note", bg=PRIMARY, fg="white",
                  command=self.add_note).pack(pady=5)

        self.note_list = tk.Frame(card, bg=CARD)
        self.note_list.pack()

    def add_note(self):
        n = self.note_entry.get()
        if n:
            self.notes.add(n)
            self.note_entry.delete(0, tk.END)
            self.render_notes()

    def render_notes(self):
        for w in self.note_list.winfo_children():
            w.destroy()

        for i, n in enumerate(self.notes.get_all()):
            row = tk.Frame(self.note_list, bg=ROW)
            row.pack(fill="x", pady=3)

            tk.Label(row, text=n, bg=ROW).pack(side="left")

            tk.Button(row, text="✕", bg=ROW, fg=DANGER,
                      command=lambda i=i: self.delete_note(i)
                      ).pack(side="right")

    def delete_note(self, i):
        self.notes.delete(i)
        self.render_notes()

    # ===== SCHEDULE (FIXED UI) =====
    def build_schedule(self):
        card = tk.Frame(self.schedule_page, bg=CARD, padx=20, pady=20)
        card.pack(expand=True)

        tk.Label(card, text="SCHEDULE", font=("Segoe UI", 16, "bold"),
                 bg=CARD, fg=TEXT).pack(pady=10)

        # INPUT ROWS (LABEL BESIDE INPUT)
        def row(label):
            r = tk.Frame(card, bg=CARD)
            r.pack(pady=2)
            tk.Label(r, text=label, width=8, anchor="w",
                     bg=CARD, fg=MUTED).pack(side="left")
            entry = tk.Entry(r, width=25)
            entry.pack(side="left")
            return entry

        self.date = row("Date:")
        self.time = row("Time:")
        self.task = row("Task:")

        tk.Button(card, text="Add Schedule",
                  bg=PRIMARY, fg="white",
                  command=self.add_schedule).pack(pady=5)

        tk.Button(card, text="Clear",
                  bg=DANGER, fg="white",
                  command=self.clear_schedule).pack(pady=3)

        # TABLE
        self.schedule_table = tk.Frame(card, bg=CARD)
        self.schedule_table.pack(pady=10)

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
        for w in self.schedule_table.winfo_children():
            w.destroy()

        # HEADER
        header = tk.Frame(self.schedule_table, bg=ROW)
        header.pack(fill="x")

        for text, w in [("Date", 10), ("Time", 10), ("Task", 20)]:
            tk.Label(header, text=text, width=w,
                     bg=ROW, fg=MUTED).pack(side="left")

        # ROWS
        for item in self.schedule.get_all():
            row = tk.Frame(self.schedule_table, bg=ROW)
            row.pack(fill="x", pady=2)

            tk.Label(row, text=item["date"], width=10, bg=ROW).pack(side="left")
            tk.Label(row, text=item["time"], width=10, bg=ROW).pack(side="left")
            tk.Label(row, text=item["task"], width=20, bg=ROW).pack(side="left")

    # ===== DASHBOARD (FIXED) =====
    def build_dashboard(self):
        card = tk.Frame(self.dashboard_page, bg=CARD, padx=20, pady=20)
        card.pack(expand=True)

        tk.Label(card, text="REPORT SUMMARY",
                 font=("Segoe UI", 16, "bold"),
                 bg=CARD, fg=TEXT).pack(pady=10)

        self.report = tk.Text(card, width=45, height=20, bg=ROW)
        self.report.pack()

    def generate_dashboard(self):
        self.report.delete("1.0", tk.END)

        self.report.insert(tk.END, "TASKS\n")
        for t in self.tasks.get_all():
            mark = "✔" if t["completed"] else "○"
            self.report.insert(tk.END, f"{mark} {t['task']}\n")

        self.report.insert(tk.END, "\nNOTES\n")
        for n in self.notes.get_all():
            self.report.insert(tk.END, f"- {n}\n")

        self.report.insert(tk.END, "\nSCHEDULE\n")
        for s in self.schedule.get_all():
            self.report.insert(
                tk.END,
                f"{s['date']} {s['time']} → {s['task']}\n"
            )
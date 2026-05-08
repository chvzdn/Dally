from services.task_service_impl import TaskService
from services.schedule_service_impl import ScheduleService
from services.notes_service_impl import NotesService

# TEST: Add task
def test_add_task():
    service = TaskService()
    service.add("Study for Math Exam")
    assert len(service.get_all()) == 1

# TEST: Toggle task completion
def test_toggle_task():
    service = TaskService()
    service.add("Study for Math Exam")
    service.toggle(0, True)
    assert service.get_all()[0].completed is True

# TEST: Delete task
def test_delete_task():
    service = TaskService()
    service.add("Study for Math Exam")
    service.delete(0)
    assert len(service.get_all()) == 0

# TEST: Add note
def test_add_note():
    service = NotesService()
    service.add("Reminder:Wash Dishes")
    assert len(service.get_all()) == 1

# TEST: Clear schedule
def test_clear_schedule():
    service = ScheduleService()
    service.assign("May 11, 2026", "3PM", "Math Exam")
    service.clear()
    assert len(service.get_all()) == 0

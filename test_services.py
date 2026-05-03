from services.task_service_impl import TaskService

def test_add():
    t = TaskService()
    t.add("Test")
    assert len(t.get_all()) == 1
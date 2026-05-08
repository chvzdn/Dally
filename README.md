# Dally: Task Schedule Planner

## Application Description
Dally: Task Schedule Planner is a standalone Python application designed to help users efficiently organize their daily tasks, schedules, and personal notes in one centralized system.

The application allows users to:
- Create and manage tasks, including deleting and marking them as completed.
- Organize daily schedules by assigning tasks to specific dates and times.
- Store and manage short notes for reminders or important information.
- View a summarized dashboard that presents all tasks, notes, and schedules in a structured format. And can export the report to a `.txt` file.

Built with a clean graphical user interface, the system emphasizes simplicity, usability, and accessibility. It operates entirely offline and follows a structured Input → Process → Output model, ensuring reliable performance without relying on external databases or internet connectivity.

Through this application, users can improve their time management, maintain organization, and increase productivity by having all essential planning tools in a single, easy-to-use platform.

## OOP Concepts Used
This project demonstrates core Object-Oriented Programming principles:
- Encapsulation: Private attributes using `_variable`
- Abstraction: `IDataService` interface defines standard methods
- Polymorphism: Task, Notes, and Schedule services implement the same interface methods
- Modularity: Code is separated into models, services, interfaces, UI, and tests

## Technologies Used
- Python (core programming language)
- GUI framework (Tkinter)
- File handling for saving and retrieving tasks and notes

# Project Structure
```
DallyPlanner/
│
├── interfaces/
│   └── data_service.py
│
├── models/
│   ├── task.py
│   ├── note.py
│   └── schedule.py
│
├── services/
│   ├── task_service_impl.py
│   ├── notes_service_impl.py
│   ├── schedule_service_impl.py
│   └── report_service.py
│
├── ui/
│   └── main_gui.py
│
├── tests/
│   └── test_services.py
│
├── main.py
└── report.txt (generated after export)
```

## How to Run
1. Requirements
Python 3.x
2. Clone this repository:
   ```bash
   git clone https://github.com/chvzdn/dally.git

## Navigate to the project folder:
  ```bash
  cd dally
  ```

## Run the Application:
  ```bash
  python main.py
  ```

## Running Tests
Run tests using pytest:
```bash
pytest tests/
```

## Export Report
Inside the application:
1. Go to the Report tab
2. Click Export Report
3. Output file will be saved as:
```
report.txt
```

## Author 
Developed as a school project by:
- Renelyn May C. Dino ([GitHub Profile of Dino](https://github.com/chvzdn))
- Princess Sharmelle Betis ([GitHub Profile of Betis](https://github.com/betisprincesssharmelle-boop))
- Arlan Guañizo Jr. ([GitHub Profile of Guañizo](https://github.com/arlanjrguanizo94-stack?fbclid=IwY2xjawRqk3VleHRuA2FlbQIxMQBzcnRjBmFwcF9pZAEwAAEeiWgKMRaiwMlvR0e6XPxZIu3KObxTaRI1FLVIGKK3E9mgsQKAC2Z4-89xQkk_aem_ws-JIW5dkC9n7-Vd271urQ))

In Partial Fulfillment of the Requirements for the Subject CC103 Computer Programming 2 Under the Course of Bachelor of Science in Information Technology at Sorsogon State University Bulan Campus. With the Supervision of our Professor John Mark Gabrentina.

### Notes
- Basic input validation only (`strip()` checks)
- Focus is on OOP structure, not advanced error handling
- Designed for educational purposes

## sharmelle
## arlan

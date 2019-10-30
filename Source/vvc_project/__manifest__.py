{
    'name': 'VVC PROJECT TRAINING',
    'description': 'This is a new project about manage review task',
    'author': 'Phan Van Phuoc Thinh',
    'depends': ['project', 'hr_timesheet'],
    'application': True,
    'data': [
        'views/review_history_project_view.xml',
        'menus/menu_project.xml',
        'views/project_task_view.xml',
        'wizards/review_history_project_wizard.xml'
    ]
}
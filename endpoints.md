LIST with list entrys
create    POST   /api/v1/todo-list/             name:str
fetch one GET    /api/v1/todo-list/<pk>
fetch all GET    /api/v1/todo-list/
modify    PUT    /api/v1/todo-list/<pk>         name:str
delete    DELETE /api/v1/todo-list/<pk>

ENTRY
create    POST   /api/v1/todo-list-entry/       parent_list:pk text:str due_date:date finished:bool
fetch one GET    /api/v1/todo-list-entry/<pk>
fetch all GET    /api/v1/todo-list-entry/
modify    PUT    /api/v1/todo-list-entry/<pk>   parent_list:pk text:str due_date:date finished:bool
delete    DELETE /api/v1/todo-list-entry/<pk>


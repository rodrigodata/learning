use std::env;

struct TodoItem {
     name: String,
     completed: char
}

fn main() {
    let arguments: Vec<String> = env::args().collect();
    let command = arguments[1].clone();
    let todo_item = TodoItem {
        name: "Jantar".to_string(),
        completed: ' '
    };
    let todo_list = vec![todo_item];
    
    if command == "get" {
        for item in todo_list  {
            println!("[{}] - {}", item.completed, item.name);
        }
    }
}

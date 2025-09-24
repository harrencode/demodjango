"use client"

import { useEffect, useState } from "react"

type TodoItem = {
  id: number;
  title: string;
  content: string;
  completed: boolean;
  published_date: string;
};


export default function Home(){
    const [todos, setTodos] = useState<TodoItem[]>([]);
    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const [complete, setComplete] = useState<boolean>(false);

    //fetch from the backend

    const fetchTodos = async() => {
        const res = await fetch(`http://127.0.0.1:8000/api/todoitems/`);
        const data = await res.json();
        setTodos(data);
    };

    //create a todo note

    const addTodo = async(e:React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        await fetch (`http://127.0.0.1:8000/api/todoitems/create/`, {
            method: "POST",
            headers:{"Content-Type":"application/json"},
            body: JSON.stringify({ title,content, completed:complete}),

        });
        setTitle("");
        setContent("");
        fetchTodos();
    };

    //mark to do as complete or not

    const toggleTodo = async (id: number, completed: boolean) => {
        await fetch(`http://127.0.0.1:8000/api/todoitems/${id}/`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ completed: !completed }),
        });
        fetchTodos();
        };

    //delete a todo

    const deleteTodo = async(id:number) =>{
        await fetch(`http://127.0.0.1:8000/api/todoitems/${id}/`, {
            method: "DELETE",

        });
        fetchTodos();
    };

    useEffect(()=>{
        fetchTodos();
    },[]);


  return (
    <div className="font-sans grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-1 sm:p-">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        


         <h1 className="text-2xl font-bold mb-4">Todo List</h1>

            {/* add tofo form */}

            <form
              onSubmit={addTodo}
              className="bg-gray-800 shadow-lg rounded-2xl p-6 mb-6 max-w-md mx-auto space-y-4"
            >
              <div>
                <label className="block text-gray-300 font-medium mb-1">Title</label>
                <input
                  type="text"
                  placeholder="Enter title"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  className="w-full border border-gray-600 rounded-lg px-3 py-2 bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400"
                  required
                />
              </div>

              <div>
                <label className="block text-gray-300 font-medium mb-1">Content</label>
                <input
                  type="text"
                  placeholder="Enter content"
                  value={content}
                  onChange={(e) => setContent(e.target.value)}
                  className="w-full border border-gray-600 rounded-lg px-3 py-2 bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-400"
                  required
                />
              </div>

              <div className="flex items-center space-x-2">
                <input
                  type="checkbox"
                  checked={complete}
                  onChange={(e) => setComplete(e.target.checked)}
                  className="h-4 w-4 text-blue-500 border-gray-400 rounded focus:ring-blue-400"
                />
                <label className="text-gray-300">Completed</label>
              </div>

              <button
                type="submit"
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg px-4 py-2 transition duration-200"
              >
                Add Todo
              </button>
            </form>



        
            {/* Todo List */}
            <ul className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full max-w-6xl">
              {todos.map((todo) => {
                const formattedDate = new Date(todo.published_date).toLocaleString("en-US", {
                  dateStyle: "medium",
                  timeStyle: "short",
                });

                return (
                  <li
                    key={todo.id}
                    className="bg-white shadow-md rounded-xl p-5 flex flex-col justify-between border border-gray-200 hover:shadow-lg transition"
                  >
                    {/* Top: content */}
                    <div className="space-y-2 mb-4">
                      <h2 className="text-lg font-semibold text-gray-800">{todo.title}</h2>
                      <p className="text-gray-600">{todo.content}</p>
                      <p className="text-xs text-gray-500">📅 {formattedDate}</p>
                    </div>

                    {/* Bottom: buttons */}
                    <div className="flex justify-between items-center">
                      <button
                        onClick={() => toggleTodo(todo.id, todo.completed)}
                        className={`px-3 py-1.5 rounded-lg text-sm font-medium transition ${
                          todo.completed
                            ? "bg-green-100 text-green-700 border border-green-300 hover:bg-green-200"
                            : "bg-yellow-100 text-yellow-700 border border-yellow-300 hover:bg-yellow-200"
                        }`}
                      >
                        {todo.completed ? "✅ Done" : "⏳ Pending"}
                      </button>
                      <button
                        onClick={() => deleteTodo(todo.id)}
                        className="px-3 py-1.5 rounded-lg text-sm font-medium bg-red-100 text-red-700 border border-red-300 hover:bg-red-200 transition"
                      >
                        🗑 Delete
                      </button>
                    </div>
                  </li>
                );
              })}
            </ul>

      </main>

      

      
      
    </div>
  );
}


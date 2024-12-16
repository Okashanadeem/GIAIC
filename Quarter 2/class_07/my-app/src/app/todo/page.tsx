'use client'
import React, { useState } from 'react'

function page() {
  const [taskToDo, setTask] = useState(
    [
      { task: "Washing clothes", id: 1 },
      { task: "Cooking dinner", id: 2 },
    ]
  )

  const [Input, setInput] = useState("")
  const [id, setId] = useState(0)

  // function 
  const addTodo = () => {
    let obj: any = taskToDo.find(item => id == item.id)
    if (obj) {
      let newArray = taskToDo.filter(item => item.id !== obj.id)
      setTask([...newArray, { task: Input, id: id }])
      setInput("")
      setId(0)
      return
    }

    setTask([...taskToDo, { task: Input, id: id }])
    setInput("")
    setId(0)

  }

  const EditItem = (id: any) => {
    let obj: any = taskToDo.find((item) => id == item.id)
    setInput(obj.task)
    setId(obj.id)
  }

  const delItem = (id: any) => {
    let newArray = taskToDo.filter((item) => item.id !== id)
    setTask([...newArray])
  }
  return (
    <div className='max-w-4xl mx-auto p-5'>
      <h1 className='text-center font-bold text-[40px]'>Task Note</h1>

      {/* input div  */}
      <div className='flex justify-between gap-4 mt-5'>
        <input className='w-[60%] p-2 ml-3 text-lg border-b focus:outline-none'
          type="text"
          value={Input}
          onChange={(e) => { setInput(e.target.value) }}
          placeholder='Write a task' />
        <input className='w-[20%] p-2 ml-3 text-lg border-b focus:outline-none'
          type="number"
          value={id}
          onChange={(e: any) => { setId(e.target.value) }}
          placeholder='ID number' />
        <button className='bg-green-600 hover:bg-green-500 w-[20%] rounded p-2' onClick={addTodo}>Add Task</button>
      </div>


      {/* Task list*/}
      <h1 className='text-center font-bold text-[40px] mt-4 underline'>Today task</h1>
      <div className='grid grid-cols-2 gap-5 mt-5' >

        {taskToDo.map((item: any, id: any) => {
          return (
            <div className='shadow p-4 ' key={id}>
              <div className='flex justify-between'>
                <span className='h-6 w-6 text-center rounded-full my-auto text-lg'>{id + 1}</span>
                <span onClick={() => delItem(item.id)} className='h-6 w-6 text-center rounded-full my-auto text-lg text-red-700 cursor-pointer'>X</span>
              </div>
              <div className='text-[40px] text-gray-700'>{item.task}</div>
              <h1 onClick={() => EditItem(item.id)} className='text-right cursor-pointer'>Edit</h1>
            </div>
          )
        })}
      </div>
    </div>
  )
}

export default page

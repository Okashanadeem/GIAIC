"use client"
import { useEffect, useState } from "react";

export default function Home() {
  const [name, setName] = useState("Okasha")

  const [count,setCount] = useState(0)
  function Incriment(){
    setCount(count + 1)
  }

  useEffect(()=>{
    console.log("Page is Ready!"),[]} //render once
  )

  useEffect(()=>{
    console.log("Changes are updated!"),[]} //rener after the change
  )

  useEffect(()=>{
    console.log("1 is added"),[count]} //reder after change in something specific
  )
  
  useEffect(()=>{
  async function fetchData() {
    const url = await fetch("https://fakerapi.it/api/v1/persons?_locale=en_US&_quantity=1");
    const res = await url.json();
    console.log(res.data);
    setName(res.data[0].firstname)
  }
  fetchData()
},[count]
)
  
  return (
      <>
         <h1>User name:</h1>
         <p>{name}</p>
         <button onClick={Incriment}>Change Name</button>
        
        <br />        
        <br />

        <p>{count}</p>
         <button onClick={Incriment}>Incriment</button>
      </>
  );
}

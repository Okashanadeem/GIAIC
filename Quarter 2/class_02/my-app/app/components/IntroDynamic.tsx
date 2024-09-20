import React from 'react'

interface DynamicProps{
  name : string
  age : number
}
export const IntroDynamic = (props: DynamicProps) => {
  return (
    <div>
      <p>{`My name is ${props.name}. I am ${props.age} years's old.`}</p>
    </div>
  )
}

export default IntroDynamic

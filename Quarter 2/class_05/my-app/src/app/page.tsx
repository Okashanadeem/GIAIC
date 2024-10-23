import Image from "next/image";
import { Heading } from "../../components/Heading";
import img1 from "../../../my-app/images/img1.webp"


export default async function Home() {
  const url ="https://fakerapi.it/api/v1/persons?_locale=en_US&_quantity=1"
  const fetchData = await fetch(url, {cache:"no-store"})
  const res = await fetchData.json()
  console.log(res.data[0])
  return (
    <>
      <Heading props="Home Page"/>
      
      <Image 
      src={img1} //you can do this by importing the image 
      alt="img" 
      width={150} 
      height={150} 
      className="w-[400px] h-[400px] ml-5 rounded-full" 
      /> 

      <Image 
      src={require("../../../my-app/images/img2.jpg")} //you can directly do this here without importing the img
      alt="img" 
      width={200} 
      height={150} 
      className="w-[600px] h-[400px] ml-5 rounded-full" 
      /> 
      
      <p><b>First Name:</b>{res.data[0].firstname}
      <br/>
      <br/>
      <b>Last Name:</b>{res.data[0].lastname}</p>
    </>
  );
}

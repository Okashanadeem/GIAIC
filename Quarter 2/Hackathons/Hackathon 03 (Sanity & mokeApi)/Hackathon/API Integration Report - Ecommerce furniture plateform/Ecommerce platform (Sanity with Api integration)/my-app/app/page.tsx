import Navbar from "./myComponents/Navbar";
import Image from "next/image";
import sofa from "../public/images/sofa top home.png";
// import sofaItem from "../public/images/sofa home.png";
// import tableItem from "../public/images/table home.png";
import ItemsPage from "./myComponents/itemsHome";
import AsgardSofa from "../public/images/Asgaard sofa 1.png";
import boximg1 from "../public/images/Rectangle 13.png"
import boximg2 from "../public/images/Rectangle 14.png"
import boximg3 from "../public/images/Rectangle 15.png"
import { Calendar, Clock } from "lucide-react";
import Link from "next/link";
import Footer from "./myComponents/footer";

export default function Home() {
  return (

    <div>
      {/* Navbar  */}
      <Navbar />
      
      <div className="h-[100vh] w-auto bg-[#FBEBB5]">
        {/* Homepage  */}
        <div className="flex flex-col md:flex-row justify-center items-center text-black h-full">
          {/* Text Section */}
          <div className="text-center md:text-left md:ml-32 px-4 md:px-0">
            <h1 className="text-3xl md:text-5xl font-semibold">Rocket single seater</h1>
            <p className=" text-lg md:text-2xl mt-4 md:mt-10"><Link href="/shop" className="flex items-center justify-center w-full sm:w-[215px] h-[48px] border border-black mt-4 hover:bg-black hover:text-[#FBEBB5] transition duration-300 ease-in-out transform hover:scale-105 bg-[#FBEBB5] text-black rounded-full ">Shop Now</Link></p>
          </div>

          {/* Image Section */}
          <div className="w-full max-w-sm md:max-w-none mt-40 md:h-[750px] md:w-[853px]">
            <Image
              src={sofa}
              alt="Sofa Image"
              className="w-full h-auto"
            />
          </div>
        </div>

        {/* <div className="bg-[#FAF4F4]  md:h-[672px] h-auto flex flex-col md:flex-row justify-center items-center pb-20 md:justify-between md:gap-10">
        <div className="w-full md:w-[605px] h-[562px] md:h-[562px] md:ml-24 p-5">
          <Image
            src={tableItem}
            alt="Table Image"
            className="w-full h-auto"
          />
          <h1 className="text-2xl md:text-5xl font-semibold">Side Table</h1>
          <p className="underline text-lg md:text-2xl mt-4 md:mt-10"><Link href="/shop" className="text-lg font-medium hover:underline">Shop Now</Link></p>
        </div>

        <div className="w-full md:w-[605px] h-[562px] md:h-[562px] md:mr-24 p-5">
          <Image
            src={sofaItem}
            alt="Sofa Image"
            className="w-full h-auto"
          />
          <h1 className="text-2xl md:text-5xl font-semibold md:mt-9">Sofa</h1>
          <p className="underline text-lg md:text-2xl mt-4 md:mt-10"><Link href="/shop" className="text-lg font-medium hover:underline">Shop Now</Link></p>
        </div>
      </div> */}
         
         {/* Featured Products  */}
        <div className="md:h-[777px] bg-white">
          <div className="flex flex-col justify-center mb-10 mt-10">
            <h3 className="text-2xl font-semibold text-center">Top Picks For You</h3>
            <p className="text-[#9F9F9F] text-center">Find a bright ideal to suit your taste with our great selection of suspension, floor and table lights.</p>
          </div>{ }
          <ItemsPage />
        </div>

        {/* New arrivals  */}
        <div className="bg-[#FFF9E5] h-auto md:h-[639px] flex flex-col md:flex-row justify-center items-center px-4 md:px-0">
          {/* Image Section */}
          <div className="flex justify-center md:mr-10">
            <Image
              src={AsgardSofa}
              alt="Asgard Sofa"
              className="w-full max-w-[983px]"
            />
          </div>


          {/* Text and Button Section */}
          <div className="w-auto md:w-[331px] flex flex-col items-center md:items-start justify-center ">
            <p className="text-2xl text-center md:text-left">New Arrivals</p>
            <h3 className="text-4xl font-extrabold text-center md:text-left">Asgaard Sofa</h3>
            <button className="border border-black rounded mt-5 w-48 h-11 bg-black text-white">
              <Link href="/shop" className="text-lg font-medium hover:text-[#FBEBB5]">Order Now</Link>
            </button>
          </div>
        </div>

        {/* Blog section  */}
        <div className="px-6 md:px-12 lg:px-16 py-16 bg-gray-50">
          {/* Section Header */}
          <div className="flex flex-col justify-center mb-10 text-center">
            <h3 className="text-4xl font-extrabold text-gray-800 mb-4">Our Blogs</h3>
            <p className="text-lg text-[#9F9F9F]">
              Find a bright idea to suit your taste with our great selection
            </p>
          </div>

          {/* Blog Cards */}
          <div className="grid gap-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
            {/* Blog Card 1 */}
            <div className="flex flex-col items-center w-full bg-white rounded-lg shadow-xl overflow-hidden transform hover:scale-105 transition-transform duration-300">
              <Image src={boximg1} alt="Blog 1" className="w-full h-56 object-cover mb-4 " />
              <div className="p-4">
                <p className="text-lg font-semibold text-gray-800 mb-2 text-center">Going all-in with millennial design</p>
                <p className="mb-4 text-xl text-[#4c4837] cursor-pointer text-center transition duration-200">Read More</p>
                <div className="flex gap-4 justify-center pt-1 text-sm text-gray-500">
                  <span className="flex items-center">
                    <Clock className="w-4 h-4 mr-1" />
                    5 min
                  </span>
                  <span className="flex items-center">
                    <Calendar className="w-4 h-4 mr-1" />
                    12<sup>th</sup> Oct 2022
                  </span>
                </div>
              </div>
            </div>

            {/* Blog Card 2 */}
            <div className="flex flex-col items-center w-full bg-white rounded-lg shadow-xl overflow-hidden transform hover:scale-105 transition-transform duration-300">
              <Image src={boximg2} alt="Blog 2" className="w-full h-56 object-cover mb-4 " />
              <div className="p-4">
                <p className="text-lg font-semibold text-gray-800 mb-2 text-center">Going all-in with millennial design</p>
                <p className="mb-4 text-xl text-[#4c4837]  cursor-pointer text-center transition duration-200 ">Read More</p>
                <div className="flex gap-4 justify-center pt-1 text-sm text-gray-500">
                  <span className="flex items-center">
                    <Clock className="w-4 h-4 mr-1" />
                    5 min
                  </span>
                  <span className="flex items-center">
                    <Calendar className="w-4 h-4 mr-1" />
                    12<sup>th</sup> Oct 2022
                  </span>
                </div>
              </div>
            </div>

            {/* Blog Card 3 */}
            <div className="flex flex-col items-center w-full bg-white rounded-lg shadow-xl overflow-hidden transform hover:scale-105 transition-transform duration-300">
              <Image src={boximg3} alt="Blog 3" className="w-full h-56 object-cover mb-4 " />
              <div className="p-4">
                <p className="text-lg font-semibold text-gray-800 mb-2 text-center">Going all-in with millennial design</p>
                <p className="mb-4 text-xl cursor-pointer text-center transition duration-200 text-[#4c4837]">Read More</p>
                <div className="flex gap-4 justify-center pt-1 text-sm text-gray-500">
                  <span className="flex items-center">
                    <Clock className="w-4 h-4 mr-1" />
                    5 min
                  </span>
                  <span className="flex items-center">
                    <Calendar className="w-4 h-4 mr-1" />
                    12<sup>th</sup> Oct 2022
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* View More Link */}
          <div className="mt-12 text-center flex justify-center">
            <Link
              href="https://giaic-milestone-03-blog-site-by-okasha-nadeem.vercel.app/"
              className="flex items-center justify-center w-full sm:w-[215px] h-[48px] border border-black rounded-xl mt-4 
                            hover:bg-black hover:text-white transition duration-300 ease-in-out transform hover:scale-105"
            >
              View More
            </Link>
          </div>
        </div>

        {/* instagram follow  */}
        <div className="bg-cover bg-center bg-fixed bg-[url('/images/Rectangle%2017.png')]  mt-12 pt-20 pb-24">
          <div className="flex flex-col items-center justify-center text-white text-center p-5">
            <h1 className="text-4xl font-extrabold text-black">Our Instagram</h1>
            <p className="mt-2 text-black">Follow our store on Instagram</p>
            <button className="flex items-center justify-center w-full sm:w-[215px] h-[48px] border border-black mt-4 
                            hover:bg-black hover:text-white transition duration-300 ease-in-out transform hover:scale-105 bg-white text-black rounded-full shadow-lg">Follow Us</button>
          </div>
        </div>
        <Footer />
      </div>
    </div>
  );
}

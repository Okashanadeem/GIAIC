import OptionCarousel from "./myComponents/optionCarousel";
import { AccordionDemo } from "./myComponents/CategoryAccordion";
import Category from "./myComponents/category";
import Listing2 from "./myComponents/listing2";
import Listing1 from "./myComponents/listing1";
import Image from "next/image";
import Speakerimg from "../public/images/Frame 600.png"
import Listing3 from "./myComponents/listing3";
import Featured from "./myComponents/featured";
import OurFeatures from "./myComponents/ourFeatures";

export default function Home() {
  return (
    <div className="space-y-10">
      {/* Option Carousel */}
      <AccordionDemo />
      <OptionCarousel />

      <Listing1 />
      <div className="flex justify-center">
        <button className="w-[234px] h-[56px] bg-[#DB4444] text-white rounded">View All Products</button>
      </div>

      <hr className="w-full max-w-[1170px] mt-10 mb-10 mx-auto border-gray-300" />
      {/* Category  */}
      <Category />

      {/* listing  */}
      <Listing2 />

      <div className="m-24 h-auto">
        <Image src={Speakerimg} alt="Speaker img" />
      </div>
      {/* listing  */}
      <Listing3 />
      <div className="flex justify-center">
        <button className="w-[234px] h-[56px] bg-[#DB4444] text-white rounded">View All Products</button>
      </div>
      <Featured />
      <OurFeatures/>
    </div>
  );
}

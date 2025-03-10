import React from 'react';
import { ChevronRight } from 'lucide-react';
import Image from 'next/image';
import img from '../../public/images/Frame 560.png';

function OptionCarousel() {
  return (
    <div className="md:flex  md:flex-row items-start md:items-center">
      {/* Menu Options */}

      <div className="hidden md:block w-full md:w-auto pl-6 pr-6 md:pl-8 md:pr-12 border-b md:border-b-0 md:border-r border-gray-300">
        <ul className="mt-6 space-y-3 ml-20">
          <li className="flex justify-between text-gray-700 hover:text-black">
            <span className="mr-14">Woman's Fashion</span>
            <ChevronRight className="w-5 h-5 text-gray-500" />
          </li>
          <li className="flex justify-between text-gray-700 hover:text-black">
            <span>Men's Fashion</span>
            <ChevronRight className="w-5 h-5 text-gray-500" />
          </li>
          <li className="text-gray-700 hover:text-black">Electronics</li>
          <li className="text-gray-700 hover:text-black">Home & Lifestyle</li>
          <li className="text-gray-700 hover:text-black">Medicine</li>
          <li className="text-gray-700 hover:text-black">Sports & Outdoor</li>
          <li className="text-gray-700 hover:text-black">Baby's & Toys</li>
          <li className="text-gray-700 hover:text-black">Groceries & Pets</li>
          <li className="text-gray-700 hover:text-black">Health & Beauty</li>
        </ul>
      </div>



      {/* Carousel */}
      <div className="w-full md:w-auto md:flex-1 m-7 pr-20">
        <Image
          src={img}
          alt="Hero Image"
          width={892}
          height={344}
        />
      </div>
    </div>
  );
}

export default OptionCarousel;

'use client';
import logo from '../../public/images/Meubel House_Logos-05.png';
import Footer from '../myComponents/footer';
import Navbar from "../myComponents/Navbar";
import { ChevronRight } from "lucide-react";
import Image from "next/image";

const AboutPage = () => {
  return (
    <div>
      <Navbar />
            <div
                className="bg-cover bg-center bg-fixed pt-20 pb-24 "
                style={{
                    backgroundImage: "url('/images/Rectangle 1.png')",
                }}
            >
                <div className="flex flex-col items-center justify-center h-full px-4 md:px-8 lg:px-16">
                    <Image src={logo} alt='Logo' />
                    <h1 className='text-4xl'>About Us</h1>
                    <p className='flex'>Home<ChevronRight /> About</p>
                </div>
            </div>
    <div className="bg-[#FBEBB5] text-black">
      {/* Hero Section */}
      <div className="flex flex-col items-center text-center px-6 py-16 bg-[#FAF4F4]">
        <h1 className="text-4xl md:text-5xl font-extrabold">About Us</h1>
        <p className="mt-4 text-lg md:text-xl text-gray-700 max-w-2xl">
          Crafting furniture with a perfect blend of elegance and durability. Discover the artistry behind every piece we create.
        </p>
      </div>

      {/* Story Section */}
      <div className="flex flex-col md:flex-row items-center justify-between px-6 md:px-16 py-12 bg-white gap-8">
        <div className="md:w-1/2">
          <h2 className="text-3xl font-semibold">Our Story</h2>
          <p className="mt-4 text-gray-600 leading-relaxed">
            Established with a passion for timeless design and craftsmanship, we’ve been delivering premium-quality furniture for over a decade.
            Each piece tells a story, crafted to complement your living space and elevate your lifestyle.
          </p>
        </div>
      </div>

      {/* Values Section */}
      <div className="px-6 md:px-16 py-12">
        <h2 className="text-3xl font-semibold text-center mb-8">Why Choose Us</h2>
        <div className="grid gap-8 md:grid-cols-3">
          {/* Value Card 1 */}
          <div className="flex flex-col items-center text-center bg-[#FAF4F4] p-6 rounded-lg shadow-md">
            <div className="w-20 h-20 mb-4 bg-gray-200 rounded-full"></div>
            <h3 className="text-xl font-bold">Luxury Living</h3>
            <p className="text-gray-600 mt-2">
              Our designs bring elegance and luxury into your living spaces, perfectly tailored to your tastes.
            </p>
          </div>

          {/* Value Card 2 */}
          <div className="flex flex-col items-center text-center bg-[#FAF4F4] p-6 rounded-lg shadow-md">
            <div className="w-20 h-20 mb-4 bg-gray-200 rounded-full"></div>
            <h3 className="text-xl font-bold">Quality Assurance</h3>
            <p className="text-gray-600 mt-2">
              Every piece is crafted with precision and undergoes rigorous quality checks for unmatched durability.
            </p>
          </div>

          {/* Value Card 3 */}
          <div className="flex flex-col items-center text-center bg-[#FAF4F4] p-6 rounded-lg shadow-md">
            <div className="w-20 h-20 mb-4 bg-gray-200 rounded-full"></div>
            <h3 className="text-xl font-bold">Sustainable Craftsmanship</h3>
            <p className="text-gray-600 mt-2">
              Committed to sustainability, we source materials responsibly to create eco-friendly furniture.
            </p>
          </div>
        </div>
      </div>

      {/* Call to Action */}
      <div className="flex flex-col items-center justify-center text-center bg-[#FFF9E5] px-6 py-12">
        <h2 className="text-3xl font-semibold">Join Our Legacy</h2>
        <p className="mt-4 text-lg text-gray-600 max-w-xl">
          Be part of our journey to transform homes with furniture that blends aesthetics and function seamlessly.
        </p>
        <button className="mt-6 px-6 py-3 bg-black text-white rounded-full shadow-md">
          <a href="/shop">Explore Our Collection</a>
        </button>
      </div>
    </div>
    <Footer/>
    </div>
  );
};

export default AboutPage;

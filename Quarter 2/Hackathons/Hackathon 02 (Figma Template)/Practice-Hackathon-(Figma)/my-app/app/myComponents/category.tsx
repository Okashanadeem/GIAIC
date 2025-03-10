import { ArrowLeft, ArrowRight, Camera, Gamepad, Headphones, Laptop, Smartphone, Watch } from 'lucide-react'
import React from 'react'
import ProductSection from './productSection'

const Category = () => {
    return (
        <div>
            <div className="md:ml-[100px] m-auto max-w-[1170px] px-4">
                <div className="flex flex-col gap-6 md:flex-row md:items-center justify-between px-4">
                    {/* Product Section Content */}
                    <div className="flex flex-col items-center md:items-start text-center md:text-left space-y-4 w-full md:w-auto">
                        <ProductSection
                            heading="Browse By Category"
                            subHeading="Categories"
                            showTime={false} // Show the timer section
                            action={null} // Leave action outside for better alignment on small screens
                            product={[]} // Pass your product list or keep as an empty array for now
                            isCarousal={false} // Disable carousel behavior
                        />
                    </div>

                    {/* Action Buttons */}
                    <div className="flex justify-center md:justify-start gap-4 w-full md:w-auto md:mt-20">
                        {/* Left Arrow Button */}
                        <button className="flex items-center justify-center bg-[#F5F5F5] rounded-full h-[46px] w-[46px] p-2 hover:bg-gray-200">
                            <ArrowLeft className="h-[24px] w-[24px]" />
                        </button>
                        {/* Right Arrow Button */}
                        <button className="flex items-center justify-center bg-[#F5F5F5] rounded-full h-[46px] w-[46px] p-2 hover:bg-gray-200">
                            <ArrowRight className="h-[24px] w-[24px]" />
                        </button>
                    </div>
                </div>
            </div>

            {/* categories  */}
            {/* Categories */}
<div className="flex justify-center items-center mt-[60px] gap-[30px] ml-[12px] mr-10 flex-wrap md:flex-nowrap">
  {/* Category Item */}
  <div className="hover:bg-red-500 w-[170px] h-[140px] flex flex-col justify-center items-center rounded-md border-[#00000053] border hover:border-none">
    <Smartphone className="w-[56px] h-[56px]" />
    <p className="text-white mt-2 font-medium">Camera</p>
  </div>

  <div className="hover:bg-red-500 w-[170px] h-[140px] flex flex-col justify-center items-center rounded-md border-[#00000053] border hover:border-none">
    <Laptop className="w-[56px] h-[56px]" />
    <p className="text-black hover:text-white mt-2 font-medium">Laptop</p>
  </div>

  <div className="hover:bg-red-500 w-[170px] h-[140px] flex flex-col justify-center items-center rounded-md border-[#00000053] border hover:border-none">
    <Watch className="w-[56px] h-[56px]" />
    <p className="text-black hover:text-white mt-2 font-medium">Watch</p>
  </div>

  <div className="hover:bg-red-500 w-[170px] h-[140px] flex flex-col justify-center items-center rounded-md border-[#00000053] border hover:border-none">
    <Headphones className="w-[56px] h-[56px]" />
    <p className="text-black hover:text-white mt-2 font-medium">Headphones</p>
  </div>

  <div className="hover:bg-red-500 w-[170px] h-[140px] flex flex-col justify-center items-center rounded-md border-[#00000053] border hover:border-none">
    <Camera className="w-[56px] h-[56px]" />
    <p className="text-black hover:text-white mt-2 font-medium">Camera</p>
  </div>

  <div className="hover:bg-red-500 w-[170px] h-[140px] flex flex-col justify-center items-center rounded-md border-[#00000053] border hover:border-none">
    <Gamepad className="w-[56px] h-[56px]" />
    <p className="text-black hover:text-white mt-2 font-medium">Gamepad</p>
  </div>
</div>


        </div>
    )
}

export default Category
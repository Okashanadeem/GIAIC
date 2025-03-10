import React from 'react'
import ProductSection from './productSection'
import { ArrowLeft, ArrowRight } from 'lucide-react'
import ProductCard from '../ProductCardProps'
import cout from "../../public/images/cout.png"
import bag from "../../public/images/Bag.png"
import cooler from "../../public/images/Cpu Cooler.png"
import shelf from "../../public/images/Book Shelf.png"



const Listing3 = () => {
  return (
    <div>
       {/* Product Section */}
       <div className="md:ml-[100px] m-auto max-w-[1170px] px-4">
 <div className="flex flex-col gap-6 md:flex-row md:items-center justify-between px-4">
{/* Product Section Content */}
<div className="flex flex-col items-center md:items-start text-center md:text-left space-y-4 w-full md:w-auto">
<ProductSection
 heading="Flash Sales"
 subHeading="Today's"
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

      {/* Product Listing */}
      <div className="m-auto max-w-[1080px] px-4 mt-10">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 justify-center">
        {/* Product Card */}
        <ProductCard
          image={cout}
          discount="-40%"
          name="The north coat"
          price="$260"
          delPrice="$360"
          rating={5}
          numOfPieces={65}
        />
        <ProductCard
          image={bag}
          discount="-40%"
          name="Gucci duffle bag"
          price="$960"
          delPrice="$1160"
          rating={4}
          numOfPieces={65}
        />
        <ProductCard
          image={cooler}
          discount="-40%"
          name="RGB liquid CPU Cooler"
          price="$170"
          delPrice="400"
          rating={4}
          numOfPieces={65}
        />
        <ProductCard
          image={shelf}
          discount="-40%"
          name="Small BookSelf"
          price="$360"
          delPrice=""
          rating={5}
          numOfPieces={65}
        />
         <ProductCard
          image={cout}
          discount="-40%"
          name="The north coat"
          price="$260"
          delPrice="$360"
          rating={5}
          numOfPieces={65}
        />
        <ProductCard
          image={bag}
          discount="-40%"
          name="Gucci duffle bag"
          price="$960"
          delPrice="$1160"
          rating={4}
          numOfPieces={65}
        />
        <ProductCard
          image={cooler}
          discount="-40%"
          name="RGB liquid CPU Cooler"
          price="$170"
          delPrice="400"
          rating={4}
          numOfPieces={65}
        />
        <ProductCard
          image={shelf}
          discount="-40%"
          name="Small BookSelf"
          price="$360"
          delPrice=""
          rating={5}
          numOfPieces={65}
        />
      </div>
      </div>
      </div>
  )
}

export default Listing3
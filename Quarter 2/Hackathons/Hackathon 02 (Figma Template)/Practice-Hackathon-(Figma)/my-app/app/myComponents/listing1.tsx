import React from 'react'
import ProductCard from '../ProductCardProps'
import { ArrowLeft, ArrowRight } from 'lucide-react'
import ProductSection from './productSection'
import gamepad from "../../public/images/gamepad.png";
import Gamingkeyboard from "../../public/images/Gamingkeyboard.png";
import Monitor from "../../public/images/Gaming Monitor.png";
import chair from "../../public/images/chair.png";


const Listing1 = () => {
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
 showTime={true} // Show the timer section
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
 <div className="m-auto max-w-[1080px] px-4">
 <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 justify-center">
   {/* Product Card */}
   <ProductCard
     image={gamepad}
     discount="-40%"
     name="HAVIT HV-G92 Gamepad"
     price="$120"
     delPrice="160"
     rating={5}
     numOfPieces={88}
   />
   <ProductCard
     image={Gamingkeyboard}
     discount="-40%"
     name="AK-900 Wired Keyboard"
     price="$120"
     delPrice="1160"
     rating={5}
     numOfPieces={75}
   />
   <ProductCard                  
     image={Monitor}
     discount="-40%"
     name="IPS LCD Gaming Monitor"
     price="$120"
     delPrice="400"
     rating={5}
     numOfPieces={99}
   />
   <ProductCard
     image={chair}
     discount="-40%"
     name="S-Series Comfort Chair "
     price="$120"
     delPrice="400"
     rating={5}
     numOfPieces={99}
   />
 </div>
 </div>
    </div>
  )
}

export default Listing1
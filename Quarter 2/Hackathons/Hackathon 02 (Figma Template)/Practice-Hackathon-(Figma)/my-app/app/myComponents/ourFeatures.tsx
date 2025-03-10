import { Headphones, ShieldCheck, Truck } from 'lucide-react';
import React from 'react';

const OurFeatures = () => {
    return (
      <div className="flex flex-col md:flex-row justify-center items-center gap-10 px-4 py-10">
        {/* Feature 1 */}
        <div className="flex flex-col items-center text-center md:items-start md:text-left max-w-[300px]">
          <div className="flex justify-center items-center w-[60px] h-[60px] bg-gray-800 rounded-full mb-4">
            <Truck className="text-white w-[30px] h-[30px]" />
          </div>
          <h3 className="text-lg font-semibold text-gray-800">FREE AND FAST DELIVERY</h3>
          <p className="text-sm text-gray-600">Free delivery for all orders over $140</p>
        </div>
  
        {/* Feature 2 */}
        <div className="flex flex-col items-center text-center md:items-start md:text-left max-w-[300px]">
          <div className="flex justify-center items-center w-[60px] h-[60px] bg-gray-800 rounded-full mb-4">
            <Headphones className="text-white w-[30px] h-[30px] " />
          </div>
          <h3 className="text-lg font-semibold text-gray-800">24/7 CUSTOMER SERVICE</h3>
          <p className="text-sm text-gray-600">Friendly 24/7 customer support</p>
        </div>
  
        {/* Feature 3 */}
        <div className="flex flex-col items-center text-center md:items-start md:text-left max-w-[300px]">
          <div className="flex justify-center items-center w-[60px] h-[60px] bg-gray-800 rounded-full mb-4">
            <ShieldCheck className="text-white w-[30px] h-[30px]" />
          </div>
          <h3 className="text-lg font-semibold text-gray-800">MONEY BACK GUARANTEE</h3>
          <p className="text-sm text-gray-600">We return money within 30 days</p>
        </div>
      </div>
    );
  };
  
export default OurFeatures;

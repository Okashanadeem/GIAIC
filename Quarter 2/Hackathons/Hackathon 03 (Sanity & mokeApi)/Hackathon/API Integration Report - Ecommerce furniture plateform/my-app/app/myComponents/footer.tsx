import Link from 'next/link';
import React from 'react';

const Footer = () => {
  return (
    <>
      {/* Footer Main Section */}
      <div className="w-full bg-white text-black py-16 px-6 md:px-12 lg:px-24">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
          {/* Address Section */}
          <div className="flex items-center">
            <p className="text-[#9F9F9F] text-sm">
              G223 M.T Khan Road <br/>
              SultanAbad Karachi,<br />
              Pakistan
              
            </p>
          </div>

          {/* Links Section */}
          <div>
  <h1 className="mb-6 text-sm font-bold text-[#9F9F9F]">Links</h1>
  <ul className="space-y-4">
    <li className="text-sm">
      <Link href="/" className="text-sm hover:text-blue-400 transition-colors duration-300">Home</Link>
    </li>
    <li className="text-sm">
      <Link href="/shop" className="text-sm hover:text-blue-400 transition-colors duration-300">Shop</Link>
    </li>
    <li className="text-sm">
      <Link href="/about" className="text-sm hover:text-blue-400 transition-colors duration-300">About</Link>
    </li>
    <li className="text-sm">
      <Link href="/contact" className="text-sm hover:text-blue-400 transition-colors duration-300">Contact</Link>
    </li>
  </ul>
</div>


          {/* Help Section */}
          <div>
            <h1 className="mb-6 text-sm font-bold text-[#9F9F9F]">Help</h1>
            <ul className="space-y-4">
              <li className="text-sm">Payment Options</li>
              <li className="text-sm">Return</li>
              <li className="text-sm">Privacy Policies</li>
            </ul>
          </div>

          {/* Newsletter Section */}
          <div>
            <h1 className="mb-6 text-sm font-bold text-[#9F9F9F]">Newsletter</h1>
            <div className="flex">
              <input
                type="text"
                placeholder="Enter Your Email Address"
                className="border-b-2 border-black px-2 py-1 text-sm focus:outline-none mr-2"
              />
              <button className="border-b-2 border-black text-sm px-4 py-1">
                SUBSCRIBE
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Footer Bottom Section */}
      <div className="w-full bg-white border-t border-gray-200">
        <div className="py-6 items-center text-center text-sm text-gray-500">
          <p>2022 Meubel House. All rights reserved.</p>
        </div>
      </div>
    </>
  );
};

export default Footer;

import React from 'react';
import { Heart, Eye } from 'lucide-react';
import Image from 'next/image';
import { StaticImageData } from 'next/image';


interface ProductCardProps {
  image: string | StaticImageData; // Ensure compatibility with Next.js Image
  discount: string;
  name: string;
  price: string;
  delPrice: string;
  rating: number; // Rating out of 5
  numOfPieces: number;
}

const ProductCard: React.FC<ProductCardProps> = ({
  image,
  discount,
  name,
  price,
  delPrice,
  rating,
  numOfPieces,
}) => {
  return (
    <div className="w-full max-w-[250px] rounded-sm p-4 relative bg-white group">
      {/* Discount Badge */}
      <div className="absolute top-3 left-3 bg-red-500 text-white text-xs font-bold rounded-md px-2 py-1 z-10">
        {discount}
      </div>

      {/* Product Image */}
      <div className="relative">
        <Image
          src={image}
          alt={name}
          className="w-full h-[180px] object-contain rounded-md bg-[#F5F5F5] p-8"
        />

        {/* Hover Icons */}
        <div className="absolute top-2 right-2 space-y-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-10">
          <div className="bg-white shadow-md p-2 rounded-full cursor-pointer hover:bg-gray-100">
            <Heart className="text-gray-600" size={20} />
          </div>
          <div className="bg-white shadow-md p-2 rounded-full cursor-pointer hover:bg-gray-100">
            <Eye className="text-gray-600" size={20} />
          </div>
        </div>
      </div>

      {/* Add to Cart Hover */}
      <div className="absolute bottom-0 left-0 w-full text-center bg-black text-white text-sm font-medium py-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-10">
        Add To Cart
      </div>

      {/* Product Name */}
      <div className="mt-3 text-black text-lg font-medium truncate">{name}</div>

      {/* Price */}
      <div className="mt-3 text-lg">
        <span className="text-red-500 font-semibold">{price}</span>{' '}
        <span className="text-gray-400 line-through">{delPrice}</span>
      </div>

      {/* Star Ratings */}
      <div className="flex items-center space-x-1 mt-1">
        {Array.from({ length: 5 }).map((_, index) => (
          <span
            key={index}
            className={`${
              index < rating ? 'text-yellow-400' : 'text-gray-300'
            }`}
          >
            ★
          </span>
        ))}
        <span className="text-sm text-gray-600 ml-2">
          ({numOfPieces} pieces)
        </span>
      </div>
    </div>
  );
};

export default ProductCard;

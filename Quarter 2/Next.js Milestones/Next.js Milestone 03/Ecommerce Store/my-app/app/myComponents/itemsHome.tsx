import Image from "next/image";
import item1sofa from "../../public/images/Trenton modular sofa_3 1.png";
import item2chair from "../../public/images/Granite dining table with dining chair 1.png";
import item3stool from "../../public/images/Outdoor bar table and stool 1.png";
import item4mirror from "../../public/images/Plain console with teak mirror 1.png";
import Link from "next/link";

const items = [
  {
    src: item1sofa,
    alt: "Trenton modular sofa_3",
    name: "Trenton modular sofa_3",
    price: "Rs. 25,000.00",
  },
  {
    src: item2chair,
    alt: "Granite dining table with dining chair",
    name: "Granite dining table with dining chair",
    price: "Rs. 25,000.00",
  },
  {
    src: item3stool,
    alt: "Outdoor bar table and stool",
    name: "Outdoor bar table and stool",
    price: "Rs. 25,000.00",
  },
  {
    src: item4mirror,
    alt: "Plain console with teak mirror",
    name: "Plain console with teak mirror",
    price: "Rs. 25,000.00",
  },
];

export default function ItemsPage() {
  return (
    <div className="w-full px-6 py-10 md:px-12 lg:px-16">
      {/* Items List */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {items.map((item, index) => (
          <div
            key={index}
            className="flex flex-col items-center bg-white  p-4 rounded-md"
          >
            <Image
              src={item.src}
              alt={item.alt}
              className="h-auto w-full rounded-md"
            />
            <h4 className="text-center mt-4 font-semibold text-lg">{item.name}</h4>
            <p className="text-center text-gray-600 mt-2">{item.price}</p>
          </div>
        ))}
      </div>

      {/* View More Link */}
      <p className="underline text-center text-lg md:text-2xl mt-10">
        <Link href={"/"}>View More</Link>
      </p>
    </div>
  );
}

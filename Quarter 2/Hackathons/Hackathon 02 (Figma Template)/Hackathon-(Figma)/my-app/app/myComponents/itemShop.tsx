import Image from "next/image";
import item1sofa from "../../public/images/Trenton modular sofa_3 1.png";
import item2chair from "../../public/images/Granite dining table with dining chair 1.png";
import item3stool from "../../public/images/Outdoor bar table and stool 1.png";
import item4mirror from "../../public/images/Plain console with teak mirror 1.png";
import grainCoffeeTable from "../../public/images/Grain coffee table 1.png";
import kentCoffeeTable from "../../public/images/Kent coffee table 1.png";
import roundCoffeeTable from "../../public/images/Round coffee table_color 2 1.png";
import reclaimedTeakCoffeeTable from "../../public/images/Reclaimed teak coffee table 1.png";
import plainConsole from "../../public/images/Plain console_ 1.png"
import reclaimedTeakSideboard from "../../public/images/Reclaimed teak Sideboard 1.png";
import sjp0825 from "../../public/images/SJP_0825  1.png";
import bellaChairAndTable from "../../public/images/Bella chair and table 1.png";
import graniteSquareSideTable from "../../public/images/Granite square side table 2.png";
import asgaardSofa from "../../public/images/Asgaard sofa 2.png";
import mayaSofaThreeSeater from "../../public/images/Maya sofa three seater 1.png";
import outdoorSofaSet from "../../public/images/Outdoor sofa set 1.png"


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
    {
      src: grainCoffeeTable,
      alt: "Grain coffee table",
      name: "Grain coffee table",
      price: "Rs. 15,000.00",
    },
    {
      src: kentCoffeeTable,
      alt: "Kent coffee table",
      name: "Kent coffee table",
      price: "Rs. 225,000.00",
    },
    {
      src: roundCoffeeTable,
      alt: "Round coffee table_color 2",
      name: "Round coffee table_color 2",
      price: "Rs. 251,000.00",
    },
    {
      src: reclaimedTeakCoffeeTable,
      alt: "Reclaimed teak coffee table",
      name: "Reclaimed teak coffee table",
      price: "Rs. 25,200.00",
    },
    {
      src: plainConsole,
      alt: "Plain console",
      name: "Plain console",
      price: "Rs. 258,200.00",
    },
    {
      src: reclaimedTeakSideboard,
      alt: "Reclaimed teak Sideboard",
      name: "Reclaimed teak Sideboard",
      price: "Rs. 20,000.00",
    },
    {
      src: sjp0825,
      alt: "SJP_0825",
      name: "SJP_0825",
      price: "Rs. 200,000.00",
    },
    {
      src: bellaChairAndTable,
      alt: "Bella chair and table",
      name: "Bella chair and table",
      price: "Rs. 100,000.00",
    },
    {
      src: graniteSquareSideTable,
      alt: "Granite square side table",
      name: "Granite square side table",
      price: "Rs. 258,800.00",
    },
    {
      src: asgaardSofa,
      alt: "Asgaard sofa",
      name: "Asgaard sofa",
      price: "Rs. 250,000.00",
    },
    {
      src: mayaSofaThreeSeater,
      alt: "Maya sofa three seater",
      name: "Maya sofa three seater",
      price: "Rs. 115,000.00",
    },
    {
      src: outdoorSofaSet,
      alt: "Outdoor sofa set",
      name: "Outdoor sofa set",
      price: "Rs. 244,000.00",
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
    </div>
  );
}

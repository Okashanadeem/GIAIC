import { ChevronRight } from "lucide-react"
import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
  } from "../../components/ui/accordion"
  
  export function AccordionDemo() {
    return (
      <Accordion type="single" collapsible className="w-full">
        <AccordionItem value="item-1">
          <AccordionTrigger className="md:hidden px-2 border-none">Category</AccordionTrigger>
          <AccordionContent>
            {/* Menu Options */}
      <div className="w-full py-2 md:w-auto pl-6 pr-6 md:pl-8 md:pr-12 border-b md:border-b-0 md:border-r border-gray-300">
        <ul className="mt-6 space-y-3 ml-20">
          <li className="flex justify-between text-gray-700 hover:text-black ">
            <span className='mr-14'>Woman's Fashion</span>
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
          </AccordionContent>
        </AccordionItem>
      </Accordion>
    )
  }
  
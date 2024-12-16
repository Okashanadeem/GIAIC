import Image from "next/image";
import { AccordionDemo } from "./components/accordion";
import { AlertDialogDemo } from "./components/Alrtbox";
import { CardWithForm } from "./components/card";
import { CalendarDemo } from "./components/calender";
import { SheetDemo } from "./components/sheet";

export default function Home() {
  return (
    <>
        <div className="flex justify-end m-2"><SheetDemo/> </div>
    <div className="flex justify-center my-5"><CardWithForm/> </div>
    <AccordionDemo/>
    <div className="flex justify-center mt-5"><AlertDialogDemo/></div>
    <div className="flex justify-center mt-5"><CalendarDemo/> </div>

    </>
  );
}

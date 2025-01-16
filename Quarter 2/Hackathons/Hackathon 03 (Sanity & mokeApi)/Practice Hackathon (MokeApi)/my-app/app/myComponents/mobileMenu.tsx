import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetHeader, SheetTitle, SheetTrigger } from "@/components/ui/sheet";
import Link from "next/link";

export default function MobileNavbar() {
  return (
    <div className="flex justify-between items-center px-6 py-4 bg-white shadow-md sticky top-0 z-50 md:hidden">
      {/* Logo */}
      <div className="text-2xl font-bold">MyLogo</div>

      {/* Sheet for Mobile Menu */}
      <Sheet>
        <SheetTrigger asChild>
          <Button variant="outline">Menu</Button>
        </SheetTrigger>
        <SheetContent side="right" className="w-[250px]">
          <SheetHeader>
            <SheetTitle>Menu</SheetTitle>
          </SheetHeader>
          <div className="flex flex-col space-y-4 mt-4">
            <Link href="/" className="text-lg font-medium hover:underline">Home</Link>
            <Link href="/shop" className="text-lg font-medium hover:underline">Shop</Link>
            <Link href="/about" className="text-lg font-medium hover:underline">About</Link>
            <Link href="/contact" className="text-lg font-medium hover:underline">Contact</Link>
            <Link href="/account" className="text-lg font-medium hover:underline">My Account</Link>
          </div>
        </SheetContent>
      </Sheet>
    </div>
  );
}

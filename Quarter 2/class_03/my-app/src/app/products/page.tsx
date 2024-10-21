import Link from "next/link";

export default function Products(){
    return (
        <>
        <h1>This is product Listing</h1>
        <ol>
        <li><Link href={"/products/product"}>Product 01</Link></li>
        <li><Link href={"/products/product"}>Product 02</Link></li>
        <li><Link href={"/products/product"}>Product 03</Link></li>
        </ol>
        </>
    )
}
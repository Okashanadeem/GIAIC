import Link from "next/link";

export default function Products(){
    return (
        <>
        <h1>This is product page</h1>
        <ol>
        <li><Link href={"/products/product01"}>Product 01</Link></li>
        <li><Link href={"/products/product02"}>Product 02</Link></li>
        </ol>
        </>
    )
}
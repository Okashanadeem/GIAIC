import Link from "next/link";

export default async function Products(){
    const fetchData = await fetch("https://jsonplaceholder.typicode.com/posts")
    const res = await fetchData.json();
    console.log(res)
    return (
        <>
        <h1>This is product Listing</h1>
        <ol>
           {
            res.map((item:any,i:number) => {
                return(
                <li><Link href={`/products/${item.id}`}>{item.title}</Link></li>
                )
            })
        }
        </ol>
        </>
    )
}
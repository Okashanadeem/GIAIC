export default async function Product({ params }: { params: { product: string } }) {
    const fetchData = await fetch(`https://jsonplaceholder.typicode.com/posts/${params.product}`)
    const res = await fetchData.json();
    console.log(res)
    return (
        <>
            <h1>Product details:</h1>
            <h3>title: {res.title}</h3>
            <p>details: {res.body}</p>
            <p>product id: {res.id}</p>
        </>
    )
}

//we also made this route dynamic by typing [] on product folder.
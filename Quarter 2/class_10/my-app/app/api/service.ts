export const GetData = async <T>(url: string):Promise<T> => {
    const fetchData = await fetch(url);
    const res = fetchData.json()
    return res;
}
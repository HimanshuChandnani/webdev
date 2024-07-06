
function List({category = 'Category', item = []}) {
    
    const items = item

    // items.sort((a,b) => a.name.localeCompare(b.name)) // Alphabetical
    // items.sort((a,b) => b.name.localeCompare(a.name)) // reverse ALphabetical
    // items.sort((a,b) => a.amount - b.amount) // Ascending
    // items.sort((a,b) => b.amount - a.amount) // Descending

    const listItems = items.map(item => <li key={item.id}>{item.id}: {item.name}- <b>{item.amount}</b></li>)
    return(
        <>
            <h2>{category}</h2>
            <ul>{listItems}</ul>
        </>
    )
}

export default List
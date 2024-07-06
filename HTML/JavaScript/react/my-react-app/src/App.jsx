import Header from './Header.jsx'
import Footer from './Footer.jsx'
import Card from './Card.jsx'
import Marksheet from './Marksheet.jsx'
import List from './List.jsx'

function App() {

  const fruits = [{id: '1', name: 'Apple', amount: '123'}, 
    {id: 2, name: 'Mango', amount: 43}, 
    {id: 3, name: 'Banana', amount: 34}, 
    {id: 4, name: 'Orange', amount: 64}, 
    {id: 5, name: 'Watermelon', amount: 128}]

  return (
    <>
      <Header />
      <Card />
      <List item={fruits} category="Fruits" />
      <Marksheet />
      <Footer />
    </>
  )
}

export default App

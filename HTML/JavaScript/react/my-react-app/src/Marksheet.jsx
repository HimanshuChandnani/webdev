import Marks from './Marks.jsx'

function Marksheet() {
    return(
        <table><tbody>
            <Marks />
            <Marks name="Himanshu" english={80} hindi={75} maths={83} pass={true} />
            <Marks name="Raju" english={30} hindi={20} maths={21} pass={false} />
        </tbody></table>
    )
}

export default Marksheet
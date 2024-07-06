import PropTypes from 'prop-types'

function Marks({name = 'Name',english = 'English',hindi = 'Hindi',maths = 'Maths',pass = 'Result',}) {
    return(
        <tr>
            <td>{name}</td>
            <td>{english}</td>
            <td>{hindi}</td>
            <td>{maths}</td>
            <td>{pass == true ? 'passed' : (pass == false ? 'failed' : pass)}</td>
        </tr>
    )
}
// Marks.propTypes = {
//     name: PropTypes.string,
//     english: PropTypes.number,
//     hindi: PropTypes.number,
//     maths: PropTypes.number,
//     pass: PropTypes.bool,
// }

export default Marks
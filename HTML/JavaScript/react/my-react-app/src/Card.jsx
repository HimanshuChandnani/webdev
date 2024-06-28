import ImgSection from "./ImgModule/ImgSection";

function Card() {
    let style = {
        fontSize: '40px',
    }
    return(
        <div className="card">
            <ImgSection />
            <h2 style={style}>React</h2>
            <p>I am learning react and it is fun as hell</p>
        </div>
    )
}

export default Card
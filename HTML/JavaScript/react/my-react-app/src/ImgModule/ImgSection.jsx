import Logo from '../assets/react.svg'
import style from './style.module.css'

function ImgSection() {
    return(
        <img className={style.img} src={Logo} />
    )
}

export default ImgSection
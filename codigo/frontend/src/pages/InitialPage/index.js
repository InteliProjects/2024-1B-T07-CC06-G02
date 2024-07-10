import { useNavigate } from "react-router-dom";

import { Container, LogoView, InitView } from "./styles";
import Button from "../../components/Button";

import logo from "../../assets/logo-onda.png";

/**
 * InitialPage Component
 * 
 * This component represents the initial page of the application.
 * 
 * @returns {JSX.Element} InitialPage component.
 */
export default function InitialPage() {
    const navigate = useNavigate();

    return (
        <Container>
            <LogoView>
                <div>
                    <img src={logo} alt="Logo" />
                    <p>
                        @powered by <span>ONDA</span>
                    </p>
                </div>
                <div></div>
            </LogoView>
            <InitView>
                <div>
                    <h1>Bem vindo!</h1>
                    <Button width="50%" onClickFunc={() => navigate("/home")}>
                        Entrar
                    </Button>
                </div>
                <div></div>
            </InitView>
        </Container>
    );
}
